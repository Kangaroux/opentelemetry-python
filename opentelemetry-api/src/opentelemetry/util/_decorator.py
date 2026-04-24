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

import contextlib

# On Python 2.7 there is no async, so the agnostic context manager is just
# the standard contextlib.contextmanager.  The original Python 3 version
# subclassed contextlib._GeneratorContextManager with Generic[R] and handled
# coroutine functions -- none of which is available or needed on 2.7.
_agnosticcontextmanager = contextlib.contextmanager
