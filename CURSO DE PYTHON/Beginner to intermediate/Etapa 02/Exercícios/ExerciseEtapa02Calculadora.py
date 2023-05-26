import os


"""CALCULADORA COM WHILE (SERÁ EXECUTADO ATÉ USAR MÉTODO SAIR "break")"""

while True:
    os.system('CLS || CLEAR')
    n1 = input("First number: \n")
    n2 = input("Second number: \n")
    operador = input("Operador: [+, -, /, *] \n")
    #Gerando Boolenaa de Check
    numeros_validos = None
    operador_permitido = '+-/*' #por estar tudo junto, tenho que separar em uma len

    try:
        n1 = float(n1)
        n2 = float(n2)
        numeros_validos = True


    except:
        numeros_validos = None
        #Se números validos for "None" (is "None")
        if numeros_validos is None:
            print("Invalid Numbers.")
            #Continue é responsável por... 
            #retornar o While de onde estava.
            continue

        if operador not in operador_permitido:
            print("Operador inválido.")
            continue

        if len(operador) > 1:
            print("! Apenas um operador !")
            continue
        else:
            print("Não tem else.") #Não tem o porque ter um else aqui
    ###

    if operador == '+':
        print(f'{n1 + n2}') #or print(n1 + n2)
    if operador == '-':
        print(f'{n1 - n2}') #or print(n1 - n2)
    if operador == '/':
        print(f'{n1 / n2}') #or print(n1 / n2)
    if operador == '*':
        print(f'{n1 * n2}') #or print(n1 * n2)

    ###

    sair = input("Deseja Sair? [s]\n")
    # Função Lower responsável por transformar string
    # em letras minúsculas
    sair = sair.lower()

    #esse é um método porém existe outro abaixo
    #if sair == 's':
    #    break

    #Método utilizando um exemplo de Booleana
    sair = sair.startswith('s') #traduzindo para o português: 
    #start = começar swith = com...
    if sair is True:
        break
    #Poderia juntar todas essas funções através do input
    #sair = Input("Deseja Sair? [s]\n").lower().startswith('s')

    print(sair)
    