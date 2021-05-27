# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A
# classe deve possuir os seguintes atributos: número da conta, nome do correntista e
# saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor,
# saldo é opcional, com valor default zero e os demais atributos são obrigatórios.

class ContaCorrente:
    def __init__(self, numeroConta, nomeCorrentista, saldo):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, nome):
        self.nome = nome
    
    def deposito(self, valor):
        self.saldo += valor
    
    def saque(self, valor):
        if(self.saldo >= valor):
            self.saldo -= valor

conta1 = ContaCorrente(2004, 'Debora', 100)
conta1.alterarNome('Debora Rosa')
print(conta1.nome)
conta1.deposito(50)
print(conta1.saldo)
conta1.saque(60)
print(conta1.saldo)
