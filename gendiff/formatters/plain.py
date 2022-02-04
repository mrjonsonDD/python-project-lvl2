from gendiff.const import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
)


ADDED_STR = "Property '{0}' was added with value: {1}"
DELETED_STR = "Property '{0}' was removed"
CHANGED_STR = "Property '{0}' was updated. From {1} to {2}"


def format_plain(diff, key_path=None):  # noqa: C901
    result = []
    if not key_path:
        key_path = []
    for key, value in sorted(diff.items()):
        key_path.append(key)
        status, *rest = value[0], value[1:]
        if status == UNCHANGED:
            key_path.pop()
            continue
        elif status == ADDED:
            result.append(ADDED_STR.format(
                '.'.join(key_path), get_value(rest[0])))
            key_path.pop()
        elif status == DELETED:
            result.append(DELETED_STR.format('.'.join(key_path)))
            key_path.pop()
        elif status == NESTED:
            result.append(format_plain(rest[0], key_path))
            key_path.pop()
        elif status == CHANGED:
            result.append(CHANGED_STR.format(
                '.'.join(key_path), get_value(rest[0]),
                get_value(rest[1])))
            key_path.pop()
    return '\n'.join(result)


def get_value(value):
    if type(value) in (list, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return value
