#Faça um programa que leia o nome completo de uma pessoa,
#moostrando em seguida o primeiro e o ultimo nome separadamente
#ex: Ana Maria Braga
#primeiro=Ana
#ultimo = Braga
n = str(input('Qual seu nome completo?')).strip()
nome = n.split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
