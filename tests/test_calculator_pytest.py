import pytest

from uheba_01.lek04_calculator import calculator, plus


def test_calk_plus():
    assert calculator('1+2') == 3

def test_no_signs():
    with pytest.raises(ValueError) as error:
        calculator('abracadabra')
    assert "Invalid expression (+-/*)" == error.value.args[0]

def test_two_signs():
    with pytest.raises(ValueError) as error:
        calculator('2+2+2')
    assert "Выражение должно содержать 2 числа и один оператор" == error.value.args[0]

def test_plus():
    assert plus(1, 2) == 3

def test_plus_zeroes():
    assert plus(0, 0) == 0

def test_plus_should_be_zero_if_negative():
    assert plus(1, -1) == 0

if __name__ == '__main__':
    pytest.main()