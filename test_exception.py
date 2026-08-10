import pytest

from src.exception import CustomException


def test_custom_exception():
    try:
        a = 10
        b = 0
        a / b

    except Exception as e:
        custom_error = CustomException(e, __import__("sys"))

        assert "division by zero" in str(custom_error)