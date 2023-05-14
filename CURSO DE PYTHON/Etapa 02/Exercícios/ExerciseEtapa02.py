import os

os.system("CLS || CLEAR")

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# Primeiro método
try:
    numero = input("Digite um número: ")

    numero_int = float(numero)
    
    par_impar = numero_int % 2 == 0

    if par_impar:
        print('par.')
    else:
        print('impar')
    
except:
    print("Você não informou um número.")

# Outro método:
entrada = input('Digite um número: ')
# usando o método 'isdigit()'
if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0

    if par_impar:
        print('par.')
    else:
        print('impar')

else:
    print('não é um número')


# Horário 

hora = input('Digite a hora: ')

hora_int = int(hora)

if hora_int < 12:
    print('BOM DIA! O SOL JÁ NASCEU LÁ NA FAZENDINHA')
elif hora_int > 17:
    print('BOA TARDE! VADIAA')
elif hora_int > 18:
    print('Boa noite... zZ*Z*')