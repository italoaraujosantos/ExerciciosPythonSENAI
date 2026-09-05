print("Sistema Radar de transito")

velocidadeAtual = int(input("Velocidade atual: "))
if velocidadeAtual<= 80:
    print("Velocidade dentro do limite permitido. Boa viagem!")
else:
    print("Você foi multado por excesso de velocidade!")