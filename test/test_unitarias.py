import pytest
from src.utilidades import invertir_palabra, es_palindromo, factorial

def test_invertir_palabra():
    assert invertir_palabra("gato") == "otag"

def test_es_palindromo_true():
    assert es_palindromo("Anilina") is True

def test_es_palindromo_false():
    assert es_palindromo("Python") is False

def test_factorial_valido():
    assert factorial(5) == 120

def test_factorial_error():
    with pytest.raises(ValueError):
        factorial(-3)