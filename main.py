import contador

def main():
    """
    Función principal que solicita un número al usuario y ejecuta la cuenta regresiva.
    """
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor, ingrese un número positivo.")
        else:
            print("\n🔽 Iniciando cuenta regresiva:\n")
            contador.cuenta_regresiva(numero)
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")

if __name__ == "__main__":
    main()
