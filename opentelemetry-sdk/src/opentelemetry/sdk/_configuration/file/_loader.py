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

"""Configuration file loading and parsing."""

import json
import logging
from pathlib import Path
from typing import Any, Dict, List

try:
    from importlib.resources import files as importlib_files
except ImportError:
    # Python 3.7, use backport
    import importlib_resources

    importlib_files = importlib_resources.files

from opentelemetry.sdk._configuration.file._env_substitution import (
    substitute_env_vars,
)
from opentelemetry.sdk._configuration.models import OpenTelemetryConfiguration

try:
    import yaml
except ImportError as exc:
    raise ImportError(
        "File configuration requires pyyaml. "
        "Install with: pip install opentelemetry-sdk[file-configuration]"
    )

try:
    import jsonschema
except ImportError as exc:
    raise ImportError(
        "File configuration requires jsonschema. "
        "Install with: pip install opentelemetry-sdk[file-configuration]"
    )

_schema_cache = []


def _get_schema():
    if not _schema_cache:
        schema_path = (
            importlib_files("opentelemetry.sdk._configuration") / "schema.json"
        )
        _schema_cache.append(
            json.loads(schema_path.read_text(encoding="utf-8"))
        )
    return _schema_cache[0]


_logger = logging.getLogger(__name__)


class ConfigurationError(Exception):
    """Raised when configuration file loading, parsing, or validation fails.

    This includes errors from:
    - File not found or inaccessible
    - Invalid YAML/JSON syntax
    - Schema validation failures
    - Environment variable substitution errors
    """


def load_config_file(file_path):
    """Load and parse an OpenTelemetry configuration file.

    Supports YAML and JSON formats. Performs environment variable substitution
    before parsing.

    Args:
        file_path: Path to the configuration file (.yaml, .yml, or .json).

    Returns:
        Parsed OpenTelemetryConfiguration object.

    Raises:
        ConfigurationError: If file cannot be read, parsed, or validated.
        EnvSubstitutionError: If required environment variable is missing.

    Examples:
        >>> config = load_config_file("otel-config.yaml")
        >>> print(config.tracer_provider)
    """
    path = Path(file_path)

    if not path.exists():
        _logger.error("Configuration file not found: %s", file_path)
        raise ConfigurationError(
            "Configuration file not found: {}".format(file_path)
        )

    if not path.is_file():
        _logger.error("Configuration path is not a file: %s", file_path)
        raise ConfigurationError(
            "Configuration path is not a file: {}".format(file_path)
        )

    try:
        with open(path, encoding="utf-8") as config_file:
            content = config_file.read()
    except (OSError, IOError) as exc:
        _logger.exception("Failed to read configuration file: %s", file_path)
        raise ConfigurationError(
            "Failed to read configuration file: {}".format(file_path)
        )

    # Perform environment variable substitution
    try:
        content = substitute_env_vars(content)
    except Exception as exc:
        raise ConfigurationError(
            "Environment variable substitution failed: {}".format(exc)
        )

    # Parse based on file extension
    suffix = path.suffix.lower()
    try:
        if suffix in (".yaml", ".yml"):
            data = yaml.safe_load(content)
        elif suffix == ".json":
            data = json.loads(content)
        else:
            _logger.error("Unsupported file format: %s", suffix)
            raise ConfigurationError(
                "Unsupported file format: {}. Use .yaml, .yml, or .json".format(
                    suffix
                )
            )
    except yaml.YAMLError as exc:
        _logger.exception("Failed to parse YAML from %s", file_path)
        raise ConfigurationError("Failed to parse YAML: {}".format(exc))
    except json.JSONDecodeError as exc:
        _logger.exception("Failed to parse JSON from %s", file_path)
        raise ConfigurationError("Failed to parse JSON: {}".format(exc))

    if data is None:
        _logger.error("Configuration file is empty: %s", file_path)
        raise ConfigurationError("Configuration file is empty")

    if not isinstance(data, dict):
        _logger.error(
            "Configuration must be a mapping/object, got %s",
            type(data).__name__,
        )
        raise ConfigurationError(
            "Configuration must be a mapping/object, got {}".format(
                type(data).__name__
            )
        )

    _validate_schema(data)

    # Convert to OpenTelemetryConfiguration model
    try:
        config = _dict_to_model(data)
    except Exception as exc:
        _logger.exception(
            "Failed to validate configuration from %s", file_path
        )
        raise ConfigurationError(
            "Failed to validate configuration: {}".format(exc)
        )

    return config


def _validate_schema(data):
    """Validate configuration dict against the OTel configuration JSON schema.

    Raises:
        ConfigurationError: If the data does not conform to the schema.
    """
    try:
        jsonschema.validate(
            instance=data,
            schema=_get_schema(),
            cls=jsonschema.Draft202012Validator,
        )
    except jsonschema.ValidationError as exc:
        raise ConfigurationError(
            "Configuration does not match schema: {} ".format(exc.message)
            + "(at {})".format(" -> ".join(str(p) for p in exc.absolute_path))
            if exc.absolute_path
            else "Configuration does not match schema: {}".format(exc.message)
        )
    except jsonschema.SchemaError as exc:
        raise ConfigurationError(
            "Invalid configuration schema: {}".format(exc.message)
        )


def _dict_to_model(data):
    """Convert dictionary to OpenTelemetryConfiguration model.

    Uses the generated dataclass from models.py. This provides basic
    validation through dataclass field types.

    Args:
        data: Parsed configuration dictionary.

    Returns:
        OpenTelemetryConfiguration instance.

    Raises:
        TypeError: If data doesn't match expected structure.
        ValueError: If values are invalid.
    """
    # Construct the top-level model from the validated dict. Nested fields
    # are stored as dicts rather than their dataclass types; factory functions
    # in later PRs will handle the full recursive conversion when building
    # SDK objects.
    try:
        config = OpenTelemetryConfiguration(**data)
        return config
    except TypeError as exc:
        # Provide more helpful error message
        raise TypeError(
            "Configuration structure is invalid. "
            "Check that all required fields are present and correctly typed: {}".format(
                exc
            )
        )
