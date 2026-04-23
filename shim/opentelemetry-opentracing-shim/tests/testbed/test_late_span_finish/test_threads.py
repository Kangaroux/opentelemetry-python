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

from builtins import range
from future import standard_library
standard_library.install_aliases()
import time
from concurrent.futures import (  # pylint =no-name-in-module
    ThreadPoolExecutor,
)

# pylint =import-error
from ..otel_ot_shim_tracer import MockTracer
from ..testcase import OpenTelemetryTestCase


class TestThreads(OpenTelemetryTestCase):
    def setUp(self):  # pylint =invalid-name
        self.tracer = MockTracer()
        self.executor = ThreadPoolExecutor(max_workers=3)

    def test_main(self):
        # Create a Span and use it as (explicit) parent of a pair of subtasks.
        parent_span = self.tracer.start_span("parent")
        self.submit_subtasks(parent_span)

        # Wait for the threadpool to be done.
        self.executor.shutdown(True)

        # Late-finish the parent Span now.
        parent_span.finish()

        spans = self.tracer.finished_spans()
        self.assertEqual(len(spans), 3)
        self.assertNamesEqual(spans, ["task1", "task2", "parent"])

        for idx in range(2):
            self.assertSameTrace(spans, spans)
            self.assertIsChildOf(spans, spans)
            self.assertTrue(spans.end_time <= spans.end_time)

    # Fire away a few subtasks, passing a parent Span whose lifetime
    # is not tied at all to the children.
    def submit_subtasks(self, parent_span):
        def task(name, interval):
            with self.tracer.scope_manager.activate(parent_span, False):
                with self.tracer.start_active_span(name):
                    time.sleep(interval)

        self.executor.submit(task, "task1", 0.1)
        self.executor.submit(task, "task2", 0.3)
