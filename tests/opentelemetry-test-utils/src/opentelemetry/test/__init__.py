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

# type: ignore

from builtins import super
from future import standard_library
standard_library.install_aliases()
from builtins import object
from traceback import format_tb
from unittest import TestCase


class _AssertNotRaisesMixin(object):
    class _AssertNotRaises(object):
        def __init__(self, test_case):
            self._test_case = test_case

        def __enter__(self):
            return self

        def __exit__(self, type_, value, tb):  # pylint =invalid-name
            if value is not None and type_ in self._exception_types:
                self._test_case.fail(
                    "Unexpected exception was raised:\n{}".format(
                        "\n".join(format_tb(tb))
                    )
                )

            return True

        def __call__(self, exception, *exceptions):
            # pylint =attribute-defined-outside-init
            self._exception_types = (exception,) + exceptions
            return self

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # pylint =invalid-name
        self.assertNotRaises = self._AssertNotRaises(self)


class TestCase(_AssertNotRaisesMixin, TestCase):  # pylint =function-redefined
    pass
