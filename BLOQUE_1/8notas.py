"""
Crea un programa que clasifique una n cantidad de notas numéricas promediandolas y siguiendo estos criterios:

- Insuficiente: [0, 3.0)
- Suficiente: [3.0, 4.0)
- Bien: [4.0, 4.7)
- Notable: [4.7, 5.0)
- Excelente: 5.0

Requisitos obligatorios:

1. Las notas pueden tener hasta dos decimales (ej: 4.75).

2.El programa debe validar que las notas esté entre 0 y 5, mostrando
un mensaje de error y pidiéndola de nuevo hasta que sea correcta.

3. Si la nota total promediada es exactamente 5.0, debe mostrar un mensaje especial: 
"¡Excelente! Matrícula de honor."

4. El programa debe preguntar al final si el usuario quiere clasificar otra nota (S/N). Si responde 'S',
reinicia el proceso; si responde 'N', termina mostrando un resumen con:
- Total de notas clasificadas.
- Cuántas fueron Insuficientes, Suficientes, Bien, Notable y Excelente.
"""
from MODULOS import notas

print(f"""===GESTOR DE NOTAS DE LIANG===
\n- Escoge una opcion para el conteo de Notas:
1. Inicio
2. Salir
""")

opcion = notas.UserData()
i = True
while i == True:
    match opcion:
        case 1:
            print(f"Ingrese cantidad de notas analizar: ")
            cantidad = notas.UserData()
            notasDatos = notas.obtenerNotas(cantidad)
            promedio = notas.promedioNotas(notasDatos)
            reiniciar = notas.reinicio()
            mensaje = notas.mensajeFinal(notasDatos)
            if reiniciar  == False:
                break
        case 2:
            print(f"Gracias por usar nuestro Software")
            notas.limpiezaPantalla()
        case _:
            print(f"OPCION INVALIDA, LAS OPCIONES SON (1 O 2)")