#receba 4 nomes e troque a ordem de modo aleatorio
# e apresente na tela a ordem sorteada
import random
n1 = str(input('primeiro nome'))
n2 = str(input('segundo nome'))
n3 = str(input('terceiro nome'))
n4 = str(input('quarto nome'))
lista = [n1, n2, n3, n4]
print('A ordem de apresentação será:', lista )
random.shuffle(lista)
print(lista)
