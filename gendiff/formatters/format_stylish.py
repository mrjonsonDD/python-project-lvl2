from gendiff.constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
)

DEFAULT_INDENT = 4
FLAG_INDENT = 2


def to_stylish(difference, level=0):  # noqa: C901
    indent = level * DEFAULT_INDENT * ' '
    diff = []
    for key, value in sorted(difference.items()):
        if isinstance(value, list):
            flag, *rest = value
            if flag == UNCHANGED or flag == NESTED:
                diff.append(forming_string(UNCHANGED, key, rest[0], level + 1))
            if flag == CHANGED:
                diff.append(forming_string(DELETED, key, rest[0], level + 1))
                diff.append(forming_string(ADDED, key, rest[1], level + 1))
            if flag == DELETED:
                diff.append(forming_string(DELETED, key, rest[0], level + 1))
            if flag == ADDED:
                diff.append(forming_string(ADDED, key, rest[0], level + 1))
        else:
            diff.append(forming_string(UNCHANGED, key, value, level + 1))
    return '{\n' + '\n'.join(diff) + '\n' + indent + '}'


def forming_string(flag, key, value, level):
    flags = {
        ADDED: '+',
        DELETED: '-',
        UNCHANGED: ' '
    }
    indent = (level * DEFAULT_INDENT - FLAG_INDENT) * ' '
    if isinstance(value, dict):
        result = to_stylish(value, level)
        return f'{indent}{flags[flag]} {key}: {result}'
    return f'{indent}{flags[flag]} {key}: {format_value(value)}'

def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
