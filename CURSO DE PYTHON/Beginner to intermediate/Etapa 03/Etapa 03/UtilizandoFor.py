import os

os.system('cls || clear')

frase = "Python"
novo_texto = ''

for letra in frase:
    novo_texto += f'*{letra}' 
    print(letra)
print(novo_texto + "*")

###
print('\n')
# Utilizando Range:
''' For + Range 
    range -> range(start, stop, step) #Range é perfeito, da pra mexer nele e procurar números pares por exemplo range(0, 100, 2)
'''

#Lembre-se range(start, stop, step)

numeros = range(0, 81, 8) #tabuada de 8

print(numeros)

for numero in numeros:
    print(numero)

#Estou pensando em usar o Jupyter para anotar e deixar mais organizadinho.