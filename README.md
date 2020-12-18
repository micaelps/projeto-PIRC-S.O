# projeto-PIRC-S.O
Alunos:
* Micael Pinheiro da Silva
* Anderson Lima

DOCUMENTAÇÃO:  

- MODOS: 

  - ENVIO -  quando cliente envia algo para o servidor. 
  - RETORNO - quando o servidor recebe algo do cliente e retorna uma resposta ao cliente. 
  - ERRO - quando há parâmetros insuficiente.  ver validação de dado  

- CÓDIGOS: 

	- 13 - código de envio 
	- 19 - código de retorno
	- 27 - código de erro

- DADO  - string usada para pesquisa 

- TAMANHO DO DADO  - tamanho do dado

- DATA -  o protocolo oferece hora e data de envio tanto do servidor, como do cliente.  

o servidor retornará algo se o envio estiver dentro do padrão, caso contrário retornará erro.

Exemplo de envio:  /ENVIO/13/simples/7/2020-12-18 09:46:43.452828
------------

REQUISITOS:

- python 3.6 ou superior
- instalar pip
- instalar a biblioteca requests (pip install requests)

NO LINUX: 
- firefox
- geckodriver com versao equivalente ao firefox (https://github.com/mozilla/geckodriver/releases)
- mover o geckodriver para /usr/local/bin e dar permissão de execução
- instalar selenium (pip install selenium)


