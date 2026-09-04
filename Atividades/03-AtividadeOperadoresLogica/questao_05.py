from enum import Enum

class Cartao(Enum):
    SIM = 1
    NAO = 0

print("SISTEMA DE DESCONTO")
valorCompra = float(input("Informe o valor da compra: "))
opcao = input("Informe se o cliente tem cartao: (1) SIM ou (0) NAO")
cartao = Cartao(opcao)
print(f"Valor da compra: {valorCompra>=200} \n"
      f"Ganhou entrega gratis: {valorCompra>=200 and cartao.name == True} \n")