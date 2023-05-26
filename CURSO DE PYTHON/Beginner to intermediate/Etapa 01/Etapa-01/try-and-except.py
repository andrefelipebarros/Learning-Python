import os

os.system("cls || clear")

"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""
#variável nomeada com str devido o 'Input' sempre gerar uma string
numero_str = input(
    'Vou dobrar o número que vc digitar. Digite: '
)

try:
    #transformando string em float:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')