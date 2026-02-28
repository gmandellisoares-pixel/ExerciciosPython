import math
area = float(input("Digite o tamanho da area a ser pintada (em m²): "))
litros = area/3
latas = math.ceil(litros/18)
preco = latas*80
print("Vc precisará de {} latas de tinta".format(latas))
print("O preço total será R$ {:.2f}".format(preco))
