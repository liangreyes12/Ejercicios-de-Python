"""
Simula un login: usuario y contraseña correctos → acceso permitido.

- Crea un listado de minimo 5 usuarios, pidele al usuario que ingrese
sus credenciales y evalua si esta registrado en el sistema

- El usuario tendrá como máximo 3 intentos para acceder al sistema
si se equivoca 3 veces al ingresar su usuario o contraseña se deberá 
arrojar una alerta donde ya no tendrá acceso al sistema

- Debe incluir una excepcion para errores inesperados
"""
from os import sys

listado = {"liang":"Liang123CoOL", 
           "jhon":"Type&7.ka@", 
           "lisandro":"po098jb@.-", 
           "nathalia":"8329/0?9ejd",
           "jose":"'owkp4o5qelrv4@12"
        }

intentos = 1
maximo = 3
while intentos <= maximo:
    try:
        user = input(f"{intentos}) Ingrese su usuario: ").lower()
        password = input(f"{intentos})Ingrese su contraseña: ")

        if user in listado and listado[user] == password:
            print(f"ACCESO PERMITIDO")
            break
        else:
            print(f"El usuario no existe o la contraseña es errada")
            if intentos == 3:
                print(f"ACCESO DENEGADO, NUMERO MAXIMO DE INTENTOS {intentos}")
                break
        intentos += 1
    except KeyboardInterrupt:
        print(f"\n⚠️  Operación cancelada por el usuario (Ctrl+C)")
        sys.exit(1)
    except EOFError:
        print(f"\n⚠️  Entrada no disponible")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        
# for i in range(0, 3, 1):
#     user = input("Ingrese su usuario: ")
#     password = input("Ingrese su contraseña: ")