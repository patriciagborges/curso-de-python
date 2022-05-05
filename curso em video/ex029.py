#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma msg que ele foi multado
#A multa vai custar R$7,00 por cada km acima do limite

#resolução1
#velocidade = int(input('Qual a velocidade do carro?'))
#if velocidade <= 80:
#    print('Velocidade dentro do limite')
#else:
#    multa = (velocidade - 80)*7
#    print('Você foi multado! Sua multa é de R${} reais'.format(multa))

#Resolução2
velocidade = float(input('Qual a velociade atual do carro?'))
if velocidade > 80:
    print("você foi multado")
    multa = (velocidade - 80) *7
    print('Sua multa vai custar R$ {} Reais'.format(multa))
else:
    print('Velocidade dentro do limite')