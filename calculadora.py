def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b


def calculadora():
    print("\n--- CALCULADORA PYTHON ---")

    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        print("\n1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            resultado = sumar(a, b)

        elif opcion == "2":
            resultado = restar(a, b)

        elif opcion == "3":
            resultado = multiplicar(a, b)

        elif opcion == "4":
            resultado = dividir(a, b)

        else:
            print("Opción inválida.")
            return

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: ingresá un valor numérico válido.")

    except ZeroDivisionError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    calculadora()