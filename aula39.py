nome=input('Digite seu nome: ')
tamanho_nome=len(nome)
indice=0
novo_nome=''

while indice<tamanho_nome:
    letra=nome[indice]
    novo_nome+=f'*{letra}'
    indice+=1

    
    
print(novo_nome)












#print(tamanho_nome)