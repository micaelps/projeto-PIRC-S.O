import sys
from datetime import datetime

def mostrarOperacoes():
  print('''
    1) Procurar música por trecho.\n
    ''')
  operacao = int(input('Digite o número correspondente a opção desejada: '))
  
  return operacao



def escolherOperacao(operacao):
  print('Você digitou ', operacao)
  while True:
    if operacao == 1: #Procurar música por trecho.
      trecho = input('Digite o trecho: ')

      # dado = str(nome) + ',' + str(senha)
      dado = f'/ENVIO/10/{trecho}/{len(trecho)}/{datetime.now()}'
      return dado
      '''
      MODO: ENVIO, RETORNO, ERRO
      CODIGO: 10, 20, 30
      DADO: STRING TEXTO
      '''
    elif operacao == 2: # Encerrar consulta
      print('Consulta encerrada')
      sys.exit(0)
      break
    else:
      print('Número de operação não existe\n')
      escolherOperacao(operacao)

