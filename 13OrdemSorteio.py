import random
p = str(input("Primeiro Aluno: "))
s = str(input("Segundo aluno: "))
t = str(input("Terceiro aluno: "))
q = str(input("Quarto aluno: "))
lista = [p,s,t,q]
random.shuffle(lista)
print("A ordem de apresentação será")
print(lista)
