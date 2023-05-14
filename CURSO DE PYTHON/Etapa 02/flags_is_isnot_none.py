"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None #não tem definição

if condicao: 
    #como a variavel "condicao" está false acima não é possível
    #fazer com que passou_no_if ser True
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

#testando se "passou_no_if" continua "None" ou não
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')

#utilizando is not

print(passou_no_if is not None) #informará se é false or true
print(passou_no_if is None) #True porque ela é None