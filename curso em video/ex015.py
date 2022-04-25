#Aluguel de carros
#Escreva um programa que pergunte a quantidade de km rodados por
#um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60,00 a diaria e
#0,15 por km rodado.
dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km rodados?'))
valor_pag = (dias * 60) + (km * 0.15)

print('O valor total pago por um veiculo alugado {} dias e que rodou {}Km, custa: R$ {:.2f}'.format(dias, km, valor_pag))


