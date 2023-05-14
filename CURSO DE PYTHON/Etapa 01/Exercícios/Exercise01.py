import os

os.system("cls || clear")

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input(str("Digite seu nome: "))
#Método avançado de erro
'''while len(nome) == 0:
    print("Erro: você não informou um nome válido.")
    nome = input("Digite seu nome novamente: ")'''

idade = input("Digite sua idade: ")
#Método avançado de erro
'''while len(idade) == 0:
    print("Erro: você não informou uma idade válida.")
    idade = input("Digite sua idade novamente: ")'''

#Como deveria ser feito:

if nome and idade:
    print(f'\nSeu nome é {nome}\n')
    print(f'Seu nome invertido é {nome[::-1]}\n')

    #Gerando variável para espaço e fazer a troca dentro de print
    espaco = ' '

    if espaco in nome:
     espaco = 'True'
    else:
        espaco = 'False'

    print(f'Seu nome contém espaços: {espaco}\n')

    #Primeiro Método Len:
    letra = len(nome)

    print(f'{nome} contém {letra} letras.\n')

    #Segundo Método Len:
    print(f'{nome} contém {len(nome)} letras.\n')

    # '0' é correspondente a primeira letra
    print(f'primeira letra do seu nome: {nome[0]}\n')
    # '-1' ele faz com que inverta a string assim pegando a última letra
    print(f'última letra do seu nome: {nome[-1]}\n')
else:
   print('Perdão, você deixou campos vazios.')

#esse método if e else não contém while, devido a isso o 
#código encerra por não informar todos os campos