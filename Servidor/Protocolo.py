class Protocolo:
    '''
    modo: ENVIO, RETORNO, ERRO
    codigo: 13, 19, 27
    dado: string
    tamanho_dado: len(dado)
    datetime: datetime 
    '''
    def __init__(self, modo, codigo, dado, tamanho_dado, datetime):
        self.modo = modo
        self.codigo = codigo
        self.dado = dado
        self.tamanho_dado = tamanho_dado
        self.datetime = datetime

    def instanciaPorString(self, string):
        string = string.split('/')
        return Protocolo(string[1],string[2],string[3],string[4],string[5])

    def stringPorInstancia(self):
        return f'/{self.modo}/{self.codigo}/{self.dado}/{self.tamanho_dado}/{self.datetime}/'