import pytest
from source import my_func


def test_add():
    result = my_func.add(5, 2)
    assert result == 7


def test_divide():
    result = my_func.divide(12, 4)
    assert result == 3


def test_divide_by_zero():
    """
    Test that my_func.divide raises a ZeroDivisionError when dividing by zero.
    """
    with pytest.raises(ZeroDivisionError):
        my_func.divide(5, 0)








