#!/usr/bin/env python3
import socket
import sys
from Menu.menu import *
from selenium import webdriver
import time



HOST = socket.gethostname()     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta

if len(sys.argv) > 1:
    HOST = sys.argv[1]

print('Servidor: ', (HOST, PORT))

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)

print('Para sair use CTRL+X\n')

while True:
    try:
        operacao = mostrarOperacoes()   
    except:
        break
    dado = escolherOperacao(operacao)
    tcp.send(str.encode(dado))
    dado = tcp.recv(1024)
    if not dado:
        break

    operacao = mostrarMusicas(dado.decode())
    site = escolherMusica(operacao-1, dado.decode())

    firefox = webdriver.Firefox()
    firefox.get(site)

    time.sleep(5)

    botao = firefox.find_element_by_xpath('//*[@class="vagaPlayAlpha"]')
    botao.click()

tcp.close()