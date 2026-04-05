"""
Determina si un número ingresado por el usuario es positivo, negativo o cero.
- El numero debe ser ingresado por el usuario
- Deberas verificar que el tipo de dato ingresado sea un entero en caso contrario
deberás arrojar una alerta y continuar con el flujo del programa.
"""

while True:
    try:
        numero = int(input("- Ingrese un numero: "))
        if numero == 0:
            print(f"El numero es {numero}")
        elif numero > 0:
            print(f"El numero {numero} es positivo")
        else:
            print(f"El numero {numero} es negativo")
        break
    except ValueError:
        print(f"EL DATO INGRESADO DEBE SER DE TIPO NUMERICO ENTERO")
    except Exception as e:
        print(f"ERROR: {e}")