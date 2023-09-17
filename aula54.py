import os
lista=[]

while True:
    entrada=input('Selecione uma opção [i]nserir [a]pagar [l]istar:')
    if entrada=='i':
        os.system('cls')
        adicionar=input('Valor:')
        lista.append(adicionar)
    elif entrada=='a':
        apagar_str=input('Qual indice deseja apagar?')
        try:
            apagar=int(apagar_str)
            del lista[apagar]
        except:
            print('Não foi possível apagar este índice')
    elif entrada=='l':
         os.system('cls')
         for i, valor in enumerate (lista):
            print(i, valor)
    else:
        print('Digite uma opção válida.')

