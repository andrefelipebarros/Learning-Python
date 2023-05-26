import os 
'''
Novamente usarei o método while para estudo.

'''
os.system("CLS || CLEAR")

frase = 'Minecraft é muito bom,'\
'Minecraft é formiudável,'\
'Se tu não gosta vai tomar no cu.'

print(frase.lower().count('minecraft')) 
# .lower() deixa toda a frase em minusculo, 
# para ser melhor usado na busca atraves do .count()

i = 0

while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)

    print(letra_atual, quantas_vezes_letra_apareceu)

    i += 1