from gendiff.constants import (
    ADDED,
    CHANGED,
    DELETED,
    NESTED,
    UNCHANGED
)

DEFAULT_INDENT = 4
FLAG_INDENT = 2
flags = {
        ADDED: '+',
        DELETED: '-',
        UNCHANGED: ' '
    }


def to_stylish(difference, level=0):  # noqa: C901
    indent = level * DEFAULT_INDENT * ' '
    diff = []
    for key, value in sorted(difference.items()):
        if isinstance(value, list):
            flag, *rest = value
            if flag == UNCHANGED or flag == NESTED:
                updated_val = rest[0]
                format_val = forming_str(UNCHANGED, key, updated_val, level + 1)
                diff.append(format_val)
            if flag == CHANGED:
                updated_val = rest[0]
                format_val = forming_str(DELETED, key, updated_val, level + 1)
                diff.append(format_val)
                updated_val = rest[1]
                format_val = forming_str(ADDED, key, updated_val, level + 1)
                diff.append(format_val)
            if flag == DELETED:
                updated_val = rest[0]
                format_val = forming_str(DELETED, key, updated_val, level + 1)
                diff.append(format_val)
            if flag == ADDED:
                updated_val = rest[0]
                format_val = forming_str(ADDED, key, updated_val, level + 1)
                diff.append(format_val)
        else:
            updated_val = value
            format_val = forming_str(UNCHANGED, key, updated_val, level + 1)
            diff.append(format_val)
    return '{\n' + '\n'.join(diff) + '\n' + indent + '}'


def forming_str(flag, key, value, level):
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
