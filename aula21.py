entrada=input('[E]ntrar [S]air:  ')
senha=input('Senha: ')

senha_permitida = '123456'

if entrada =='E' and senha==senha_permitida:
    print('Entrar')
else:
    print('Sair')