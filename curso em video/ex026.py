#Faça um programa que leia uma frase e mostre:
#Quantas vezes aparece a letra "a"
#em qual posição ela aparece na primeira vez
#Em que posição ela aparece na ultima vez

frase = str(input('Escreva uma frase')).upper().strip()
print('A letra A aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))