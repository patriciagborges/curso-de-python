#Manipulando texto
# 'cadeia de texto' = string
frase = 'curso em video python'
#indice = 0 a final do array

#Fatiamento:
#frase = 'Curso em video Python'
#print(frase[9]) #pega o valor dentro do indice 9
#print(frase[9:13])#pega o valor do indice 9 ao indice 13 (-1)
#print(frase[9:21])#pega o valor do indice 9 até o final da string
#print(frase[9:21:2])#pega o valor do indice 9 ao ultimo, pulando de 2 em 2
#print(frase[:5])#começa no indice 0 e vai até a posição 5 (-1)
#print(frase[15:])#começa pelo indice 15 e vai até o final da string
#print(frase[9::3])#começa no indice 9 e vai até o final pulando de 3 em 3

#Análise
#frase = 'Curso em video Python'
#print(len(frase))#Quantos caracteres tem a string frase
#print(frase.count('o'))
#print(frase.count('o',0,13))#Conta quantos 'o' tem do 0 ao 13 (-1)
#print(frase.find('deo'))#diz em qual posição essa frase começa
#print(frase.find('Android'))#retorna -1 caso não exista a palavra na frase
#print('Curso' in frase)#retorna verdadeiro ou falso

#Transformação
#frase = 'Curso em video Python'
#print(frase.replace('Python', 'Android')#substitui um valor por outro
#print(frase.upper())#transforma todos os itens em maiusculo
#print(frase.lower())#transforma todos os itens em minusculo
#print(frase.capitalize())#transforma tudo em minusculo e deixa somente a primeira letra da string em maiuscula
#print(frase.title())#transforma só a primeira letra de cada frase em maiusculas
#frase = 'Aprenda Pyhton'
#print(frase.strip())#retira os espaços vazios antes e depois da frase
#print(frase.rstrip())#retira os espaços vazios da direita
#print(frase.lstrip())#retira os espaços vazios da esquerda

#Divisão
#frase = 'Curso de Python'
#print(frase.split())#traz um novo array só com as palavras (vai dividir aonde tiver um espaço vazio)

#junção
#frase = 'Curso em video'
#print('_'.join(frase))#vai juntar tudo e vai usar o novo separador
# ''' imprime um texto grande de uma vez


