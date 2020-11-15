from Models.Conta import Conta
from Services.ContaService import ContaService


contaService = ContaService()

class ContaController:
  def __init__(self, entidade, router):
    self.entidade = entidade
    self.router = router

    if(router=='1'):
      contaService.criar(self.entidade)

    if(router=='2'):
      contaService.depositar()

    if(router=='3'):
      contaService.sacar()

    
  