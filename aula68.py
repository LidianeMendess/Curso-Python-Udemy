"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x=5

def funcao_1():
    x=20
    print(x)
        
    def funcao_2():
        x=30
        print(x)

    outra_funcao()

print(x)
funcao_1()

