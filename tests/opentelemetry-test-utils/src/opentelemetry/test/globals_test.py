from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
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

from builtins import super
from future import standard_library
standard_library.install_aliases()
import unittest

from opentelemetry import trace as trace_api
from opentelemetry._logs import _internal as logging_api
from opentelemetry.metrics import _internal as metrics_api
from opentelemetry.metrics._internal import _ProxyMeterProvider
from opentelemetry.util._once import Once


# pylint =protected-access
def reset_trace_globals():
    """WARNING: only use this for tests."""
    trace_api._TRACER_PROVIDER_SET_ONCE = Once()
    trace_api._TRACER_PROVIDER = None
    trace_api._PROXY_TRACER_PROVIDER = trace_api.ProxyTracerProvider()


# pylint =protected-access
def reset_metrics_globals():
    """WARNING: only use this for tests."""
    metrics_api._METER_PROVIDER_SET_ONCE = Once()  # type
    metrics_api._METER_PROVIDER = None  # type
    metrics_api._PROXY_METER_PROVIDER = _ProxyMeterProvider()  # type


# pylint =protected-access
def reset_logging_globals():
    """WARNING: only use this for tests."""
    logging_api._LOGGER_PROVIDER_SET_ONCE = Once()  # type
    logging_api._LOGGER_PROVIDER = None  # type
    logging_api._PROXY_LOGGER_PROVIDER = logging_api.ProxyLoggerProvider()  # type


# pylint =protected-access
def reset_event_globals():
    """WARNING: only use this for tests."""
    from opentelemetry import (  # pylint =import-outside-toplevel # noqa: PLC0415
        _events as events_api,
    )

    events_api._EVENT_LOGGER_PROVIDER_SET_ONCE = Once()  # type
    events_api._EVENT_LOGGER_PROVIDER = None  # type
    events_api._PROXY_EVENT_LOGGER_PROVIDER = (
        events_api.ProxyEventLoggerProvider()
    )  # type: ignore


class TraceGlobalsTest(unittest.TestCase):
    """Resets trace API globals in setUp/tearDown

    Use as a base class or mixin for your test that modifies trace API globals.
    """

    def setUp(self):
        super().setUp()
        reset_trace_globals()

    def tearDown(self):
        super().tearDown()
        reset_trace_globals()


class MetricsGlobalsTest(unittest.TestCase):
    """Resets metrics API globals in setUp/tearDown

    Use as a base class or mixin for your test that modifies metrics API globals.
    """

    def setUp(self):
        super().setUp()
        reset_metrics_globals()

    def tearDown(self):
        super().tearDown()
        reset_metrics_globals()


class LoggingGlobalsTest(unittest.TestCase):
    """Resets logging API globals in setUp/tearDown

    Use as a base class or mixin for your test that modifies logging API globals.
    """

    def setUp(self):
        super().setUp()
        reset_logging_globals()

    def tearDown(self):
        super().tearDown()
        reset_logging_globals()


class EventsGlobalsTest(unittest.TestCase):
    """Resets logging API globals in setUp/tearDown

    Use as a base class or mixin for your test that modifies logging API globals.
    """

    def setUp(self):
        super().setUp()
        reset_event_globals()

    def tearDown(self):
        super().tearDown()
        reset_event_globals()
