"""
Verifica si un número es par o impar e imprimelo en pantalla
- El numero debe ser ingresado por el usuario
- Debes verificar que el numero ingresado sea de tipo entero
de lo contrario arroja una alerta de error
"""

while True:
    try:
        numero = int(input(f"Ingrese un numero: "))
        if numero == 0:
            print(f"El numero {numero} es cero")
        elif numero % 2 == 0:
            print(f"El numero {numero} es par")
        else:
            print(f"El numero {numero} es impar")
        break
    except ValueError:
        print(f"EL DATO INGRESADO {numero} DEBE SER DE TIPO NUMERICO ENTERO")
    except Exception as e:
        print(f"ERROR: {e}")