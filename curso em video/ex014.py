#Converta a temperatura
#calculo = grauscelsios x 1.8 + 32
#ou ((9*c)/5)+32

c = float(input('Qual a temperatura?'))
f = c * 1.8 + 32
print('A temperatura de {:.1f}c° corresponde a {:.1f}°F'.format(c, f))
