#Dissecando uma variável
item1 = input('digite algo')
print('O tipo primitivo de {} é '.format(item1), type(item1))
print('{} Só tem espaços?'.format(item1), item1.isspace())#só espaços
print('{} É um numero?'.format(item1),item1.isnumeric())#só tem numeros
print('{} É alfabético?'.format(item1),item1.isalpha())#alfabético
print('{} É alfanumerico?'.format(item1),item1.isnumeric())#alfanumerico
print('{} Está em maiúscula?'.format(item1) ,item1.isupper())#está em maiusculos
print('{} Éstá em minuscula?' .format(item1), item1.islower())#está em minusculas
print('{} Está capitalizada?' .format(item1), item1.istitle())#identifica se a primeira letra é maiuscula

