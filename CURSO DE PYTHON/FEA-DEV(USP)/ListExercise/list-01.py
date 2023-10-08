#QUESTÃO 0
#Todo programador deve saber apenas uma coisa: Pedir para o Python escrever "Hello, World" Vamos testar se você já pode ser nomeado como um programador???

#seu código começa aqui
print("Hello, World")

#E se eu te pedir para criar um código que tenha como OUTPUT (termo comumente usado na programação e na computação em geral para se referir à saída de um programa ou processo) o seu número favorito? Como seria?
#seu código começa aqui
meu_numero_favorito = 2
print("Meu número favorito é:", meu_numero_favorito)

'''QUESTÃO 1
Você está fazendo um pedido no Starbucks e na hora da compra pedem o seu nome completo para te chamarem quando seu pedido estiver pronto. Entretanto a moça do caixa anota somente o seu primeiro nome. Só depois de ter visto que haviam muitas pessoas na fila com o mesmo nome que o seu, ela te pergunta somente o seu sobrenome.

Na hora de entrega do seu pedido, como o atendente chamará por você??

Agora, sua tarefa é criar um código em Python no Jupyter Notebook para combinar o seu primeiro nome e seu sobrenome e exibir o nome completo que o atendente usará para chamar você quando seu pedido estiver pronto.

Seu código deve fazer o seguinte:

Declare duas variáveis: primeiro_nome e sobrenome. Atribua um valor ao primeiro_nome representando o primeiro nome que a atendente anotou. Atribua um valor ao sobrenome representando o sobrenome que a atendente solicitou posteriormente. Use sua habilidade em Python para combinar essas duas partes e criar o nome completo. Exiba o nome completo no Jupyter Notebook.

Desafio aceito? Agora, você está pronto para criar o código que garantirá que o atendente do Starbucks chame você corretamente quando seu pedido estiver pronto! ☕🪄'''

#seu código começa aqui
nome = "André Felipe"
sobrenome = "Nogueira"

nome_completo = nome + " " + sobrenome

print("Nome completo que o atendente vai usar: " + nome_completo)

"""QUESTÃO 2
Imagine que você é um professor de Matemática para crianças do ensino fundamental e um aluno curioso te pergunta:

"Professor, quanto é 13 + 15 + 16 + 6?"

Você, é claro, não quer parecer contar nos dedos por baixo da mesa para uma pergunta tão simples. Então, você decide mostrar toda a sua sabedoria tecnológica e recorre ao Python para dar a resposta instantaneamente.

Como deve ser o código para chegar ao resultado?"""

# seu código começa aqui
calculo = 13 + 15 + 16 + 6

print(calculo)

'''
QUESTÃO 3
Você é um detetive de palavras, conhecido por desvendar enigmas usando manipulação de texto. Hoje, você enfrenta um novo mistério envolvendo uma mensagem secreta. Sua missão é decifrar essa mensagem usando operações com texto em Python.

Mistério da Mensagem Secreta:

Você recebeu a seguinte mensagem secreta:
#Mistério: @s4b@d0 3n0c0nd3 3st@ m3n$@g3m. P0d3r14$ d3c1fr@-l@?

A mensagem parece confusa, mas você sabe que ela contém informações importantes. Aqui estão as etapas que você deve seguir para decifrar a mensagem:

Crie uma variável chamada mensagem e atribua a ela a mensagem secreta fornecida acima. Use operações de texto em Python para limpar a mensagem, removendo todos os caracteres especiais, números e espaços em branco.

Converta a mensagem resultante para letras minúsculas.

Agora que a mensagem está limpa, você pode decifrá-la? A mensagem secreta pode conter uma pista importante!

Crie um código em Python no Jupyter Notebook para realizar essas etapas e revelar o que está por trás desse mistério! 🕵️‍♂️🔍
'''

#seu código começa aqui

#Tenho que usar o replace( trocar, trocado)

mensagem = "@s4b@d0 3n0c0nd3 3st@ m3n$@g3m. P0d3r14$ d3c1fr@-l@?"

mensagem = mensagem.replace( "@" , "a")
mensagem = mensagem.replace( "3" , "e")
mensagem = mensagem.replace( "$" , "s")
mensagem = mensagem.replace( "0" , "o")
mensagem = mensagem.replace( "1" , "i")
mensagem = mensagem.replace( "4" , "a")

print(mensagem)

'''QUESTÃO 4
Você acaba de ingressar no curso de Python do FEA.dev e decide iniciar sua própria consultoria. Parabéns!!! Você logo recebe seu primeiro cliente, a pizzaria do bairro. Ela tem um grande objetivo em mente: desbancar a grande indústria de pizza Baralho's e Pizza Wut. Para isso, vai recorrer à tecnologia em seus processos.

Sua primeira função é criar um sistema que recebe o valor de cada venda de pizza e bebida e imprima o valor final.'''

#seu código começa aqui

valor_pizza = 20.00
valor_bebida = 5.00

valor_total = valor_pizza + valor_bebida

print("O valor total da venda é: R$ {}".format(valor_total))

'''QUESTÃO 5
Excelente! A clientela adorou o programa de fidelidade. Feito isto, chegou a hora de olhar para os processos internos. A ideia é automatizar a lista de compra da semana, antes feita no papel.

a) O chef de cozinha resolveu aprender uma receita que utiliza a fermentação natural, de forma que a pizza fique mais próxima da tradicional italiana. Feito isso, não há mais necessidade de utilizar leite, ovos e fermento biológico para a receita. Retire-os da lista de compras e em seguida, adicione Levain e Açúcar, ingredientes da fermentação natural. Imprima a nova lista.'''

compras = ['Farinha de Trigo', 'Ovos', 'Fermento Biológico', 'Leite', 'Calabresa', 'Milho',
           'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo']
##### Seu código começa aqui
compras.remove("Leite")
compras.remove("Ovos")
compras.remove("Fermento Biológico")

compras.append("Levain")
compras.append("Açucar")

print(compras)

'''b) Enquanto você estava com o computador ligado, um hacker da pizzaria rival do bairro resolveu atacar sua lista de compras invertendo alguns dos itens, como se vê abaixo:

Conserte os valores que foram adulterados e imprima a lista corrigida.'''

sarpmoc = ['ogirT ed ahniraF', 'Calabresa', 'Milho', 'Champignon', 'etamoT ed ohloM', 'Frango',
           'Requeijão', 'Lombo', 'niaveL', 'Açúcar']
#### Seu código começa aqui
compras = sarpmoc

indice = compras.index("ogirT ed ahniraF")
indice2 = compras.index("etamoT ed ohloM")
indice3 = compras.index("niaveL")

invertido = compras[indice][::-1]
invertido2 = compras[indice2][::-1]
invertido3 = compras[indice3][::-1]

compras[indice] = invertido
compras[indice2] = invertido2
compras[indice3] = invertido3

print(compras)

'''c) Após esse duro golpe, você percebe que é necessário guardar as informações importantes em uma estrutura de dados que seja mais segura (isto é, que não seja mutável). Converta a lista de compras para uma estrutura com estas características e imprima o tipo da variável.   Dica: Utilize a função type() para obter o tipo da variável'''

#seu código começa aqui

compras = tuple(compras)

print(type(compras))

'''QUESTÃO 6
Empresas modernas se importam com ESG (Environmental, Social and Governance). A pizzaria do bairro não seria diferente, e sua missão é auxiliar a empresa a reduzir as emissões de lixo em sua operação.  

ac137a44f5f8cd3c6126fc8ff8c24fff.jpg

O primeiro passo será tornar o panfleto digital, de forma que seja enviado pelas redes sociais e não precise ser impresso e consequentemente descartável. Para demonstrar essa funcionalidade ao dono, você deve criar um exemplo de panfleto que contenha os sabores de pizza salgadas e doces (separados), tipos de bebida e adicionais, conforme os valores a seguir:

Pizzas salgadas: Calabresa, Portuguesa, Mussarela e Pepperoni;
Pizzas doces: Prestígio, Chocolate e Doce de Leite;
Bebidas: Guaraná, Cola, Suco de Laranja e Suco de Uva;
Adicionais: Bacon, Requeijão, Milho e Azeitona
Imprima o panfleto final.'''

### Seu código começa aqui

pizzas_salgadas = ["Calabresa", "Portuguesa", "Mussarela", "Pepperoni"]
pizzas_doces = ["Prestígio", "Chocolate", "Doce de Leite"]
bebidas = ["Guaraná", "Cola", "Suco de Laranja", "Suco de Uva"]
adicionais = ["Bacon", "Requeijão", "Milho", "Azeitona"]

print("---- Panfleto Digital ----")
print("Pizzas Salgadas:")
print("\n".join(pizzas_salgadas))

print("\nPizzas Doces:")
print("\n".join(pizzas_doces))

print("\nBebidas:")
print("\n".join(bebidas))

print("\nAdicionais:")
print("\n".join(adicionais))

'''DESAFIO
Sucesso! A pizzaria do bairro tornou-se uma multinacional que engoliu todas as concorrentes. Querendo crescer ainda mais, o dono sugere um novo recurso: criar sua própria pizza. Para isso, temos um dicionário com todos os ingredientes e seus respectivos preços. A pizzaria recebeu os seguintes pedidos:

1: Massa sem glúten, molho barbecue, frango, pimentão e tomate
2: Massa tradicional, molho de tomate, atum, mussarela, azeitona, cebola, pimentão, tomate e borda com queijo
3: Massa integral, molho bechamel, cebola, pimentão, tomate, frango e borda com requeijão
Imprima uma lista com todos os itens do pedido e seu preço final que será retornado ao cliente. Armazene o valor das vendas de forma que não seja possível alterar seus valores e imprima.'''