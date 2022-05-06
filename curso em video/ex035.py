#leia o comprimento de tres retas
#diga se elas formam um trangulo

a = int(input('qual tamanho da reta'))
b = int(input('Qual o tamanho da outra reta'))
c = int(input('Tamanho da terceira reta'))
if a < b + c and b < a + c and c < a + b:
    print('Forma triangulo')
else:
    print('Não forma triangulo')
