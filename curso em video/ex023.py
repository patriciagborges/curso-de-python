#Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
#ex: digite 1867
#unidade 4
#dezena 3
#centena 8
#milhar 1

n = int(input('digete um numero de até 4 dígitos'))
num = str(n)
print('Unidade: {}'.format(num[3]))
print('Dezena: {}'.format(num[2]))
print('Centena: {}'.format(num[1]))
print('Milhar: {}'.format(num[0]))
