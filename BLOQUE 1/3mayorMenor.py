"""
Pide una cantidad (n) números y muestra el mayor.
- los numeros deben ser ingresados por el usuario
- Debes verificar que el numero ingresado sea de tipo entero
de lo contrario arroja una alerta de error
"""
listado = []
while True:
    try:
        cantidad = int(input("Cantidad de numeros a ingresar: "))
        for i in range(0, cantidad, 1):
            numero = int(input(f"{i+1}) Ingrese numero: "))
            listado.append(numero)
        print(f"El numero mayor es: {max(listado)}")
        break
    except ValueError:
        print(f"EL DATO DEBE SER DE TIPO NUMERICO ENTERO")
    except Exception as e:
        print(f"ERROR: {e}")