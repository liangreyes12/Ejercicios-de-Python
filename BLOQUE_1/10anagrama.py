"""Dadas dos cadenas de texto (pueden contener letras, números, espacios y signos de puntuación)

- determina si son anagramas entre sí, ignorando mayúsculas/minúsculas y caracteres no alfabéticos. 
"""

print(f"""===DETECTOR DE ANAGRAMAS===
\n- No registrar palabras con acentos o tildes
""")
try:
    word1 = input(f"1) Ingrese palabra: ").lower().strip(".-_:,;[]*+}*{><#$/)(¿?'¡°|¨´ ")
    word2 = input(f"2) Ingrese palabra: ").lower().strip(".-_:,;[]*+}*{><#$/)(¿?'¡°|¨´ ")

    if len(word1) == len(word2):
        ordenar = sorted(word1)
        ordenar2 = sorted(word2)
        if ordenar == ordenar2:
            print(f"SON ANAGRAMAS: {word1} - {word2}")
        else:
            print(f"NO ES ANAGRAMA")
    else:
        print(f"NO SON ANAGRAMAS POR QUE NO TIENEN LAS MISMA CANTIDAD DE LETRAS")
except Exception as e:
    print(f"ERROR: {e}")
except KeyboardInterrupt:
    print(f"\nEL USUARIO A DETENIDO EL FLUJO DEL PROGRAMA")
except EOFError:
    print(f"\nEL USUARIO A DETENIDO EL FLUJO DEL PROGRAMA")