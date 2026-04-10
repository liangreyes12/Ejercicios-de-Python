def clasificacionLados(a, b, c):
    if a == b and a == c and b == a and b == c:
        print(f"TRIANGULO EQUILATERO")
    elif a == b or a == c or b == a or b == c:
        print(f"TRIANGULO ISOSCELES")
    elif a != b and a != c and b != a and b != c:
        print(f"TRIANGULO ESCALENO")

def clasificacionAngulos():
    pass
