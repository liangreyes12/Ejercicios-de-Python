"""Dadas tres longitudes (números reales positivos)
- Determina si pueden formar un triángulo válido.
- En caso afirmativo, clasifica el triángulo por sus lados
(equilátero, isósceles o escaleno)
- También por sus ángulos (acutángulo, rectángulo u obtusángulo).
- Implementa la solución con validación de entrada robusta 
y eficiencia computacional."""

from MODULOS import calculoTriangulo
import sys

print(f"===ANALISIS NUMERICO DE TRIANGULOS===")
while True:
    try:
        valor1 = float(input("Ingrese valor de lado (A): "))
        valor2 = float(input("Ingrese valor de lado (B): "))
        valor3 = float(input("Ingrese valor de lado (C): "))
        suma = valor1 + valor2
        if valor1 < 0 or valor2 < 0 or valor3 < 0:
            print(f"LOS DATOS DEBEN SER MAYORES O IGUAL A 1")
        elif suma <= valor3:
            print(f"No se puede formar un triangulo, la suma de los lados (A) y (B) es menor al lado más grande")
            break
        else:
            print(f"===CLASIFICACION DEL TRIANGULO===")
            lados = calculoTriangulo.clasificacionLados(valor1, valor2, valor3)
            break
    except KeyboardInterrupt:
        print(f"\nEL USUARIO HA DETENIDO EL FLUJO DEL PROGRAMA")
        sys.exit(1)
    except EOFError:
        print(f"\nEL USUARIO HA DETENIDO EL PROGRAMA")
        sys.exit(1)
    except ValueError:
        print(f"EL VALOR INGRESADO DEBE SER DE TIPO NUMERICO FLOTANTE")
    except Exception as e:
        print(f"ERROR: {e}")
