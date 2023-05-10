import os
os.system("cls||clear")

''' 
interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDE01234)
'''

nome = 'luiz'
preco = 100.22438713
variavel = '%s, o preço é R$%.2f' % (nome,preco)
print(variavel)