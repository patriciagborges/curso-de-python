#Escreva um programa para aprovar o emprestimo bancario
# para a compra de uma casa.
# O programa vai perguntar o valor da casa,
# o salario do comprador e a
# quantidade de anos que ele vai pagar.
#Calcule o valor da prestação sabendo que ela não pode
# execeder 30%
#do salário ou então o emprestimo será negago.

'''
Primeira resolução:
valor = float(input('Qual o valor da casa? R$: '))
salario = float(input('Qual o seu salário do comprador? R$:'))
parcelas = int(input('Quantas meses vai financiar?'))
vlparcelas = valor / parcelas
print('O valor de cada parcela vai ser R$:{:.1f}'.format(vlparcelas))
porcento = salario *30/100
print('30% do salario é {}'.format(porcento))
if (vlparcelas < porcento):
    print('Seu emprestimo foi aprovado!')
else:
    print('Seu emprestimo foi negado!')
'''

#Segunda resolução:
'''
casa = float(input('Valor da casa R$: '))
salario = float(input('Salario do comprador? R$'))
prazo = int(input('Quantos anos de financiamento?'))
prestacao = casa / (prazo * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa, prazo))
print('O valor da prestação será de R$ {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Aprovado')
else:
    print('Emprestimo negado!')
'''
