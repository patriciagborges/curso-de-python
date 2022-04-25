#Faça um algoritmo que leia um salário
# de um funcionario e mostre seu salario com
#15% de aumento

salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)

print('Um funcionário que ganhava R$ {:.2f}, com aumento de 15%, passa a receber R$ {:.2f}'.format(salario, aumento))