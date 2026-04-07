"""
Dado un número, indica si es múltiplo de 3 y 5.
"""
import sys

while True:
    try:
        numero = int(input("Ingrese numero: "))
        if numero == 0:
            print(f"El numero es {0}")
        elif numero % 3 == 0 and numero % 5 == 0:
            print(f"El numero {numero} es multiplo de 3 y 5") 
        else:
            print(f"El numero no es multiplo ni de 3 ni de 5")
        break
    except KeyboardInterrupt:
        print(f"\nEl usuario a interrumpido el programa")
        sys.exit(1)
    except EOFError:
        print("\nEntrada no disponible")
        sys.exit(1)
    except ValueError:
        print(f"EL DATO INGRESADO DEBE SER DE TIPO NUMERICO ENTERO")
    except Exception as e:
        print(f"ERROR:{e}")