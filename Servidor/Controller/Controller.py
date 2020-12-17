from datetime import datetime
from Operacoes.Operacoes import *
from Protocolo import Protocolo

def roteador(dado):
    try:
        dado = dado.split('/')
        if dado[1] !='ENVIO':
            raise ValueError
        pedido = Protocolo(dado[1],dado[2], dado[3], dado[4], dado[5])
        return busca(pedido)
    except:
        return f'/ERRO/27///{datetime.now()}'
