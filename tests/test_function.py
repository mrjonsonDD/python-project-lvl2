"""Test help function for gendiff."""
from gendiff.constants import ADDED, DELETED, UNCHANGED
from gendiff.formatters.format_plain import format_value
from gendiff.formatters.format_stylish import format_value


def test_converted():  # noqa: D103
    assert format_value(False) == 'false'
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'


def test_converted_plain():  # noqa: D103
    assert format_value(False) == 'false'
    assert format_value(True) == 'true'
    assert format_value(None) == 'null'
