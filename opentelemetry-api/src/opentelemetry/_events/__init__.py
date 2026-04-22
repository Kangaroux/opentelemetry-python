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

from abc import ABC, abstractmethod
from logging import getLogger
from os import environ
from typing import Optional, cast

from typing_extensions import deprecated

from opentelemetry._logs import LogRecord
from opentelemetry._logs.severity import SeverityNumber
from opentelemetry.environment_variables import (
    _OTEL_PYTHON_EVENT_LOGGER_PROVIDER,
)
from opentelemetry.trace.span import TraceFlags
from opentelemetry.util._once import Once
from opentelemetry.util._providers import _load_provider
from opentelemetry.util.types import AnyValue, _ExtendedAttributes

_logger = getLogger(__name__)


@deprecated(
    "You should use `LogRecord` with the `event_name` field set instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class Event(LogRecord):
    def __init__(
        self,
        name,
        timestamp = None,
        trace_id = None,
        span_id = None,
        trace_flags = None,
        body = None,
        severity_number = None,
        attributes = None
    ):
        attributes = attributes or {}
        event_attributes = attributes
        event_attributes.update({"event.name": name,})
        super().__init__(
            timestamp=timestamp,
            trace_id=trace_id,
            span_id=span_id,
            trace_flags=trace_flags,
            body=body,
            severity_number=severity_number,
            attributes=event_attributes,
        )
        self.name = name


@deprecated(
    "You should use `Logger` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class EventLogger(ABC):
    def __init__(
        self,
        name,
        version = None,
        schema_url = None,
        attributes = None
    ):
        self._name = name
        self._version = version
        self._schema_url = schema_url
        self._attributes = attributes

    @abstractmethod
    def emit(self, event):
        """Emits a :class:`Event` representing an event."""


@deprecated(
    "You should use `NoOpLogger` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class NoOpEventLogger(EventLogger):
    def emit(self, event):
        pass


@deprecated(
    "You should use `ProxyLogger` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class ProxyEventLogger(EventLogger):
    def __init__(
        self,
        name,
        version = None,
        schema_url = None,
        attributes = None
    ):
        super().__init__(
            name=name,
            version=version,
            schema_url=schema_url,
            attributes=attributes,
        )
        self._real_event_logger = None
        self._noop_event_logger = NoOpEventLogger(name)

    @property
    def _event_logger(self):
        if self._real_event_logger:
            return self._real_event_logger

        if _EVENT_LOGGER_PROVIDER:
            self._real_event_logger = _EVENT_LOGGER_PROVIDER.get_event_logger(
                self._name,
                self._version,
                self._schema_url,
                self._attributes,
            )
            return self._real_event_logger
        return self._noop_event_logger

    def emit(self, event):
        self._event_logger.emit(event)


class EventLoggerProvider(ABC):
    @abstractmethod
    def get_event_logger(
        self,
        name,
        version=None,
        schema_url=None,
        attributes=None
    ):
        """Returns an EventLoggerProvider for use."""


@deprecated(
    "You should use `NoOpLoggerProvider` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class NoOpEventLoggerProvider(EventLoggerProvider):
    def get_event_logger(
        self,
        name,
        version = None,
        schema_url = None,
        attributes = None
    ):
        return NoOpEventLogger(
            name, version=version, schema_url=schema_url, attributes=attributes
        )


@deprecated(
    "You should use `ProxyLoggerProvider` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
class ProxyEventLoggerProvider(EventLoggerProvider):
    def get_event_logger(
        self,
        name,
        version = None,
        schema_url = None,
        attributes = None
    ):
        if _EVENT_LOGGER_PROVIDER:
            return _EVENT_LOGGER_PROVIDER.get_event_logger(
                name,
                version=version,
                schema_url=schema_url,
                attributes=attributes,
            )
        return ProxyEventLogger(
            name,
            version=version,
            schema_url=schema_url,
            attributes=attributes,
        )


_EVENT_LOGGER_PROVIDER_SET_ONCE = Once()
_EVENT_LOGGER_PROVIDER = None
_PROXY_EVENT_LOGGER_PROVIDER = ProxyEventLoggerProvider()


@deprecated(
    "You should use `get_logger_provider` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
def get_event_logger_provider():
    global _EVENT_LOGGER_PROVIDER  # pylint =global-variable-not-assigned
    if _EVENT_LOGGER_PROVIDER is None:
        if _OTEL_PYTHON_EVENT_LOGGER_PROVIDER not in environ:
            return _PROXY_EVENT_LOGGER_PROVIDER

        event_logger_provider = _load_provider(  # type: ignore
            _OTEL_PYTHON_EVENT_LOGGER_PROVIDER, "event_logger_provider"
        )

        _set_event_logger_provider(event_logger_provider, log=False)

    return cast("EventLoggerProvider", _EVENT_LOGGER_PROVIDER)


def _set_event_logger_provider(
    event_logger_provider, log
):
    def set_elp():
        global _EVENT_LOGGER_PROVIDER  # pylint =global-statement
        _EVENT_LOGGER_PROVIDER = event_logger_provider

    did_set = _EVENT_LOGGER_PROVIDER_SET_ONCE.do_once(set_elp)

    if log and not did_set:
        _logger.warning(
            "Overriding of current EventLoggerProvider is not allowed"
        )


@deprecated(
    "You should use `set_logger_provider` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
def set_event_logger_provider(
    event_logger_provider
):
    _set_event_logger_provider(event_logger_provider, log=True)


@deprecated(
    "You should use `get_logger` instead. "
    "Deprecated since version 1.39.0 and will be removed in a future release."
)
def get_event_logger(
    name,
    version = None,
    schema_url = None,
    attributes = None,
    event_logger_provider = None
):
    if event_logger_provider is None:
        event_logger_provider = get_event_logger_provider()
    return event_logger_provider.get_event_logger(
        name,
        version,
        schema_url,
        attributes,
    )
