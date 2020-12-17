import sys
from datetime import datetime

def mostrarOperacoes():
  print('''
    1) Procurar música por trecho.
    2) Encerrar consulta\n
    ''')
  operacao = input('Digite o número correspondente a opção desejada: ')
  
  return operacao



def escolherOperacao(operacao):
  print('Você digitou ', operacao)
  while True:
    if operacao == '1': #Procurar música por trecho.
      trecho = input('Digite o trecho: ')

      # dado = str(nome) + ',' + str(senha)
      dado = f'/ENVIO/13/{trecho}/{len(trecho)}/{datetime.now()}'
      return dado
      '''
      MODO: ENVIO, RETORNO, ERRO
      CODIGO: 10, 20, 30
      DADO: STRING TEXTO
      '''
    elif operacao == '2': # Encerrar consulta
      print('Consulta encerrada')
      sys.exit(0)
      break
    else:
      print('Número de operação não existe\n')
      escolherOperacao(operacao)


def pegarLista(resposta):
  resposta = resposta.split('[')[1]
  resposta = resposta.split(']')[0]
  lista = resposta.split("',")
  # print(lista)
  return lista


def mostrarMusicas(resposta):
  lista = pegarLista(resposta)
  if lista:
    for i in range(len(lista)):
      print(f"[{i+1}] - {lista[i].split(' - ')[0]} - {lista[i].split(' - ')[1]}")
  
  operacao = int(input('\nDigite o número correspondente a opção desejada: '))
  return operacao
    

def pegarLink(resposta):
  lista = pegarLista(resposta)
  urls = []

  for i in range(len(lista)):
    rota = lista[i].split(' - ')[2]
    rota = rota.split(': ')

    url = 'https://www.vagalume.com.br'+rota[1]
    urls.append(url)
  return urls


def escolherMusica(operacao, lista):
  print('Você digitou ', operacao + 1, '\n')
  if operacao > len(pegarLink(lista)) or operacao < 0:
    print('Opção inválida')
  else:
    texto = pegarLink(lista)[operacao]
    texto = texto.replace("'", "")
    # print(texto)
    return texto