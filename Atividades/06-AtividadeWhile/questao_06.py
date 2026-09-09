numero_secreto = 15
tentaitvas = 0
while entrada != numero_secreto:
    entrada = int(input("Insira seu palpite: "))
    tentaitvas += 1
    if entrada == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto em {tentaitvas} tentativas!")
        break
    else:
        print("Erro o palpite!")