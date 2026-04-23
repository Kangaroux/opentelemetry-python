# OpenTelemetry Python (Python 2.7 Refactor)
[![Slack](https://img.shields.io/badge/slack-@cncf/otel/python-brightgreen.svg?logo=slack)](https://cloud-native.slack.com/archives/C01PD4HUVBL)
[![Minimum Python Version](https://img.shields.io/badge/python-2.7+-blue.svg)](https://www.python.org/downloads/)

> **Note:** This is a fork being refactored for Python 2.7 compatibility. The
> source code has been mechanically transformed using `refactor_to_py27.py` to
> remove Python 3-only syntax (type hints, f-strings, async/await, dataclasses,
> walrus operators, etc.). See [Refactoring Status](#refactoring-status) below.

## Refactoring Status

This branch targets **Python 2.7** syntax compatibility. The refactoring script
(`refactor_to_py27.py`) applies the following transformations:

- Remove `from __future__ import annotations`
- Replace f-strings with `.format()` calls
- Remove type hints from function signatures and class attributes
- Remove `@dataclass` decorators (replaced with manual `__init__`/`__eq__`)
- Remove `async`/`await` keywords
- Replace `raise ... from ...` with `raise ...`
- Replace `...` (ellipsis) with `pass`
- Remove `TypeAlias` usage
- Replace `X | Y` union syntax

### Verification

- **Python 2.7 compilation:** All source files compile with `python:2.7-alpine`
- **Python 3.12 tests:** API (259 passed), SDK (708 passed), B3 propagator (52),
  Jaeger propagator (18), OTLP exporter (17)
- 2 async-specific API tests are expected failures (async/await removed for Py2.7)

### How to verify

```sh
# Compile check with Python 2.7
docker run --rm -v "$(pwd):/work" -w /work python:2.7-alpine python -m py_compile <file.py>

# Run tests with the test image
docker build -f Dockerfile.test -t otel-py-test .
docker run --rm -v "$(pwd):/work" -w /work otel-py-test pytest opentelemetry-api/tests
docker run --rm -v "$(pwd):/work" -w /work otel-py-test pytest opentelemetry-sdk/tests
```

## Project Status

See the [OpenTelemetry Instrumentation for Python](https://opentelemetry.io/docs/instrumentation/python/#status-and-releases).

| Signal  | Status       | Project |
| ------- | ------------ | ------- |
| Traces  | Stable       | N/A     |
| Metrics | Stable       | N/A     |
| Logs    | Development* | N/A     |

Project versioning information and stability guarantees can be found [here](./rationale.md#versioning-and-releasing).

***Breaking Changes**

> [!IMPORTANT]
> We are working on stabilizing the Log signal which would require making deprecations and breaking changes. We will try to reduce the releases that may require an update to your code, especially for instrumentations or for SDK developers.

## Getting started

You can find the getting started guide for OpenTelemetry Python [here](https://opentelemetry.io/docs/instrumentation/python/getting-started/).

If you are looking for **examples** on how to use the OpenTelemetry API to
instrument your code manually, or how to set up the OpenTelemetry
Python SDK, see https://opentelemetry.io/docs/instrumentation/python/manual/.

## Python Version Support

This fork targets Python 2.7 syntax compatibility. Source files are verified to
compile with `python:2.7-alpine` and tests are run with Python 3.12.


## Documentation

The online documentation is available at https://opentelemetry-python.readthedocs.io/.
To access the latest version of the documentation, see
https://opentelemetry-python.readthedocs.io/en/latest/.

## Install

This repository includes multiple installable packages. The `opentelemetry-api`
package includes abstract classes and no-op implementations that comprise the OpenTelemetry API following the
[OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification).
The `opentelemetry-sdk` package is the reference implementation of the API.

Libraries that produce telemetry data should only depend on `opentelemetry-api`,
and defer the choice of the SDK to the application developer. Applications may
depend on `opentelemetry-sdk` or another package that implements the API.

The API and SDK packages are available on the Python Package Index (PyPI). You can install them via `pip` with the following commands:

```sh
pip install opentelemetry-api
pip install opentelemetry-sdk
```

The
[`exporter/`](https://github.com/open-telemetry/opentelemetry-python/tree/main/exporter)
directory includes OpenTelemetry exporter packages. You can install the packages separately with the following command:

```sh
pip install opentelemetry-exporter-{exporter}
```

The
[`propagator/`](https://github.com/open-telemetry/opentelemetry-python/tree/main/propagator)
directory includes OpenTelemetry propagator packages. You can install the packages separately with the following command:

```sh
pip install opentelemetry-propagator-{propagator}
```

To install the development versions of these packages instead, clone or fork
this repository and perform an [editable
install](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs):

```sh
pip install -e ./opentelemetry-api -e ./opentelemetry-sdk -e ./opentelemetry-semantic-conventions
```

For additional exporter and instrumentation packages, see the
[`opentelemetry-python-contrib`](https://github.com/open-telemetry/opentelemetry-python-contrib) repository.

## Contributing

For information about contributing to OpenTelemetry Python, see [CONTRIBUTING.md](CONTRIBUTING.md).

We meet weekly on Thursdays at 9AM PST. The meeting is subject to change depending on contributors' availability. Check the [OpenTelemetry community calendar](https://calendar.google.com/calendar/embed?src=c_2bf73e3b6b530da4babd444e72b76a6ad893a5c3f43cf40467abc7a9a897f977%40group.calendar.google.com) for specific dates and Zoom meeting links.

Meeting notes are available as a public [Google doc](https://docs.google.com/document/d/18w8zOBm_mbety0OqlPwxc7dvnfu641EgmrO4AdJef0U/edit?tab=t.0).

### Maintainers

- [Aaron Abbott](https://github.com/aabmass), Google
- [Leighton Chen](https://github.com/lzchen), Microsoft
- [Riccardo Magliocchetti](https://github.com/xrmx), Elastic

For more information about the maintainer role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#maintainer).

### Approvers

- [Dylan Russell](https://github.com/dylanrussell), Google
- [Emídio Neto](https://github.com/emdneto), Independent
- [Héctor Hernández](https://github.com/hectorhdzg), Microsoft
- [Jeremy Voss](https://github.com/jeremydvoss), Microsoft
- [Liudmila Molkova](https://github.com/lmolkova), Grafana Labs
- [Lukas Hering](https://github.com/herin049), Oracle
- [Owais Lone](https://github.com/owais), Splunk
- [Pablo Collins](https://github.com/pmcollins), Splunk
- [Shalev Roda](https://github.com/shalevr), Cisco
- [Srikanth Chekuri](https://github.com/srikanthccv), signoz.io
- [Tammy Baylis](https://github.com/tammy-baylis-swi), SolarWinds

For more information about the approver role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#approver).

### Emeritus Maintainers

- [Alex Boten](https://github.com/codeboten)
- [Chris Kleinknecht](https://github.com/c24t)
- [Diego Hurtado](https://github.com/ocelotl)
- [Owais Lone](https://github.com/owais)
- [Reiley Yang](https://github.com/reyang)
- [Srikanth Chekuri](https://github.com/srikanthccv)
- [Yusuke Tsutsumi](https://github.com/toumorokoshi)

For more information about the emeritus role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#emeritus-maintainerapprovertriager).

### Emeritus Approvers

- [Ashutosh Goel](https://github.com/ashu658)
- [Carlos Alberto Cortez](https://github.com/carlosalberto)
- [Christian Neumüller](https://github.com/Oberon00)
- [Mauricio Vásquez](https://github.com/mauriciovasquezbernal)
- [Nathaniel Ruiz Nowell](https://github.com/NathanielRN)
- [Nikolay Sokolik](https://github.com/oxeye-nikolay)
- [Sanket Mehta](https://github.com/sanketmehta28)
- [Tahir H. Butt](https://github.com/majorgreys)

For more information about the emeritus role, see the [community repository](https://github.com/open-telemetry/community/blob/main/guides/contributor/membership.md#emeritus-maintainerapprovertriager).

### Thanks to all of our contributors!

<a href="https://github.com/open-telemetry/opentelemetry-python/graphs/contributors">
  <img alt="Repo contributors" src="https://contrib.rocks/image?repo=open-telemetry/opentelemetry-python" />
</a>
