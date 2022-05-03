#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras minusculas
#O nome com todas as letras maiusculas
#quantas letras ao sem considerar o espaço
#quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é:{}'.format(nome.upper()))
print('Seu nome em minusculas é:{}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nome.split()[0], len(nome.split()[0])))