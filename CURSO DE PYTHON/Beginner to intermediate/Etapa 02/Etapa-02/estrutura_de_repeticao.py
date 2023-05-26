import os

os.system("CLS || CLEAR")
#Declarando Variável
condicao = True

#Estrutura de repetição while
while condicao:
    print("andando")
    break
# "break" FUNÇÃO RESPONSÁVEL POR QUEBRAR A REPETIÇÃ WHILE.

###

# GERANDO UM while com contador para não ser infinito:
print('Contador:')
contador = 0

while contador <= 10:
    print(contador)
    contador = contador + 1
    #Caso queira dar o número 11 coloque o print abaixo:
    #print(contador)

print("Fim while")

###

#USAR MÉTODO "continue"
contador_continue = 0

while contador_continue <= 10:
    
    #caso você queira acrescentar +1 poderá usar isso abaixo 
    #ao invés de repetir a variável:
    #usando o '+=' vocÊ pode usar também o de divisão '/=' 
    #multiplicação '*=' e etc.
    contador_continue += 1

    if contador_continue == 6:
        print('sumiu')    
        continue
    
    #ao acrescentar o print abaixo do if, ele sumirá
    #com o número 6 de acordo com o exemplo continue
    print(contador_continue)
