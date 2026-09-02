print("Calculador divide conta Amigos!\n\n")
valorTotal = input("Informe o valor total: ")
valorTotal = float(valorTotal)
numeroPessoas = int(input("Informe o numero de pessoas: "))

totalDivisao = valorTotal / numeroPessoas

print(f'O valor total foi de R$ {valorTotal}, e cada pessoa deve pagar R$ {totalDivisao}')