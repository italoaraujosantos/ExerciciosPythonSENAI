class conta:
    def __init__(self, tipo, numero, saldo):
        self.tipo = tipo
        self.numero = numero
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def transferir(self, valor):
        self.saldo -= valor

