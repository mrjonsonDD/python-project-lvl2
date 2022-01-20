import pytest
from gendiff.generate import generate_diff


@pytest.fixture
def first_file():
    return 'tests/fixtures/file1.json'


@pytest.fixture
def second_file():
    return 'tests/fixtures/file2.json'


expected_result = '{\n\t- follow: False\n\t  host: hexlet.io\n\t' \
                  '- proxy: 123.234.53.22\n\t- timeout: 50\n\t' \
                  '+ timeout: 20\n\t+ verbose: True\n}\n'


def test1(first_file, second_file):
    assert generate_diff(first_file, second_file) == expected_result