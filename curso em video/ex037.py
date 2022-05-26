#Escreva um programa que leia um número inteiro qualquer
#e peça para o usuario escolher qual será a base de conversão:
#1 para binário
#2 para octal
#3 para hexadecimal

num = int(input('Digite um numero'))
print('''Escolha uma das bases para converter:
[1] converter para Binario
[2] converter para Octal
[3] converter para Headecimal 
''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('O numero {} convertido em Binario é: {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O numero {} convertido em Octal é: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{}{}'.format(num, hex(num)[2:]))
else:
    print("valor invalido")
