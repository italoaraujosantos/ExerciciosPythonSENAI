
if __name__ == '__main__':
    conta1 = Conta("Conta Corrente", 46958-8, 9586.99)

    conta1.sacar(1000)
    conta1.transferir(5000)

    print(conta1.saldo)