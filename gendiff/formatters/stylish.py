def stringify_value(value):
    """Преобразует значение в строку для вывода."""

    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return str(value)


def format_stylish(diff_tree):
    """Форматирует дерево различий в стильный вывод."""

    def format_node(node):
        key, status, value = node

        if status == "unchanged":
            return f"  {key}: {stringify_value(value)}"
        elif status == "added":
            return f"+ {key}: {stringify_value(value)}"
        elif status == "removed":
            return f"- {key}: {stringify_value(value)}"
        elif status == "changed":
            old_value, new_value = value
            return (
                f"- {key}: {stringify_value(old_value)}\n"
                f"+ {key}: {stringify_value(new_value)}"
            )

    lines = [format_node(node) for node in diff_tree]
    return "{\n" + "\n".join(lines) + "\n}"
