from calculadora import multiplicar_numeros

def main():
    print("=== Calculadora de Multiplicación ===")
    try:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))
        resultado = multiplicar_numeros(num1, num2)
        print(f"Resultado: {num1} x {num2} = {resultado}")
    except ValueError:
        print("Error: Por favor ingresa valores numéricos válidos.")

if __name__ == "__main__":
    main()
