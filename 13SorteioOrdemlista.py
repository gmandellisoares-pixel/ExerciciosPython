import random
p = str(input("Primeiro Aluno: "))
s = str(input("Segundo Aluno: "))
t = str(input("Terceiro Aluno: "))
q = str(input("Quarto Aluno: "))
lista = [p,s,t,q]
random.shuffle(lista)
print("A ordem da apresentação será")
print(lista)
