"""Stylish formatter for diff output."""

SPACES = 4


def stringify_value(value, depth):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return "null"
    if isinstance(value, dict):
        if not value:
            return "{}"

        indent = " " * ((depth + 1) * SPACES)
        closing_indent = " " * (depth * SPACES)

        lines = ["{"]
        for key, val in value.items():
            val_str = stringify_value(val, depth + 1)
            lines.append(f"{indent}{key}: {val_str}")
        lines.append(f"{closing_indent}}}")
        return "\n".join(lines)

    return str(value)


def format_node(node, depth):
    indent = " " * ((depth + 1) * SPACES)
    sign_indent = " " * ((depth + 1) * SPACES - 2)

    if node.status == "unchanged":
        val_str = stringify_value(node.value, depth + 1)
        return f"{sign_indent}  {node.key}: {val_str}"

    if node.status == "added":
        val_str = stringify_value(node.value, depth + 1)
        return f"{sign_indent}+ {node.key}: {val_str}"

    if node.status == "removed":
        val_str = stringify_value(node.value, depth + 1)
        return f"{sign_indent}- {node.key}: {val_str}"

    if node.status == "changed":
        old_val_str = stringify_value(node.old_value, depth + 1)
        new_val_str = stringify_value(node.new_value, depth + 1)
        old_line = f"{sign_indent}- {node.key}: {old_val_str}"
        new_line = f"{sign_indent}+ {node.key}: {new_val_str}"
        return old_line + "\n" + new_line

    if node.status == "nested":
        children_str = format_tree(node.children, depth + 1)
        return f"{indent}{node.key}: {children_str}"

    raise ValueError(f"Unknown status: {node.status}")


def format_tree(diff_tree, depth=0):
    lines = [format_node(node, depth) for node in diff_tree]
    indent = " " * (depth * SPACES)
    return "{\n" + "\n".join(lines) + "\n" + indent + "}"


def format_stylish(diff_tree):
    return format_tree(diff_tree)
