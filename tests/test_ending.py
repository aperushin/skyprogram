import pytest
from post import get_ending

ending_parameters = [
    (0, 'ев'), (1, 'й'), (2, 'я'), (5, 'ев'), (13, 'ев'), (101, 'й'),
]


@pytest.mark.parametrize('number, expected_result', ending_parameters)
def test_get_ending(number: int, expected_result: str):
    assert get_ending(number) == expected_result
