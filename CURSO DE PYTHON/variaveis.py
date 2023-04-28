import os

os.system('cls || clear')
#Exercício 01
#Declarar variáveis:
nome = 'André'
sobrenome = 'Barros'
idade = 19
data_nascimento = 2023 - idade
altura = 1.80
maioridade = idade >= 18
#Printar Variáveis:
print('nome:', nome)
print('sobrenome:', sobrenome)
print('idade:', idade)
print('D/nascimento:', data_nascimento)
print('Altura:', altura)
print('Tem a maioridade?', maioridade)

#repetição através de divisão 
print( 4 * 'a')

#criando imc format (formatação é o f ao lado da variável) *f-strings*
linha_1 = f'nome:{nome} sobrenome: {sobrenome}'

print(linha_1)

#Função FORMAT
a='A'
b='B'
c=1.1
string = 'a={} b={} c={}'

formato = string.format(a, b, c)

print(formato)

linha01 = '{0} {1} {2}'

#fazendo format de cabeça

printando_format = linha01.format(
    nome, sobrenome, idade
    )

print(printando_format)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))

nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))


