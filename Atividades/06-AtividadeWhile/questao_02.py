senha = "123456"


while senha != senha:
    entrada = input("Digite a senha: ")
    if entrada != senha:
        print("Senha incorreta. Tente novamente")
    else:
        print("Acesso permitido")
        break