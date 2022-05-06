#Leia 3 numeros
#Mostre qual é o maior
#e qual é o menor

n1 = int(input('digite num 1'))
n2 = int(input('digite num 2'))
n3 = int(input('digite num 3'))
maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
print('Maior número é {}'.format(maior))
menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('Menor número é {}'.format(menor))
