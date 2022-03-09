"""Test help function for gendiff."""
from gendiff.formatters.format_plain import format_val
"""from gendiff.formatters.format_stylish import format_value"""


"""def test_converted():  # noqa: F811
    assert format_value(False) == 'false'
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'"""


def test_converted_plain():  # noqa: F811
    assert format_val(False) == 'false'
    assert format_val(True) == 'true'
    assert format_val(None) == 'null'
