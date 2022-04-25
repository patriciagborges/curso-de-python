#Faça um algoritmo que leia o preço de um produto
#e mostre seu novo preço com desconto de 5%
valor = float(input('Qual o preço do produto?R$ '))
desconto = valor - (valor * 5 / 100)

print('O produto que custava RS{}, na promoção com desconto de 5% vai custar R${:0.2f}'.format(valor, desconto))
