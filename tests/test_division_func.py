import pytest
from current.solution import division


@pytest.mark.parametrize("a, b, c", [(10, 2, 5), (10, -2, -5), (10, -1, -10)])
def test_division(a, b, c):
    assert division(a, b) == c


if __name__ == '__main__':
    pytest.main()
