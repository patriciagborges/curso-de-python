#Pergunte o salário e calcule o aumento
#Para salario até 1250 dê 10%
# para salarios menores dê 15%

salario = float(input('Qual seu salário?'))

if salario > 1250.00:
    print('Seu aumento foi de 10%, seu novo salario é : R$ {:.2f} Reais'.format(salario + (salario * 10 / 100)))
else:
    print('Seu aumento foi de 15%, seu novo salario é: R$ {:.2f} Reais'.format(salario*0.15 + salario))

