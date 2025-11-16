import pytest
from calculator import eval_tokens

def test_add():
    assert eval_tokens("2", "+", "3") == 5

def test_subtract():
    assert eval_tokens("5", "-", "2") == 3

def test_multiply():
    assert eval_tokens("3", "*", "4") == 12

def test_divide():
    assert pytest.approx(eval_tokens("10", "/", "4")) == 2.5

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        eval_tokens("1", "/", "0")

def test_invalid_number():
    with pytest.raises(ValueError):
        eval_tokens("a", "+", "2")

def test_unsupported_op():
    with pytest.raises(ValueError):
        eval_tokens("2", "^", "3")
