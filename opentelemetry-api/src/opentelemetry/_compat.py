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

"""Python 2.7 compatibility patches for OpenTelemetry.

This module is imported at the top of opentelemetry/__init__.py, before any
other submodules load.  It monkey-patches stdlib and third-party modules so
that code written against Python 3.x APIs works on Python 2.7.

Patches applied:
  1. abc.ABC        -- synthesised from ABCMeta   (added in Python 3.4)
  2. collections.abc -- alias to collections       (split out in Python 3.3)
  3. contextvars    -- thread-local backport        (added in Python 3.7)
  4. typing_extensions -- stubs for deprecated, final, override, etc.
"""

import abc
import collections
import sys
import threading
import types


# ---------------------------------------------------------------------------
# 1. abc.ABC
# ---------------------------------------------------------------------------
# abc.ABC was added in Python 3.4.  In 2.7 we create it from ABCMeta so that
# ``class Foo(ABC):`` and ``class Bar(abc.ABC):`` both work unchanged.
if not hasattr(abc, 'ABC'):
    abc.ABC = abc.ABCMeta('ABC', (object,), {'__slots__': ()})


# ---------------------------------------------------------------------------
# 2. collections.abc
# ---------------------------------------------------------------------------
# In Python 2.7 MutableMapping, Sequence, etc. live directly in collections.
# Python 3.3+ moved them to collections.abc.  Injecting an alias into
# sys.modules lets ``from collections.abc import X`` resolve correctly.
try:
    import collections.abc  # noqa: F401
except ImportError:
    sys.modules['collections.abc'] = collections
    collections.abc = collections


# ---------------------------------------------------------------------------
# 3. contextvars (thread-local backport)
# ---------------------------------------------------------------------------
# contextvars was added in Python 3.7.  The OTel context system depends on
# ContextVar and Token.  This backport uses threading.local which is correct
# for synchronous, thread-per-request workloads (async is not available on
# Python 2.7 anyway).
try:
    import contextvars  # noqa: F401
except ImportError:
    _MISSING = object()

    class Token(object):
        """Opaque token returned by ContextVar.set()."""
        MISSING = _MISSING

        def __init__(self, var, old_value):
            self.var = var
            self.old_value = old_value
            self._used = False

    class ContextVar(object):
        """Thread-local backport of contextvars.ContextVar."""

        def __init__(self, name, **kwargs):
            self.name = name
            self._default = kwargs.get('default', _MISSING)
            self._local = threading.local()

        def get(self, default=_MISSING):
            try:
                return self._local.value
            except AttributeError:
                if default is not _MISSING:
                    return default
                if self._default is not _MISSING:
                    return self._default
                raise LookupError(self.name)

        def set(self, value):
            try:
                old = self._local.value
            except AttributeError:
                old = _MISSING
            token = Token(self, old)
            self._local.value = value
            return token

        def reset(self, token):
            if token._used:
                raise RuntimeError("Token already used")
            if token.var is not self:
                raise ValueError("Token from different ContextVar")
            token._used = True
            if token.old_value is _MISSING:
                try:
                    del self._local.value
                except AttributeError:
                    pass
            else:
                self._local.value = token.old_value

    def copy_context():
        return {}

    _ctx_mod = types.ModuleType('contextvars')
    _ctx_mod.ContextVar = ContextVar
    _ctx_mod.Token = Token
    _ctx_mod.copy_context = copy_context
    sys.modules['contextvars'] = _ctx_mod


# ---------------------------------------------------------------------------
# 4. typing_extensions stubs
# ---------------------------------------------------------------------------
# The latest Py2.7-compatible typing_extensions is 3.7.4.3 which predates
# symbols like ``deprecated``, ``override``, ``Self``, ``TypeAlias``, etc.
# Provide no-op stubs so that ``from typing_extensions import X`` works.
try:
    import typing_extensions as _te
except ImportError:
    _te = types.ModuleType('typing_extensions')
    sys.modules['typing_extensions'] = _te

if not hasattr(_te, 'deprecated'):
    def _deprecated(__msg, **kwargs):
        """No-op stub for typing_extensions.deprecated."""
        def _decorator(__arg):
            return __arg
        return _decorator
    _te.deprecated = _deprecated

if not hasattr(_te, 'override'):
    _te.override = lambda f: f

if not hasattr(_te, 'final'):
    _te.final = lambda f: f

if not hasattr(_te, 'Final'):
    _te.Final = None

if not hasattr(_te, 'TypeAlias'):
    _te.TypeAlias = None

if not hasattr(_te, 'Self'):
    _te.Self = None

if not hasattr(_te, 'Protocol'):
    _te.Protocol = type('Protocol', (object,), {})

if not hasattr(_te, 'Literal'):
    _te.Literal = None

if not hasattr(_te, 'ParamSpec'):
    class _ParamSpec(object):
        def __init__(self, name):
            self.name = name
            self.args = self
            self.kwargs = self
    _te.ParamSpec = _ParamSpec
