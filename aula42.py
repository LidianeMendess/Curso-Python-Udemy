frase='O python é uma linguagem de programação'\
    'multiprogramada'\
    'Python foi criada por Guido Van Rossum.'



i=0
qtd_apareceu_mais_vezes=0
letra_apareceu_mais_vezes=''

while i<len(frase):
    letra_atual=frase[i]

    if letra_atual==' ':
        i+=1
        continue

    qtas_vzs_letra_apareceu_atual=frase.count(letra_atual)

    if qtd_apareceu_mais_vezes<qtas_vzs_letra_apareceu_atual:
        qtd_apareceu_mais_vezes=qtas_vzs_letra_apareceu_atual
        letra_apareceu_mais_vezes=letra_atual

    i+=1

print ('A letra que apareceu mais vezes foi'
    f' "{letra_apareceu_mais_vezes}" que apareceu '
    f'{qtd_apareceu_mais_vezes}X' )
