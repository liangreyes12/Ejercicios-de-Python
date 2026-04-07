"""
Una tienda aplica descuentos escalonados según el monto total de compra (sin incluir impuestos) 
de acuerdo con las siguientes reglas:

- Si el monto es menor a $10,000, no hay descuento.

- Si el monto está entre $15,000 y $25,000 (incluyendo $15,000 pero excluyendo $25,000),
se aplica un descuento del 8%.

- Si el monto está entre $25,000 y $50,000 (incluyendo $25,000 pero excluyendo $50,000), 
se aplica un descuento del 12%.

- Si el monto es de $50,000 o más, se aplica un descuento del 18%.
"""

import sys
from MODULOS import supermercado

print(f"""===TIENDA DE LIANG===
\n ESCOGE UNA OPCION: 
      1. Comprar Productos
      2. Salir
""")

opcion = supermercado.opcionMenu()

match opcion:
    case 1:
        precio, factura = supermercado.compraProducto()
        total = supermercado.descuento(precio)
        supermercado.facturacion(total, factura)
    case 2:
        print("Gracias por comprar en nuestra tienda, vuelva pronto!")
        supermercado.limpiezaPantalla()