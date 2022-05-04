#Crie um programa que leia o nome de uma cidade e diga
#se ela começa com a palavra "santo"
cidade = input('Em qual cidade você nasceu?').strip()
print(cidade[:5].upper() == 'SANTO')
