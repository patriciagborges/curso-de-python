#Faça um programa que leia a largura e a altura
#de uma parede em metros
#calcule sua área e a quantidade de tinta
#sabendo que cada litro pinta 2mt2
l = input('Qual a largura da parede?')
a = input('Qual a altura da parede?')
m2 = float(l) * float(a)
tinta = m2 / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m²\n Para pintar essa parede, você precisará de {} de tinta'.format(l, a, m2, tinta))
