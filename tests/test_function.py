"""Test help function for gendiff."""
from gendiff.formatters.format_plain import format_val


def test_converted_plain():  # noqa: F811
    assert format_val(False) == 'false'
    assert format_val(True) == 'true'
    assert format_val(None) == 'null'
