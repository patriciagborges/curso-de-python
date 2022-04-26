#receber o nome de 4 alunos e
# fazer um sorteio de um dos nomes;
import random
aluno1 = input('digite o nome do primeiro aluno')
aluno2 = input('digite o nome do segundo aluno')
aluno3 = input('digite o nome do terceiro aluno')
aluno4 = input('digite o nome do quarto aluno')
alunos = [aluno1, aluno2, aluno3, aluno4]
aluno_escolhido = random.choice(alunos)
print(aluno_escolhido)


