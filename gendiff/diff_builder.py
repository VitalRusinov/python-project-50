from collections import namedtuple

# Иммутабельная структура для хранения информации о различии
DiffNode = namedtuple("DiffNode", ["key", "status", "value"])

STATUSES = {
    "unchanged": "unchanged",
    "added": "added",
    "removed": "removed",
    "changed": "changed",
}


def build_diff(data1, data2):
    """Строит дерево различий между двумя словарями."""

    result = ()
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))

    for key in all_keys:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key not in data2:
            node = DiffNode(key, STATUSES["removed"], value1)
        elif key not in data1:
            node = DiffNode(key, STATUSES["added"], value2)
        elif value1 == value2:
            node = DiffNode(key, STATUSES["unchanged"], value1)
        else:
            node = DiffNode(key, STATUSES["changed"], (value1, value2))

        result = result + (node,)

    return result
