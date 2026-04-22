# Copyright The OpenTelemetry Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
OpenTelemetry SDK Configurator for Easy Instrumentation with Distros
"""

import logging
import logging.config
import os
import warnings
from abc import ABC, abstractmethod
from os import environ
from typing import (
    Any,
    Callable,
    List,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

from typing_extensions import Literal

from opentelemetry._logs import set_logger_provider
from opentelemetry.environment_variables import (
    OTEL_LOGS_EXPORTER,
    OTEL_METRICS_EXPORTER,
    OTEL_PYTHON_ID_GENERATOR,
    OTEL_TRACES_EXPORTER,
)
from opentelemetry.metrics import set_meter_provider
from opentelemetry.sdk._logs import (
    LoggerProvider,
    LoggingHandler,
    LogRecordProcessor,
)
from opentelemetry.sdk._logs.export import (
    BatchLogRecordProcessor,
    LogRecordExporter,
)
from opentelemetry.sdk.environment_variables import (
    _OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED,
    OTEL_EXPORTER_OTLP_LOGS_PROTOCOL,
    OTEL_EXPORTER_OTLP_METRICS_PROTOCOL,
    OTEL_EXPORTER_OTLP_PROTOCOL,
    OTEL_EXPORTER_OTLP_TRACES_PROTOCOL,
    OTEL_PYTHON_TRACER_CONFIGURATOR,
    OTEL_TRACES_SAMPLER,
    OTEL_TRACES_SAMPLER_ARG,
)
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import (
    MetricExporter,
    MetricReader,
    PeriodicExportingMetricReader,
)
from opentelemetry.sdk.resources import Attributes, Resource
from opentelemetry.sdk.trace import (
    SpanProcessor,
    TracerProvider,
    _TracerConfiguratorT,
)
from opentelemetry.sdk.trace.export import BatchSpanProcessor, SpanExporter
from opentelemetry.sdk.trace.id_generator import IdGenerator
from opentelemetry.sdk.trace.sampling import Sampler
from opentelemetry.semconv.resource import ResourceAttributes
from opentelemetry.trace import set_tracer_provider
from opentelemetry.util._importlib_metadata import entry_points

_EXPORTER_OTLP = "otlp"
_EXPORTER_OTLP_PROTO_GRPC = "otlp_proto_grpc"
_EXPORTER_OTLP_PROTO_HTTP = "otlp_proto_http"

_EXPORTER_BY_OTLP_PROTOCOL = {
    "grpc": _EXPORTER_OTLP_PROTO_GRPC,
    "http/protobuf": _EXPORTER_OTLP_PROTO_HTTP,
}

_EXPORTER_ENV_BY_SIGNAL_TYPE = {
    "traces": OTEL_TRACES_EXPORTER,
    "metrics": OTEL_METRICS_EXPORTER,
    "logs": OTEL_LOGS_EXPORTER,
}

_PROTOCOL_ENV_BY_SIGNAL_TYPE = {
    "traces": OTEL_EXPORTER_OTLP_TRACES_PROTOCOL,
    "metrics": OTEL_EXPORTER_OTLP_METRICS_PROTOCOL,
    "logs": OTEL_EXPORTER_OTLP_LOGS_PROTOCOL,
}

_RANDOM_ID_GENERATOR = "random"
_DEFAULT_ID_GENERATOR = _RANDOM_ID_GENERATOR

_OTEL_SAMPLER_ENTRY_POINT_GROUP = "opentelemetry_traces_sampler"

_logger = logging.getLogger(__name__)

ExporterArgsMap = Mapping[
    Union[
        Type,
        Type,
        Type,
        Type,
    ],
    Mapping,
]


class _ConfigurationExporterSpanProcessorT(Protocol):
    def __call__(self, span_exporter, *args, **kwargs):
        pass


class _ConfigurationExporterLogRecordProcessorT(Protocol):
    def __call__(self, exporter, *args, **kwargs):
        pass


def _import_config_components(selected_components, entry_point_name):
    component_implementations = []

    for selected_component in selected_components:
        try:
            component_implementations.append(
                (
                    selected_component,
                    next(
                        iter(
                            entry_points(
                                group=entry_point_name, name=selected_component
                            )
                        )
                    ).load(),
                )
            )
        except KeyError:
            raise RuntimeError(
                "Requested entry point '{}' not found".format(entry_point_name)
            )

        except StopIteration:
            raise RuntimeError(
                "Requested component '{}' not found in ".format(
                    selected_component
                )
                + "entry point '{}'".format(entry_point_name)
            )

    return component_implementations


def _get_sampler():
    return environ.get(OTEL_TRACES_SAMPLER, None)


def _get_id_generator():
    return environ.get(OTEL_PYTHON_ID_GENERATOR, _DEFAULT_ID_GENERATOR)


def _get_tracer_configurator():
    return environ.get(OTEL_PYTHON_TRACER_CONFIGURATOR, None)


def _get_exporter_entry_point(exporter_name, signal_type):
    if exporter_name not in (
        _EXPORTER_OTLP,
        _EXPORTER_OTLP_PROTO_GRPC,
        _EXPORTER_OTLP_PROTO_HTTP,
    ):
        return exporter_name

    # Checking env vars for OTLP protocol (grpc/http).
    otlp_protocol = environ.get(_PROTOCOL_ENV_BY_SIGNAL_TYPE) or environ.get(
        OTEL_EXPORTER_OTLP_PROTOCOL
    )

    if not otlp_protocol:
        if exporter_name == _EXPORTER_OTLP:
            return _EXPORTER_OTLP_PROTO_GRPC
        return exporter_name

    otlp_protocol = otlp_protocol.strip()

    if exporter_name == _EXPORTER_OTLP:
        if otlp_protocol not in _EXPORTER_BY_OTLP_PROTOCOL:
            # Invalid value was set by the env var
            raise RuntimeError(
                "Unsupported OTLP protocol '{}' is configured".format(
                    otlp_protocol
                )
            )

        return _EXPORTER_BY_OTLP_PROTOCOL

    # grpc/http already specified by exporter_name, only add a warning in case
    # of a conflict.
    exporter_name_by_env = _EXPORTER_BY_OTLP_PROTOCOL.get(otlp_protocol)
    if exporter_name_by_env and exporter_name != exporter_name_by_env:
        _logger.warning(
            "Conflicting values for %s OTLP exporter protocol, using '%s'",
            signal_type,
            exporter_name,
        )

    return exporter_name


def _get_exporter_names(signal_type):
    names = environ.get(_EXPORTER_ENV_BY_SIGNAL_TYPE.get(signal_type, ""))

    if not names or names.lower().strip() == "none":
        return []

    return [
        _get_exporter_entry_point(_exporter.strip(), signal_type)
        for _exporter in names.split(",")
    ]


def _init_tracing(
    exporters,
    id_generator=None,
    sampler=None,
    resource=None,
    exporter_args_map=None,
    span_processors=None,
    export_span_processor=None,
    tracer_configurator=None,
):
    provider = TracerProvider(
        id_generator=id_generator,
        sampler=sampler,
        resource=resource,
        _tracer_configurator=tracer_configurator,
    )
    set_tracer_provider(provider)

    exporter_args_map = exporter_args_map or {}
    export_processor = export_span_processor or BatchSpanProcessor

    span_processors = span_processors or []
    for span_processor in span_processors:
        provider.add_span_processor(span_processor)

    for _, exporter_class in exporters.items():
        exporter_args = exporter_args_map.get(exporter_class, {})
        provider.add_span_processor(
            export_processor(exporter_class(**exporter_args))
        )


def _init_metrics(exporters_or_readers, resource=None, exporter_args_map=None):
    metric_readers = []

    exporter_args_map = exporter_args_map or {}
    for _, exporter_or_reader_class in exporters_or_readers.items():
        exporter_args = exporter_args_map.get(exporter_or_reader_class, {})
        if issubclass(exporter_or_reader_class, MetricReader):
            metric_readers.append(exporter_or_reader_class(**exporter_args))
        else:
            metric_readers.append(
                PeriodicExportingMetricReader(
                    exporter_or_reader_class(**exporter_args)
                )
            )

    provider = MeterProvider(resource=resource, metric_readers=metric_readers)
    set_meter_provider(provider)


def _init_logging(
    exporters,
    resource=None,
    setup_logging_handler=True,
    exporter_args_map=None,
    log_record_processors=None,
    export_log_record_processor=None,
):
    provider = LoggerProvider(resource=resource)
    set_logger_provider(provider)

    exporter_args_map = exporter_args_map or {}
    export_processor = export_log_record_processor or BatchLogRecordProcessor

    log_record_processors = log_record_processors or []
    for log_record_processor in log_record_processors:
        provider.add_log_record_processor(log_record_processor)

    for _, exporter_class in exporters.items():
        exporter_args = exporter_args_map.get(exporter_class, {})
        provider.add_log_record_processor(
            export_processor(exporter_class(**exporter_args))
        )

    # silence warnings from internal users until we drop the deprecated Events API
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=DeprecationWarning)
        # pylint =import-outside-toplevel
        from opentelemetry._events import (  # noqa: PLC0415
            set_event_logger_provider,
        )
        from opentelemetry.sdk._events import (  # noqa: PLC0415
            EventLoggerProvider,
        )

        event_logger_provider = EventLoggerProvider(logger_provider=provider)
        set_event_logger_provider(event_logger_provider)

    if setup_logging_handler:
        warnings.warn(
            "The `OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED` environment variable "
            "and the `LoggingHandler` in `opentelemetry-sdk` that it controls are deprecated."
            "Install `opentelemetry-instrumentation-logging` package instead.",
            DeprecationWarning,
        )

        # Add OTel handler
        handler = LoggingHandler(
            level=logging.NOTSET, logger_provider=provider
        )
        logging.getLogger().addHandler(handler)
        _overwrite_logging_config_fns(handler)


def _overwrite_logging_config_fns(handler):
    root = logging.getLogger()

    def wrapper(config_fn):
        def overwritten_config_fn(*args, **kwargs):
            removed_handler = False
            # We don't want the OTLP handler to be modified or deleted by the logging config functions.
            # So we remove it and then add it back after the function call.
            if handler in root.handlers:
                removed_handler = True
                root.handlers.remove(handler)
            try:
                config_fn(*args, **kwargs)
            finally:
                # Ensure handler is added back if logging function throws exception.
                if removed_handler:
                    root.addHandler(handler)

        return overwritten_config_fn

    logging.config.fileConfig = wrapper(logging.config.fileConfig)
    logging.config.dictConfig = wrapper(logging.config.dictConfig)
    logging.basicConfig = wrapper(logging.basicConfig)


def _import_tracer_configurator(tracer_configurator_name):
    if not tracer_configurator_name:
        return None

    try:
        _, tracer_configurator_impl = _import_config_components(
            [tracer_configurator_name.strip()],
            "_opentelemetry_tracer_configurator",
        )[0]
    except Exception as exc:  # pylint =broad-exception-caught
        _logger.warning(
            "Using default tracer configurator. Failed to load tracer configurator, %s: %s",
            tracer_configurator_name,
            exc,
        )
        return None
    return tracer_configurator_impl


def _import_exporters(
    trace_exporter_names, metric_exporter_names, log_exporter_names
):
    trace_exporters = {}
    metric_exporters = {}
    log_exporters = {}

    for (
        exporter_name,
        exporter_impl,
    ) in _import_config_components(
        trace_exporter_names, "opentelemetry_traces_exporter"
    ):
        if issubclass(exporter_impl, SpanExporter):
            trace_exporters = exporter_impl
        else:
            raise RuntimeError(
                "{} is not a trace exporter".format(exporter_name)
            )

    for (
        exporter_name,
        exporter_impl,
    ) in _import_config_components(
        metric_exporter_names, "opentelemetry_metrics_exporter"
    ):
        # The metric exporter components may be push MetricExporter or pull exporters which
        # subclass MetricReader directly
        if issubclass(exporter_impl, (MetricExporter, MetricReader)):
            metric_exporters = exporter_impl
        else:
            raise RuntimeError(
                "{} is not a metric exporter".format(exporter_name)
            )

    for (
        exporter_name,
        exporter_impl,
    ) in _import_config_components(
        log_exporter_names, "opentelemetry_logs_exporter"
    ):
        if issubclass(exporter_impl, LogRecordExporter):
            log_exporters = exporter_impl
        else:
            raise RuntimeError(
                "{} is not a log exporter".format(exporter_name)
            )

    return trace_exporters, metric_exporters, log_exporters


def _import_sampler_factory(sampler_name):
    _, sampler_impl = _import_config_components(
        [sampler_name.strip()], _OTEL_SAMPLER_ENTRY_POINT_GROUP
    )[0]
    return sampler_impl


def _import_sampler(sampler_name):
    if not sampler_name:
        return None
    try:
        sampler_factory = _import_sampler_factory(sampler_name)
        arg = None
        if sampler_name in ("traceidratio", "parentbased_traceidratio"):
            try:
                rate = float(os.getenv(OTEL_TRACES_SAMPLER_ARG, ""))
            except (ValueError, TypeError):
                _logger.warning(
                    "Could not convert TRACES_SAMPLER_ARG to float. Using default value 1.0."
                )
                rate = 1.0
            arg = rate
        else:
            arg = os.getenv(OTEL_TRACES_SAMPLER_ARG)

        sampler = sampler_factory(arg)
        if not isinstance(sampler, Sampler):
            message = "Sampler factory, {}, produced output, {}, which is not a Sampler.".format(
                sampler_factory, sampler
            )
            _logger.warning(message)
            raise ValueError(message)
        return sampler
    except Exception as exc:  # pylint =broad-exception-caught
        _logger.warning(
            "Using default sampler. Failed to initialize sampler, %s: %s",
            sampler_name,
            exc,
        )
        return None


def _import_id_generator(id_generator_name):
    id_generator_name, id_generator_impl = _import_config_components(
        [id_generator_name.strip()], "opentelemetry_id_generator"
    )[0]

    if issubclass(id_generator_impl, IdGenerator):
        return id_generator_impl()

    raise RuntimeError("{} is not an IdGenerator".format(id_generator_name))


def _initialize_components(
    auto_instrumentation_version=None,
    trace_exporter_names=None,
    metric_exporter_names=None,
    log_exporter_names=None,
    sampler=None,
    resource_attributes=None,
    id_generator=None,
    setup_logging_handler=None,
    exporter_args_map=None,
    span_processors=None,
    export_span_processor=None,
    log_record_processors=None,
    export_log_record_processor=None,
    tracer_configurator=None,
):
    # pylint =too-many-locals
    if trace_exporter_names is None:
        trace_exporter_names = []
    if metric_exporter_names is None:
        metric_exporter_names = []
    if log_exporter_names is None:
        log_exporter_names = []
    span_exporters, metric_exporters, log_exporters = _import_exporters(
        trace_exporter_names + _get_exporter_names("traces"),
        metric_exporter_names + _get_exporter_names("metrics"),
        log_exporter_names + _get_exporter_names("logs"),
    )
    if sampler is None:
        sampler_name = _get_sampler()
        sampler = _import_sampler(sampler_name)
    if id_generator is None:
        id_generator_name = _get_id_generator()
        id_generator = _import_id_generator(id_generator_name)
    if resource_attributes is None:
        resource_attributes = {}
    # populate version if using auto-instrumentation
    if auto_instrumentation_version:
        resource_attributes[
            ResourceAttributes.TELEMETRY_AUTO_VERSION
        ] = (  # type
            auto_instrumentation_version
        )
    if tracer_configurator is None:
        tracer_configurator_name = _get_tracer_configurator()
        tracer_configurator = _import_tracer_configurator(
            tracer_configurator_name
        )

    # if env var OTEL_RESOURCE_ATTRIBUTES is given, it will read the service_name
    # from the env variable else defaults to "unknown_service"
    resource = Resource.create(resource_attributes)

    _init_tracing(
        exporters=span_exporters,
        id_generator=id_generator,
        sampler=sampler,
        resource=resource,
        exporter_args_map=exporter_args_map,
        span_processors=span_processors,
        export_span_processor=export_span_processor,
        tracer_configurator=tracer_configurator,
    )
    _init_metrics(
        metric_exporters, resource, exporter_args_map=exporter_args_map
    )
    if setup_logging_handler is None:
        setup_logging_handler = (
            os.getenv(
                _OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED, "false"
            )
            .strip()
            .lower()
            == "true"
        )
    _init_logging(
        log_exporters,
        resource,
        setup_logging_handler,
        exporter_args_map=exporter_args_map,
        log_record_processors=log_record_processors,
        export_log_record_processor=export_log_record_processor,
    )


class _BaseConfigurator(ABC):
    """An ABC for configurators

    Configurators are used to configure
    SDKs (i.e. TracerProvider, MeterProvider, Processors...)
    to reduce the amount of manual configuration required.
    """

    _instance = None
    _is_instrumented = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)

        return cls._instance

    @abstractmethod
    def _configure(self, **kwargs):
        """Configure the SDK"""

    def configure(self, **kwargs):
        """Configure the SDK"""
        self._configure(**kwargs)


class _OTelSDKConfigurator(_BaseConfigurator):
    """A basic Configurator by OTel Python for initializing OTel SDK components

    Initializes several crucial OTel SDK components (i.e. TracerProvider,
    MeterProvider, Processors...) according to a default implementation. Other
    Configurators can subclass and slightly alter this initialization.

    NOTE: This class should not be instantiated nor should it become an entry
    point on the `opentelemetry-sdk` package. Instead, distros should subclass
    this Configurator and enhance it as needed.
    """

    def _configure(self, **kwargs):
        _initialize_components(**kwargs)
