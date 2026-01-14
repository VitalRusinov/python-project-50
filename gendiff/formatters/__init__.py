"""Formatters module for different output formats."""

from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def get_formatter(format_name: str):
    """Get formatter function by name."""
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    return formatters.get(format_name)
