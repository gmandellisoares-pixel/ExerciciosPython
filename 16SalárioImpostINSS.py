h = float(input("Quanto vc ganha por hora? "))
nh = float(input("Quantas horas trabalhou por mes? "))
s = h*nh
ir =  0.11*s
inss = 0.08*s
si = 0.05*s
sl = s - ir - inss - si
print("Salário Bruto: R${}".format(s))
print("IR (11%) : R${}".format(ir))
print("INSS (8%) : R${}".format(inss))
print("Sindicato (5%) : R${}".format(si))
print("Salário Liquido : R${}".format(sl))
