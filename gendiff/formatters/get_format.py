from gendiff.formatters.format_stylish import to_stylish
from gendiff.formatters.format_plain import to_plain
from gendiff.formatters.format_json import to_json


FORMAT_TYPES = {
    'stylish': to_stylish,
    'plain': to_plain,
    'json': to_json,
}


def select_formatter(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
