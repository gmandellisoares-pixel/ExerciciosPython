a = int(input("Valor de A: "))
if a == 0:
    print("Equação de primeiro grau, inválido")
else:
    b = int(input("Valor de B: "))
    c = int(input("Valor de C: "))

    delta = (b**2) - (4*a*c)

    if delta < 0:
        print("A equação não possui raízes reais")
    elif delta == 0:
        x = -b / (2*a)
        print("Apenas uma raiz real: {}".format(x))
    else:
        x1 = (-b + (delta**0.5)) / (2*a)
        x2 = (-b - (delta**0.5)) / (2*a)
        print("Possui duas raízes reais e diferentes:")
        print("{} e {}".format(x1, x2))
