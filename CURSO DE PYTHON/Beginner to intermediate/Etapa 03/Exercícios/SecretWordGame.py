"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

os.system("CLS || CLEAR")

word_secret = "PerFumE"
word_secret = word_secret.lower()
palavras_acertadas = ''

#Gerar um loop com While
while True:
    letra_digit = input('Digite uma letra: ')

    os.system("CLS || CLEAR")

    if len(letra_digit) > 1:
        print("Informe apenas uma letra.")
        #continue faz o while reiniciar a operação
        continue

    if letra_digit in word_secret:
        print('Contém na palavra secreta.')
        #faz o acréscimo da letra na variável com acertos
        palavras_acertadas += letra_digit

    #Colocar if else dentro da ariável lista
    lista = ''
    #Primeiro faço a letra_secreta fazer a lista da palavra secreta
    for letra_secreta in word_secret:
        #crio um condição para que a cada vez que a lista tiver 
        #uma letra acertada ela print a letra secreta
        if letra_secreta in palavras_acertadas:
            lista += letra_secreta
            
        else:
        #caso a condição não contenha a palavra acertada entrará um asteristico
            lista += '*'
    print(lista)
        


    
