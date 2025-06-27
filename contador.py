
def es_par(n):
    """
    Determina si un número es par o impar.

    Args:
        n (int): El número a evaluar.

    Returns:
        str: 'par' si es par, 'impar' si es impar.
    """
    return 'par' if n % 2 == 0 else 'impar'


def cuenta_regresiva(n):
    """
    Imprime una cuenta regresiva desde n hasta 0, mostrando si cada número es par o impar.

    Args:
        n (int): Número entero desde el cual iniciar la cuenta regresiva.
    """
    if n < 0:
        return
    print(f"{n} - {es_par(n)}")
    if n == 0:
        print("🎉 ¡Llegamos a cero! Fin de la cuenta regresiva.")
    else:
        cuenta_regresiva(n - 1)
