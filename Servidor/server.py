import socket
import threading
from Controller.Controller import *

def threaded(c):
	while True: 
		data = c.recv(1024)
		dataString = data.decode()
		if not data: 
			print('Cliente desconectado') 
			break
		retorno = roteador(dataString)
		c.send(retorno.encode())
	c.close() 

def Main(): 
	host = "" 
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("Conectado na porta: ", port) 

	s.listen(100) 
	print("O socket está ouvindo") 

	while True: 
		c, addr = s.accept()  
		print('Conectado à:', addr[0], ':', addr[1]) 
		my_thread = threading.Thread(target=threaded, args=(c,))
		my_thread.setDaemon(True)
		my_thread.start()

if __name__ == '__main__': 
	Main() 

