while entrada == 2:
    print("1 - Mostrar saudação\n2 - Sair do programa")
    entrada = int(input("Insira os numeros: "))
    if entrada != 1 or entrada != 2:
        print("Opção Inválida!")
    if entrada == 1:
        print("Olá, seja muito bem-vindo(a)!")
    if entrada == 2:
        break