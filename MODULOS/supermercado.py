from os import system, name
import sys
from time import sleep

inventario = { "manzana":3500,
               "pera":3000,
               "banano":4000,
               "piña":5000,
               "arroz":3900,
               "pasta":5200,
               "aceite":7500,
               "jabon":2000,
               "azucar":4600,
               "sal": 1500
            }


def opcionMenu():
    opcion = 0
    while opcion != 1 and opcion != 2:
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1 or opcion == 2:
                return opcion
            else:
                print("OPCION INVALIDAD DEBE SER UN NUMERO ENTERO (1 O 2)")
        except KeyboardInterrupt:
            print("\nPROGRAMA FINALIZADO POR EL USUARIO")
            sys.exit(1)
        except EOFError:
            print("\nPROGRAMA FINALIZADO POR EL USUARIO")
            sys.exit(1)
        except ValueError:
            print("EL DATO INGRESADO DEBE SER UN NUMERO ENTERO (1 o 2)")
        except Exception as e:
            print(f"ERROR: {e}")


def cantidadProducto():
    cantidad = 0
    while cantidad <= 0:
        try:
            cantidad = int(input("Ingrese cantidad de productos a comprar: "))
            if cantidad >= 1:
                return cantidad
            else:
                print("La cantidad de productos a comprar debe ser mayor o igual a 1")
        except KeyboardInterrupt:
            print(f"\nPrograma detenido por el usuario")
            sys.exit(1)
        except EOFError:
            print(f"\nPrograma detenido por el usuario")
            sys.exit(1)
        except ValueError:
            print(f"EL DATO INGRESADO DEBE SER DE TIPO NUMERICO ENTERO Y MAYOR O IGUAL A 1")
        except Exception as e:
            print(f"ERROR: {e}")


def compraProducto():
    loop = cantidadProducto()
    precio = 0
    i = 1
    factura = {}
    while i <= loop:
        try:
            producto = input(f"{i}) Ingrese producto a comprar: ")
            if producto in inventario:
                cantidad = int(input(f"Ingrese cantidad de {producto}: "))
                if cantidad >= 1:
                    precio += inventario[producto] * cantidad
                    factura[producto] = cantidad 
                    i += 1
                else:
                    print(f"LA CANTIDAD DEL PRODUCTO DEBE SER MAYOR O IGUAL A 1")
            else:
                print(f"PRODUCTO INEXISTENTE EN INVENTARIO/AGOTADO")
        except KeyboardInterrupt:
            print(f"\nEl usuario ha detenido la ejecuccion del programa")
            sys.exit(1)
        except EOFError:
            print(f"\nEl usuario a detenido el programa")
            sys.exit(1)
        except ValueError:
                print(f"EL VALOR PARA LA CANTIDAD DEBE SER DE TIPO NUMERICO")
        except Exception as e:
            print(f"ERROR: {e}")
    return precio, factura


def descuento(total):
    match total:
        case total if total >= 15000 and total < 25000:
            return total - ((total * 8) / 100)
        case total if total >= 25000 and total < 50000:
            return total - ((total * 12) / 100)
        case total if total >= 50000:
             return total - ((total * 18) / 100)
        case _:
            return total
        

def facturacion(total, factura):
    print(f"\n===FACTURA DE COMPRAS===")
    for producto, cantidad in factura.items():
        print(f"{producto}........{cantidad}x{inventario[producto]}")
    print(f"TOTAL: {total}$")
        

def limpiezaPantalla():
    sistema = name
    if sistema == "nt":
        sleep(2)
        system("cls")
    else:
        sleep(2)
        system("clear")