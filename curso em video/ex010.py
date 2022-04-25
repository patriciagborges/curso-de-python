#Crie um programa que leia quanto
# dinheiro uma pessoa tem na carteira e
# mostre quantos dolares ela pode comprar
#1 dolar = 3,27 reais

din = input('Quanto dinheiro você tem na sua carteira? R$')
dol = float(din) / 3.27

print('Com R${:0.2f} você pode comprar US${:0.2f}'.format(din, dol))


