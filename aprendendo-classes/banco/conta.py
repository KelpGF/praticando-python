from datetime import datetime

from extrato import Extrato


class Conta:

  def __init__(self, clientes: str, numero: int, saldo: float = 0):
    self.clientes = clientes
    self.numero = numero
    self.saldo = saldo
    self.data_abertura = datetime.today()
    self.extrato = Extrato()

  def mensagem(self, tipo: str, valor: float):
    self.extrato.transacoes.append([tipo.upper(), valor, "Data", datetime.today()])

  def depositar(self, valor: float):
    self.saldo += valor
    self.mensagem('Depósito', valor)

  def sacar(self, valor: float):
    if (valor > self.saldo):
      return False
    else: 
      self.saldo -= valor
      self.mensagem('saque', valor)

  def transferir(self, valor: float):
    if (valor > self.saldo):
      return False
    else: 
      self.saldo -= valor
      self.mensagem('TransferênCIA', valor)
      return True

  def exibirSaldo(self): 
    print(f"Saldo Atual: R$ {self.saldo:10.2f}")