from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_json import format_json


FORMAT_TYPES = {
    'stylish': format_stylish,
    'plain': format_plain,
    'json': format_json,
}


def select_formatter(diff, style='stylish'):
    formatter = FORMAT_TYPES.get(style)
    return formatter(diff)
