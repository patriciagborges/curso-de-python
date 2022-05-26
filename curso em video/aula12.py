#Consições aninhadas
nome = str(input('escreva seu nome'))
if nome == 'gustavo':
    print('que nome bonito')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Nome popular')
else:
    print('boa tarde')
print('tenha um belo nome {}'.format(nome))