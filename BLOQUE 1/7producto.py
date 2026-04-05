"""
Una tienda aplica descuentos escalonados según el monto total de compra (sin incluir impuestos) 
de acuerdo con las siguientes reglas:

- Si el monto es menor a $50,000, no hay descuento.

- Si el monto está entre $50,000 y $100,000 (incluyendo $50,000 pero excluyendo $100,000),
se aplica un descuento del 8%.

- Si el monto está entre $100,000 y $200,000 (incluyendo $100,000 pero excluyendo $200,000), se aplica un descuento del 12%.

- Si el monto es de $200,000 o más, se aplica un descuento del 18%.

- Además, si el cliente paga con tarjeta de fidelidad, obtiene un descuento adicional del 3% 
sobre el monto ya descontado. El cálculo del precio final debe considerar primero el descuento 
por monto y luego, si corresponde, el descuento adicional por tarjeta.
"""

from os import sys
print(f"===TIENDA DE LIANG===")
inventario = { "manzana":3500,
               "pera":3000,
               "banano":4000,
               "piña":5000,
               "arroz":3900,
               "pasta":5200,
               "aceite":7500,
               "jabon":2000,
               "azucar":4600
            }

while cantidad <= 0:
    try:
        cantidad = int(input("Ingrese cantidad de productos a comprar"))

    except KeyboardInterrupt:
        print(f"\nEL usuario a interrumpido el flujo del programa")
        sys.exit(1)
    except EOFError:
        print(f"\nEntrada no disponible")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")