#Crie um programa que leia um número real qualquer
# e mostre sua porção inteira
#ex: digite 6.127 a porção inteira: 6

#Resolução1
#import math
#num = float(input('Digite um valor:'))
#num_inteiro = math.trunc(num)
#print('O valor digitado foir {} e sua porção inteira é {}'.format(num, num_inteiro))

#resolução2
#import math
#num = float(input('Digite um numero'))
#print('O valor digitado foi {} e sua parte inteira é {}'.format(num, math.trunc(num)))

#Resolução 3
#from math import trunc
#num = float(input('digite um num'))
#print(trunc(num))

#resolução extra
num = float(input('digite um num'))
print('o num digitado foi: {} e sua porçao inteira é {}'.format(num, int(num)))