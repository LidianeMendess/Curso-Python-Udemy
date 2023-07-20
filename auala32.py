"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero=input('Digite um número inteiro: ')

if numero.isdigit():
    numero_inteiro=int(numero)
    if numero_inteiro%2==0:
        print(f'O número {numero} é par')
    else: 
        print(f' O número {numero} é impar')
else:
    print('Número digitado não é inteiro')




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação coletiva. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual=input('Digite que horas são: ')

try:
    hora_inteira= int(hora_atual)
    if hora_inteira<=11 and hora_inteira>=0:
        print('Bom dia!')
    elif hora_inteira>=12 and hora_inteira<=17:
        print('Boa tarde!')
    elif hora_inteira>=18 and hora_inteira<=23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor digite números inteiros.')
    

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""



primeiro_nome=input('Digite seu primeiro nome:' )

tamanho_nome=(len(primeiro_nome))

if tamanho_nome>1:
    if tamanho_nome<=4:
        print('Seu nome é curto!')
    elif tamanho_nome>=5 and tamanho_nome<=6:
        print('seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')

    