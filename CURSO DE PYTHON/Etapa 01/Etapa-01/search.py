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


#resposta será 1 nas duas.
variavel_a = 0 or 1
variavel_b = 1 or 0
print(variavel_a, variavel_a)