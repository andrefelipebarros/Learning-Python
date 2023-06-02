import os

#TESTANDO BARRA INVERTIDA KKKKK Muito tosco
os.system \
    ("CLS || CLEAR")

"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

#VARIÁVEL NORMAL
velocidade = 61  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

#SE UTILIZA PARA A VARIÁVEL 'MAIUSCULO' 
#SOMENTE QUANDO FOR ALGO QUE NÃO MUDE
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print("Velocidade passou a do radar 01.\n")

# o barra invertida "\" faz uma 
# quebra de linha(continuacao do código ABAIXO)
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and \
        velocidade > RADAR_1:
    print('carro multado em radar 1\n')

#podemos ver que o uso do método acima deixou o código bastante
#poluido, poderemos fazer o seguinte...

#desenvolvi a variável para armazenar o primeiro if e else criado
vel_carro_pass_radar_1 = velocidade > RADAR_1 #deixando o código mais legível

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)

carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

#Em seguida somente printar as variáveis na tela:

#prequiça de escrever.
