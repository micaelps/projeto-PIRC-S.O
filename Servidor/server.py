import socket
import threading
from Controller.Controller import *

def threaded(c): 
	while True: 
		data = c.recv(1024)
		dataString = data.decode()
		if not data: 
			print('Bye') 
			break
		retorno = roteador(dataString)
		# retorno = busca(data.decode())
		c.send(retorno.encode())
	c.close() 

def Main(): 
	host = "" 
	port = 5000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to port", port) 

	s.listen(100) 
	print("socket is listening") 

	while True: 
		c, addr = s.accept()  
		print('Connected to :', addr[0], ':', addr[1]) 
		my_thread = threading.Thread(target=threaded, args=(c,))
		my_thread.setDaemon(True)
		my_thread.start()
	s.close() 

if __name__ == '__main__': 
	Main() 

