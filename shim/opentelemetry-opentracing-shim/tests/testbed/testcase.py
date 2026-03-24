from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from builtins import map
from future import standard_library
standard_library.install_aliases()
import unittest

import opentelemetry.trace as trace_api


# pylint: disable=C0103
class OpenTelemetryTestCase(unittest.TestCase):
    def assertSameTrace(self, spanA, spanB):
        return self.assertEqual(spanA.context.trace_id, spanB.context.trace_id)

    def assertNotSameTrace(self, spanA, spanB):
        return self.assertNotEqual(
            spanA.context.trace_id, spanB.context.trace_id
        )

    def assertIsChildOf(self, spanA, spanB):
        # spanA is child of spanB
        self.assertIsNotNone(spanA.parent)

        ctxA = spanA.parent
        if not isinstance(ctxA, trace_api.SpanContext):
            ctxA = spanA.parent.context

        ctxB = spanB
        if not isinstance(ctxB, trace_api.SpanContext):
            ctxB = spanB.context

        return self.assertEqual(ctxA.span_id, ctxB.span_id)

    def assertIsNotChildOf(self, spanA, spanB):
        # spanA is NOT child of spanB
        if spanA.parent is None:
            return

        ctxA = spanA.parent
        if not isinstance(ctxA, trace_api.SpanContext):
            ctxA = spanA.parent.context

        ctxB = spanB
        if not isinstance(ctxB, trace_api.SpanContext):
            ctxB = spanB.context

        self.assertNotEqual(ctxA.span_id, ctxB.span_id)

    def assertNamesEqual(self, spans, names):
        self.assertEqual(list(map(lambda x: x.name, spans)), names)
