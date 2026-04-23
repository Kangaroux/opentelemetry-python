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



try:
    from functools import cache
except ImportError:
    # Python 3.7, 3.8 compatibility
    try:
        from functools import lru_cache

        def cache(func):
            return lru_cache()(func)
    except ImportError:
        # Python 2.7: no lru_cache either; simple memoisation
        def cache(func):
            _sentinel = object()
            _cache = [_sentinel]
            def wrapper():
                if _cache[0] is _sentinel:
                    _cache[0] = func()
                return _cache[0]
            return wrapper


# Try importlib_metadata (backport), then importlib.metadata (stdlib 3.8+),
# then fall back to stubs for Python 2.7 / environments without packages
# installed via pip.
_has_metadata = False
try:
    from importlib_metadata import (  # type: ignore
        Distribution,
        EntryPoint,
        EntryPoints,
        PackageNotFoundError,
        distributions,
        requires,
        version,
    )
    from importlib_metadata import (
        entry_points as original_entry_points,
    )
    _has_metadata = True
except ImportError:
    try:
        from importlib.metadata import (  # type: ignore
            Distribution,
            EntryPoint,
            EntryPoints,
            PackageNotFoundError,
            distributions,
            requires,
            version,
        )
        from importlib.metadata import (
            entry_points as original_entry_points,
        )
        _has_metadata = True
    except (ImportError, AttributeError):
        pass

if _has_metadata:
    @cache
    def _original_entry_points_cached():
        return original_entry_points()

    def entry_points(**params):
        """Replacement for importlib_metadata.entry_points that caches getting all the entry points.

        That part can be very slow, and OTel uses this function many times."""
        return _original_entry_points_cached().select(**params)
else:
    # Python 2.7 or missing importlib_metadata: provide stubs so that
    # callers can import without error.  Entry-point discovery will
    # always return empty results; call sites must have their own
    # fallback (e.g. direct imports).
    class EntryPoint(object):  # type: ignore
        pass

    class EntryPoints(list):  # type: ignore
        def select(self, **kwargs):
            return EntryPoints()

    class Distribution(object):  # type: ignore
        pass

    class PackageNotFoundError(Exception):  # type: ignore
        pass

    def distributions():
        return []

    def requires(*args, **kwargs):
        return []

    def version(name):
        return "0.0.dev0"

    def entry_points(**params):
        return EntryPoints()


__all__ = [
    "entry_points",
    "version",
    "EntryPoint",
    "EntryPoints",
    "requires",
    "Distribution",
    "distributions",
    "PackageNotFoundError",
]
