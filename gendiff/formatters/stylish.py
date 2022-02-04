from gendiff.const import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
)

DEFAULT_INDENT = 4
STATUS_INDENT = 2
STATUSES = {
    ADDED: '+',
    DELETED: '-',
    UNCHANGED: ' '
}


def format_stylish(diff, lvl=0):  # noqa: C901
    indent = lvl * DEFAULT_INDENT * ' '
    result = []
    for key, value in sorted(diff.items()):
        if isinstance(value, list):
            status, *rest = value
            if status == CHANGED:
                result.append(get_string(DELETED, key, rest[0], lvl + 1))
                result.append(get_string(ADDED, key, rest[1], lvl + 1))
            elif status == DELETED:
                result.append(get_string(DELETED, key, rest[0], lvl + 1))
            elif status == ADDED:
                result.append(get_string(ADDED, key, rest[0], lvl + 1))
            elif status == NESTED or status == UNCHANGED:
                result.append(get_string(UNCHANGED, key, rest[0], lvl + 1))
        else:
            result.append(get_string(UNCHANGED, key, value, lvl + 1))
    return '{\n' + '\n'.join(result) + '\n' + indent + '}'


def get_string(status, key, value, lvl):
    indent = (lvl * DEFAULT_INDENT - STATUS_INDENT) * ' '
    if isinstance(value, dict):
        result = format_stylish(value, lvl)
        return f'{indent}{STATUSES[status]} {key}: {result}'
    return f'{indent}{STATUSES[status]} {key}: {format_value(value)}'


def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
