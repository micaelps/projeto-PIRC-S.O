from Models.Conta import Conta
from Services.ContaService import ContaService


contaService = ContaService()

class ContaController:
  def __init__(self,payload):
    self.router = payload[0]

    if(self.router=='1'):
      print("criar")
      #contaService.criar(self.entidade)

    if(self.router=='2'):
      contaService.depositar()

    if(self.router=='3'):
      contaService.sacar()

    
  