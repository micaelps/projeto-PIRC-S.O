import requests
from datetime import datetime

def busca(protocolo):
    protocolo_string = protocolo.stringPorInstancia()
    protocolo_separado = protocolo_string.split('/')
    retorno = []
    string = protocolo_separado[3]
    a = requests.get(f'https://api.vagalume.com.br/search.excerpt?q={string}&limit=5')
    a = a.json()['response']
    for i in a['docs']:
        retorno.append(f"{i['title']} - {i['band']} - URL: {i['url']}")
    return f'/OK/RETORNO/20/{str(retorno)}/{len(str(retorno))}/{datetime.now()}'