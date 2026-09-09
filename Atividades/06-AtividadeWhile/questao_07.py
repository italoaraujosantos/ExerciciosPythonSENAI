saldo_Inicial = float(input("Informe o saldo inicial: "))
while saldo_Inicial <= 0:
    custo = float(input("Informe o custo: "))
    if saldo_Inicial >= custo:
        saldo_Inicial -= custo
        print(f"Saldo é igual a R${saldo_Inicial:.2}.")
    else:
        print(f"Saldo é igual a R${saldo_Inicial:.2}.")
        print("Saldo insuficiente!")