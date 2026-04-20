sal = float(input("Qual o seu salário? R$ "))
aum1 = sal*0.2 + sal
aum2 = sal*0.15 + sal
aum3 = sal*0.1 + sal
aum4 = sal*0.05 + sal
print("Salário antes do ajuste: R${}".format(sal))
if sal<=280:
      print("Aumento de 20%")
      print("Valor do aumento: R${}".format(sal*0.2))
      print("Seu novo salário será: R${:.2f}".format(aum1))
elif sal>280 and sal<=700:
      print("Aumento de 15%")
      print("Valor do aumento: R${}".format(sal*0.15))
      print("Seu novo salário será: R${:.2f}".format(aum2))
elif sal>700 and sal<=1500:
      print("Aumento de 10%")
      print("Valor do aumento: R${}".format(sal*0.1))
      print("Seu novo salário será: R${:.2f}".format(aum3))
elif sal>1500:
      print("Aumento de 5%")
      print("Valor do aumento: R${}".format(sal*0.05))
      print("Seu novo salário será: R${:.2f}".format(aum4))
