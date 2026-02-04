"""Scripts module for gendiff."""

from gendiff.scripts.cli import parse_args
from gendiff.scripts.generate_diff import generate_diff

__all__ = ["generate_diff", "parse_args"]
