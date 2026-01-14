"""Diff builder module for generating difference trees."""

from typing import Any, Dict, List


# Структура узла дерева различий
class DiffNode:
    """Node in the difference tree."""

    def __init__(
        self,
        key: str,
        status: str,
        value: Any = None,
        old_value: Any = None,
        new_value: Any = None,
        children: List["DiffNode"] = None,
    ):
        self.key = key
        # Возможные статусы:'unchanged','added', removed','changed','nested'
        self.status = status
        self.value = value  # используется для unchanged, added, removed
        self.old_value = old_value  # используется для changed
        self.new_value = new_value  # используется для changed
        self.children = children or []  # используется для nested

    def __repr__(self) -> str:
        return f"DiffNode(key={self.key}, status={self.status})"


def is_dict(value: Any) -> bool:
    """Check if value is a dictionary."""
    return isinstance(value, dict)


def build_diff(data1: Dict[str, Any], data2: Dict[str, Any]) -> List[DiffNode]:
    """
    Build a difference tree between two dictionaries recursively.

    Args:
        data1: first dictionary
        data2: second dictionary

    Returns:
        List[DiffNode]: list of diff nodes representing the difference
    """
    result = []
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        # Key exists only in first file
        if key not in data2:
            result.append(DiffNode(key, "removed", value=value1))

        # Key exists only in second file
        elif key not in data1:
            result.append(DiffNode(key, "added", value=value2))

        # Both values are equal
        elif value1 == value2:
            result.append(DiffNode(key, "unchanged", value=value1))

        # Both values are dictionaries - need recursive comparison
        elif is_dict(value1) and is_dict(value2):
            children = build_diff(value1, value2)
            result.append(DiffNode(key, "nested", children=children))

        # Values are different and not both dictionaries
        else:
            result.append(
                DiffNode(key, "changed", old_value=value1, new_value=value2)
            )

    return result
