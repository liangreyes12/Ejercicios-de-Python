def clasificacionLados(a, b, c):
    if a == b and a == c and b == a and b == c:
        print(f"POR SUS LADOS ES: TRIANGULO EQUILATERO")
    elif a == b or a == c or b == a or b == c:
        print(f"POR SUS LADOS ES: TRIANGULO ISOSCELES")
    elif a != b and a != c and b != a and b != c:
        print(f"POR SUS LADOS ES:TRIANGULO ESCALENO")

def clasificacionAngulos(a, b, c):
    a = pow(a, 2)
    b = pow(b, 2)
    c = pow(c, 2)
    if a + b == c:
        print(f"POR SUS ANGULOS ES: RECTANGULO")
    elif a + b > c:
        print(f"POR SUS ANGULOS ES: ACUTÁNGULO")
    elif c > a + b:
        print(f"POR SUS ANGULOS ES: ACUTÁNGULO")