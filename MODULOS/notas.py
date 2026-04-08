import sys
from time import sleep
from os import system, name

def obtenerNotas(n):
    i = 1
    listado = []
    while i <= n:
        nota = float(input(f"{i}) Ingrese Nota: "))
        nota = round(nota, 2)
        if nota >= 0 and nota <= 5:
            listado.append(nota)
            i += 1
        else:
            print(f"NOTA INVALIDA, DEBE SER ENTRE 0 y 5.0")
    print(listado)
    return listado

def promedioNotas(nota):
    total = sum(nota) / len(nota)
    if total >= 0 and total < 3.0:
        print(f"Lo sentimos, Nota Insuficiente: {round(total, 2)}")
    elif total >= 3.0 and total < 4.0:
        print(f"Haz logrado aprobar, Nota Suficiente: {round(total, 2)}")
    elif total >= 4.0 and total < 4.7:
        print(f"Aprobaste, Nota Bien: {round(total, 2)}")
    elif total >= 4.7 and total < 5.0:
        print(f"Aprobaste, Desempeño Notable: {round(total, 2)}")
    else:
        print(f"¡Excelente! Matrícula de honor: {round(total, 2)}")

def reinicio(i):
    user = ""
    while user != "S" or user != "N":
        print(f"¿Quiere clasificar otra nota? (S/N):")
        user = input(f"- ").upper()
        if user == "S":
            pass
        elif user == "N":
            
            i = False
        else:
            print(f"OPCION INVALIDA, DEBES ESCOGER: (S/N)")

def mensajeFinal(listadoNotas):
   pass

def UserData():
    n = 0
    while n <= 0:
        try:
            n = int(input("- "))
            if n >= 1:
                return n
            else:
                print(f"EL DATO INGRESADO DEBE SER COMO MINIMO MAYOR O IGUAL A 1")
        except KeyboardInterrupt:
            print(f"El usuario a interrumpido el programa")
            sys.exit(1)
        except EOFError:
            print(f"\nEl usuario a detenido el programa")
            sys.exit(1)
        except ValueError:
            print(f"EL DATO INGRESADO DEBE SER DE TIPO NUMERICO ENTERO")
        except Exception as e:
            print(f"ERROR: {e}")

def limpiezaPantalla():
    sistema = name
    if sistema == "nt":
        sleep(2)
        system("cls")
    else:
        sleep(2)
        system("clear")