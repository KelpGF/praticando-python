class Extrato:
  def __init__(self):
    self.transacoes = []

  def exibirExtrato(self): 
    for p in self.transacoes:
      print(f"{p[0]:10s} {p[1]:10.2f} {p[2]:5s} {p[3].strftime('%d/%m/%y')}")