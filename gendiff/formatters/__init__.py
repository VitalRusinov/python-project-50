"""Formatters module for different output formats."""

from .diff_builder import DiffNode, build_diff
from .json import format_json
from .plain import format_plain
from .stylish import format_stylish


def get_formatter(format_name: str):
    """Get formatter function by name."""
    formatters = {
        "stylish": format_stylish,
        "plain": format_plain,
        "json": format_json,
    }
    return formatters.get(format_name)


__all__ = [
    "build_diff",
    "DiffNode",
    "get_formatter",
    "format_json",
    "format_plain",
    "format_stylish",
]
