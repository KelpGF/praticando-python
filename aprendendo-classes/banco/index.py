from cliente import Cliente
from conta import Conta

cliente1 = Cliente('000.111.222-33', 'Kelv', 'Rua tal n 1')
cliente2 = Cliente('444.111.222-33', 'Plek', 'Rua tal n 2')

conta1= Conta([cliente1, cliente2], 1)

conta1.exibirSaldo()
conta1.depositar(1500)
conta1.sacar(500)
conta1.exibirSaldo()


conta1.extrato.exibirExtrato()