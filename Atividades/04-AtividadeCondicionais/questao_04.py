print("Saque Bancaria!")
saldoAtual = float(input("Informe o saldo atual: "))
valorSaque = float(input("Informe o valor saque: "))

if saldoAtual <= valorSaque:
    print("Saldo atual: ", saldoAtual)
    print("Saque permitido: ", valorSaque)
else:
    print("Saldo insuficiente!")
    print("Saldo atual: ", saldoAtual)