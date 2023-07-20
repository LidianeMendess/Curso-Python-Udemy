"""
CONSTANTE= "variáveis" que não vão mudar
Muitas  condições no mesmo if (ruim)
    <-contagem de complexidade (ruim)
"""
velocidade= 50 #velocidade atual do carro
local_carro= 100 #local em que o carro está na estrada

RADAR_1=60 #velocidade máxima do radar 1
LOCAL_1= 100 #local onde o radar 1 está
RADAR_RANGE= 1 #A distância onde o radar pega

carro_passou_da_velocidade=velocidade>RADAR_1
carro_passou_radar1=local_carro>=(LOCAL_1-RADAR_RANGE) and \
        local_carro<=(LOCAL_1+RADAR_RANGE) 
carro_multado_radar1= carro_passou_da_velocidade and carro_passou_radar1
    
if carro_passou_da_velocidade:
    print('Velocidade ddo carro passou da permitida do radar 1')
if carro_passou_radar1:
    print('carro passou no radar 1')
if carro_multado_radar1:
    print('Carro multado pelo radar 1')