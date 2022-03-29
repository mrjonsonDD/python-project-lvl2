"""Test help function for gendiff."""
from gendiff.formatters.format_plain import format_val
from gendiff.formatters.format_stylish import get_indent


def test_converted_plain():  # noqa: F811
    assert format_val(False) == 'false'
    assert format_val(True) == 'true'
    assert format_val(None) == 'null'


def test_get_indent_stylish():
    assert get_indent(0) == ''
    assert get_indent(3) == '            '
