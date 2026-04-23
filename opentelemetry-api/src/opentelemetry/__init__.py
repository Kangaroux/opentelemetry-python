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

"""OpenTelemetry namespace package."""

# Python 2.7 compatibility -- must run before any other submodule imports.
import opentelemetry._compat  # noqa: F401

try:
    __import__("pkg_resources").declare_namespace(__name__)
except ImportError:
    pass

# Always extend __path__ via pkgutil so that PYTHONPATH-based installs
# (where pkg_resources.declare_namespace cannot discover peer directories)
# merge the namespace correctly.
from pkgutil import extend_path

__path__ = extend_path(__path__, __name__)
