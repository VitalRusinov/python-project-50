"""JSON formatter module."""

import json
from typing import Any, Dict, List

from gendiff.diff_builder import DiffNode


def convert_node_to_dict(node: DiffNode) -> Dict[str, Any]:
    """
    Convert DiffNode to dictionary for JSON serialization.

    Args:
        node: diff node

    Returns:
        Dict[str, Any]: dictionary representation of node
    """
    result = {
        "key": node.key,
        "status": node.status,
    }

    if node.status == "nested":
        result["children"] = [
            convert_node_to_dict(child) for child in node.children
        ]
    elif node.status in ("added", "unchanged", "removed"):
        result["value"] = node.value
    elif node.status == "changed":
        result["old_value"] = node.old_value
        result["new_value"] = node.new_value

    return result


def format_json(diff_tree: List[DiffNode]) -> str:
    """
    Format diff tree as JSON string.

    Args:
        diff_tree: list of diff nodes

    Returns:
        str: JSON formatted diff
    """
    # Convert diff tree to list of dictionaries
    result_list = [convert_node_to_dict(node) for node in diff_tree]

    # Convert to JSON with pretty formatting (indent=2)
    return json.dumps(result_list, indent=2)
