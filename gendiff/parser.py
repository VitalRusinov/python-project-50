"""File parsing module."""

import json
import os
from typing import Any, Callable
import yaml


def read_file(file_path: str) -> str:
    """Read file content."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def parse_json(content: str) -> Any:
    """Parse JSON content."""
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON format: {e}")


def parse_yaml(content: str) -> Any:
    """Parse YAML content."""
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise ValueError(f"Invalid YAML format: {e}")


def create_parser(extension: str) -> Callable[[str], Any]:
    """Factory for parsers."""
    parsers = {
        ".json": parse_json,
        ".yaml": parse_yaml,
        ".yml": parse_yaml,
    }

    if extension not in parsers:
        raise ValueError(f"Unsupported file format: {extension}")

    return parsers[extension]


def get_data(file_path: str) -> Any:
    """Get parsed data from file using parser factory."""
    content = read_file(file_path)
    _, extension = os.path.splitext(file_path)
    parser = create_parser(extension.lower())
    return parser(content)