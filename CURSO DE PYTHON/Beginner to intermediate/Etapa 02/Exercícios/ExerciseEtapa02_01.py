import os

os.system("CLS || CLEAR")

"""
Iterando strings com while
faça a string com while ficar assim:
'*L*u*i*z* *O*t*á*v*i*o'
"""
name = 'Luiz Otávio'
letra_toda = ''

contador = 0

while contador < len(name):
    letra = name[contador]
    letra_toda += f'*{letra}'
    contador += 1

print(letra_toda)