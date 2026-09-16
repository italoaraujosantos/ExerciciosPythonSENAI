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

    def __str__(self):
        return (f"\t Conta Bancária \n"
                f"\t Tipo: {self.tipo} \n"
                f"\t Número: {self.numero} \n "
                f"\t Saldo: {self.saldo}")