from enum import Enum
class PlanoSaude(Enum):
    TRUE = 1
    FALSE = 0

nome = input("Digite o seu nome: ")
idade = input("Digite sua idade: ")
opcao = int(input("Informe se você possui Plano de Saude: (1) SIM ou (0) NAO "))
plano = PlanoSaude(opcao)
print(f'Seu nome é {nome}, você tem {idade}. Tem plano de Saude? {plano.name}')