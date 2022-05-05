#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 parta viagens mais longas.

distancia = int(input('qual a distancia da viagem em km?'))
if distancia <= 200:
    valor = distancia * 0.50
    print('o valor da viagem  será R${:.2f} Reais'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da passagem será R${:.2f} reais'.format(valor))
