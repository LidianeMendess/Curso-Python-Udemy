"""
Calculadora com while
"""
while True:
    numero_1 = input('Digite  o primeiro número: ')
    numero_2 = input('Digite  o segundo número: ')
    operador = input('Digite o operador(+-/*): ')

    numeros_validos=None

    try:
        numero1_float=float(numero_1)
        numero2_float=float(numero_2)
        numeros_validos=True
    except:
        numeros_validos=None
    if numeros_validos is None:
        print('Um ou ambos números digitados é inválido.')
        continue

    operadores_permitidos ='+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue
    
    if operador=='+':
        print (f'{numero1_float}+{numero2_float}=',numero1_float+numero2_float)
    elif operador=='-':
        print(f'{numero1_float}-{numero2_float}=',numero1_float-numero2_float)
    elif operador=='/':
        print(f'{numero1_float}/{numero2_float}=',numero1_float/numero2_float)
    elif operador=='*':
        print(f'{numero1_float}*{numero2_float}=',numero1_float*numero2_float)
    else:
        print('Você não deveria ter chegado até aqui!')


        

    sair=input('Quer sair? [s]im').lower().startswith('s')

    if sair is True:
        break
