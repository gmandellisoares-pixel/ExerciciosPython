import math
op = float(input("Cateto Oposto: "))
ad = float(input("Cateto Adjacente: "))
hip = math.hypot(op,ad)
print("A hipotenusa vai medir {:.2f}".format(hip))
