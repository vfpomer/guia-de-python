def calculadora():
    """
    Calculadora que utiliza funciones lambda para realizar operaciones matemáticas básicas.
    Permite al usuario elegir la operación e ingresar los operandos.
    """
    # Definir operaciones usando funciones lambda
    operaciones = {
        '1': {
            'nombre': 'Suma',
            'simbolo': '+',
            'funcion': lambda x, y: x + y
        },
        '2': {
            'nombre': 'Resta',
            'simbolo': '-',
            'funcion': lambda x, y: x - y
        },
        '3': {
            'nombre': 'Multiplicación',
            'simbolo': '*',
            'funcion': lambda x, y: x * y
        },
        '4': {
            'nombre': 'División',
            'simbolo': '/',
            'funcion': lambda x, y: x / y if y != 0 else "Error: División por cero"
        },
        '5': {
            'nombre': 'Potencia',
            'simbolo': '^',
            'funcion': lambda x, y: x ** y
        },
        '6': {
            'nombre': 'Módulo',
            'simbolo': '%',
            'funcion': lambda x, y: x % y if y != 0 else "Error: Módulo por cero"
        },
        '7': {
            'nombre': 'Raíz',
            'simbolo': '√',
            'funcion': lambda x, y: x ** (1/y) if y != 0 else "Error: Exponente inválido"
        }
    }

    def mostrar_menu():
        """Muestra el menú de operaciones disponibles"""
        print("\n==== CALCULADORA FUNCIONAL ====")
        for key, op in operaciones.items():
            print(f"{key}. {op['nombre']} {op['simbolo']}")
        print("0. Salir")
        return input("\nSeleccione una operación (0-7): ")

    def obtener_numeros():
        """Solicita y valida los números para la operación"""
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            return num1, num2
        except ValueError:
            print("Error: Ingrese solo valores numéricos")
            return obtener_numeros()

    # Bucle principal
    while True:
        opcion = mostrar_menu()
        
        if opcion == '0':
            print("¡Gracias por usar la calculadora!")
            break
            
        if opcion not in operaciones:
            print("Opción inválida. Intente nuevamente.")
            continue
            
        num1, num2 = obtener_numeros()
        operacion = operaciones[opcion]
        
        # Aplicar la función lambda correspondiente
        resultado = operacion['funcion'](num1, num2)
        # Mostrar el resultado
        print(f"\nOperación: {num1} {operacion['simbolo']} {num2}")
        print(f"Resultado: {resultado:.2f}")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Desea realizar otra operación? (s/n): ").lower()
        if continuar != 's':
            print("¡Gracias por usar la calculadora!")
            break

if __name__ == "__main__":
    calculadora()