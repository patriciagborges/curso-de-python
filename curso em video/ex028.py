#Crie um jogo que o computador gere um numero de 0 a 5
#e caso o usuário acerte ele escreva: Parabens! Você conseguiu
#caso contrario escreva: "computador ganhou"

jogador = int(input('Chute um numero inteiro de 0 a 5'))
from random import randint
computador = randint(0,5)
print(computador)
if jogador == computador:
    print("Parabéns! Você conseguiu!")
else:
    print('Computador ganhou')


