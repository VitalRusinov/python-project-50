"""Main facade function for generating differences."""

from gendiff.parser import get_data
from gendiff.diff_builder import build_diff
from gendiff.formatters import get_formatter


def generate_diff(file_path1, file_path2, format_name='stylish'):
    """
    Generate difference between two files.

    Args:
        file_path1: path to first file
        file_path2: path to second file
        format_name: output format (default: 'stylish')

    Returns:
        str: formatted difference

    Raises:
        FileNotFoundError: if file doesn't exist
        ValueError: if file format is not supported
    """
    # Get data from files
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    # Build difference tree
    diff_tree = build_diff(data1, data2)

    # Format output
    formatter = get_formatter(format_name)
    if formatter is None:
        raise ValueError(f"Unknown format: {format_name}")

    return formatter(diff_tree)