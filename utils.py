import sys
import json

def mostrarOperacoes():
  print('''
    1) Abrir conta.
    2) Depósito
    3) Saldo
    4) Saque
    5) Encerrar consulta\n
    ''')
  operacao = int(input('Digite o número correspondente a opção desejada: '))
  
  return operacao



def escolherOperacao(operacao):
  print('Você digitou ', operacao)
  while True:
    if operacao == 1: #Abrir conta.
      nome = input('Digite seu nome: ')
      senha = int(input('Digite sua senha: '))

      # dado = str(nome) + ',' + str(senha)
      dado = json.dumps({"nome": nome, "senha": senha})
      return dado

    elif operacao == 2: # Depósito
      conta = int(input('Digite o número da conta: '))
      senha = int(input('Digite sua senha: '))
      deposito = float(input('Digite o valor: '))

      # dado = str(conta) + ',' + str(senha) + ',' + str(deposito)
      dado = json.dumps({"conta": conta, "senha": senha, "deposito": deposito})
      return dado

    elif operacao == 3: # Saldo
      conta = int(input('Digite o número da conta: '))
      senha = int(input('Digite sua senha: '))

      # dado = str(conta) + ',' + str(senha)
      dado = json.dumps({"conta": conta, "senha": senha})
      return dado

    elif operacao == 4: # Saque
      conta = int(input('Digite o número da conta: '))
      senha = int(input('Digite sua senha: '))
      saque = float(input('Digite o valor: '))
      
      # dado = str(conta) + ',' + str(senha) + ',' + str(saque)
      dado = json.dumps({"conta": conta, "senha": senha, "saque": saque})
      return dado

    elif operacao == 5: # Encerrar consulta
      sys.exit(0)
      print('Consulta encerrada')
      break
    else:
      print('Número de operação não existe\n')
      escolherOperacao(operacao)

