import pytest
from gendiff.formatters.plain import get_value


@pytest.mark.parametrize(
    'value',
    [
        10,
        (1, 2, 3),
    ],
)
def test_format_value(value):
    assert get_value(value) == value