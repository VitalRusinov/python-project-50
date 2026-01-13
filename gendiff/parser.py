"""File parsing module."""

import json
import os


def read_file(file_path):
    """Read file content."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r") as f:
        return f.read()


def parse_content(content, extension):
    """Parse content based on file extension."""
    if extension == ".json":
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {e}")

    raise ValueError(f"Unsupported file format: {extension}")


def get_data(file_path):
    """Get parsed data from file."""
    content = read_file(file_path)
    _, extension = os.path.splitext(file_path)
    return parse_content(content, extension.lower())
