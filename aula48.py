"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
 append, insert, pop, del, clear, extend, +
Create, Read, Update, Delete
criar, ler, alterar, apagar=lista[i] (CRUD)
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len)
# print(bool([]))  # falsy
# print(lista, type(lista))

#        0    1      2              3    4
#       -5   -4     -3             -2   -1
"""
lista = ['LIDIANE', 1.68, 26, True, []]
lista[-3] = '27'
print(lista)
print(lista[2], type(lista[2]))
lista.append(200)
print(lista)
#ultimo_valor=lista.pop()
#print('removido: ', ultimo_valor)
lista.insert(0, 'Aries')
print(lista)
lista.pop(0)
print(lista)

lista_a=[1,2,3]
lista_b=[4,5,6]
lista_c=lista_a+lista_b
print(lista_c)
lista_a.extend(lista_b)
print(lista_a)
"""

lista_a=['Lidiane','xico']
lista_b= lista_a.copy()
lista_a[0]='Margarida'
print(lista_a)


