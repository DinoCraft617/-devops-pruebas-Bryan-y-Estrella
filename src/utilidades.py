def invertir_palabra(palabra: str) -> str:
    """Devuelve la palabra al revés"""
    return palabra[::-1]

def es_palindromo(palabra: str) -> bool:
    """Verifica si una palabra es palíndromo"""
    return palabra.lower() == palabra.lower()[::-1]

def factorial(n: int) -> int:
    """Calcula factorial de un número (no negativo)"""
    if n < 0:
        raise ValueError("No existe factorial de negativos")
    return 1 if n == 0 else n * factorial(n-1)
