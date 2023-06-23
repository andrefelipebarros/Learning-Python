word = "minecraft"

word_len = len(word)

contador = 0

result = ''

while contador < word_len:
    #com print:
    print('*'+ word[contador])
    #colocando em uma variável:
    result += '*' + word[contador]
    # o "+" serve para adicionar mais uma letra ao resultado
    contador += 1

print(result)