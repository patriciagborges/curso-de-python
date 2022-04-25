#Escreva um programa que leia um valor em metros
# e exiba convertido em centimetros e milimetros
#1m = 100 cm
#1m = 1000 milimetros

metros = input('Uma distancia em metros')
c = float(metros) * 100
m = float(metros) * 1000
print('A medida de {}m em centimetros é {}cm \n Em milimetros é {}mili'.format(metros, c, m))

