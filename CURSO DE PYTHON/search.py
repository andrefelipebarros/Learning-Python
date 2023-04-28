import os
os.system("cls || clear")

#método usando "in" or "in not"
#Código bem bobinho para aprender a função "in"
nome = 'André'
encontrar = input('Digite uma letra:')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em nome')
