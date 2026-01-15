"""Plain formatter module."""

from typing import Any, List

from gendiff.diff_builder import DiffNode


def format_value(value: Any) -> str:
    """
    Format value for plain output.

    Args:
        value: value to format

    Returns:
        str: formatted value
    """
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, list):
        return "[complex value]"
    else:
        return str(value)


def format_node(node: DiffNode, path: str = "") -> List[str]:
    """
    Format a single diff node for plain output.

    Args:
        node: diff node
        path: current path (for nested properties)

    Returns:
        List[str]: list of formatted lines
    """
    current_path = f"{path}.{node.key}" if path else node.key
    result = []

    if node.status == "nested":
        for child in node.children:
            result.extend(format_node(child, current_path))

    elif node.status == "added":
        formatted_value = format_value(node.value)
        result.append(
            f"Property '{current_path}' was added with value: {formatted_value}"
        )

    elif node.status == "removed":
        result.append(f"Property '{current_path}' was removed")

    elif node.status == "changed":
        old_formatted = format_value(node.old_value)
        new_formatted = format_value(node.new_value)
        result.append(
            f"Property '{current_path}' was updated. "
            f"From {old_formatted} to {new_formatted}"
        )

    return result


def format_plain(diff_tree: List[DiffNode]) -> str:
    """
    Format diff tree as plain text.

    Args:
        diff_tree: list of diff nodes

    Returns:
        str: formatted plain text diff
    """
    lines = []
    for node in diff_tree:
        lines.extend(format_node(node))

    return "\n".join(lines)
