"""
Determina si un año es bisiesto.
- El año debe ser ingresado por el usuario
- Debe arrojar una alerta en caso de que el valor ingresado 
no sea un numero entero 
"""

while True:
    try:
        ano = int(input("Ingrese año para analizar: "))
        if ano % 4 == 0:
            print(f"El año {ano} es bicisesto")
        elif ano % 400 == 0:
            print(f"El año {ano} es bicisesto")
        elif ano % 100 == 0:
            print(f"El año {ano} es normal")
        else:
            print(f"El año {ano} es normal")
        break
    except ValueError:
        print(f"EL VALOR INGRESADO DEBE SER DE TIPO NUMERICO ENTERO")
    except Exception as e:
        print(f"ERROR: {e}")