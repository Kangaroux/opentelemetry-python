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

from future import standard_library
standard_library.install_aliases()
import unittest

from opentelemetry.exporter.zipkin import json
from opentelemetry.exporter.zipkin.proto import http


class TestZipkinExporter(unittest.TestCase):
    def test_constructors(self):
        try:
            json.ZipkinExporter()
            http.ZipkinExporter()
        except Exception as exc:  # pylint =broad-exception-caught
            self.assertIsNone(exc)
