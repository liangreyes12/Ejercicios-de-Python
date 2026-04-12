"""
Implementa un programa que imprima los números del 1 al N 
(siendo N un entero positivo ingresado por el usuario) bajo las siguientes reglas complejas:

1. Regla de reemplazo múltiple:
NUEVO: Si el número es múltiplo de 7 → imprime "Bazz".

- Si es múltiplo de 3 y 7 → "FizzBazz".
- Si es múltiplo de 5 y 7 → "BuzzBazz".
- Si es múltiplo de 3, 5 y 7 → "FizzBuzzBazz".

2. Control de flujo inverso:
- El programa debe preguntar al usuario si desea ver la serie en orden ascendente (1..N) o descendente (N..1).
Dependiendo de la respuesta, se imprimirá en ese orden.

3. Salto condicional personalizado:
- Si el usuario ingresa un N mayor a 500, el programa debe mostrar una advertencia:
"N es muy grande. ¿Deseas continuar? (s/n)"
- Si responde "n", el programa termina sin imprimir nada.
- Si responde "s", imprime pero omitirá todos los números que sean primos (no los imprime ni aplica Fizz/Buzz).

4. Restricciones técnicas (para obligar a pensar diferente):
- No se permite usar for (usa while o recursividad).
- No se permite usar cadenas concatenadas para armar FizzBuzz; debes usar una función que acumule condiciones.
- El programa debe estar compuesto por al menos 3 funciones bien definidas
(por ejemplo: evaluar_numero, imprimir_serie, es_primo).
Manejar entradas inválidas del usuario (letras, negativos, cero) con mensajes claros y solicitar nuevamente.

5. Extra (opcional pero recomendado):
- Mide el tiempo de ejecución de la impresión y muéstralo en milisegundos al final.
"""

from sys import exit
print(f"===IMPRESION NUMERICA===")
try:
    limite = int(input(f"Ingrese limite: "))
    orden = int(input(f"Orden de impresion (1. ASC / 2. DES): "))
except KeyboardInterrupt:
    print(f"\nEL USUARIO A DETENIDO EL FLUJO DEL PROGRAMA")
    exit(1)
except EOFError:
    print(f"\nEL USUARIO A DETENIDO EL FLUJO DEL PROGRAMA")
    exit(1)
except ValueError:
    print(f"EL DATO INGRESADO DEBE SER DE TIPO NUMERICO ENTERO")
except Exception as e:
    print(f"ERROR: {e}")