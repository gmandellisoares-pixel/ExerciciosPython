import math
an = float(input("Digite o angulo que vc deseja: "))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print("O angulo de {} tem o seno de {:.2f}".format(an,sen))
print("O angulo de {} tem o cosseno de {:.2f}".format(an,cos))
print("O angulo de {} tem a tangente de {:.2f}".format(an,tan))
