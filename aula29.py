"""
Introdução ao try/except
try-> tentar executar o código
except-> ocorreu um erro ao tentar executar
"""
numero=input('Vou dobrar o número que vc digitar: ')

if numero.isdigit():

    numero_int=float(numero)
    print(f'O dobro de {numero} é {numero_int*2}')
else:
    print('Isto não é um número')