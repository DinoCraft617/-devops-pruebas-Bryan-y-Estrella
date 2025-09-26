import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.utilidades import invertir_palabra, es_palindromo

def test_integracion_invertir_y_palindromo():
    palabra = "oso"
    invertida = invertir_palabra(palabra)
    assert es_palindromo(invertida)