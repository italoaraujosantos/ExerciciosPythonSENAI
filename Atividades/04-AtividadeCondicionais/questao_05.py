from enum import Enum

class ConviteVip(Enum):
    SIM = 1
    NAO = 0

class Organizadora(Enum):
    SIM = 1
    NAO = 0

print("Catraca VIP de Eventos")

idade = int(input("Insira sua idade: "))
opcaoVip = int(input("Infome (1) Vip e (0) Não Vip: "))
vip = ConviteVip(opcaoVip)
opcaoOrg = int(input("Informe se é Organizador SIM: (1) SIM ou NAO: "))
org = Organizadora(opcaoOrg)

if (idade >= 18 or vip.value == ConviteVip.SIM) or (org.value == ConviteVip.SIM):
    print("Entrada PERMITIDA! Seja bem-vindo(a)")
else:
    print("Entrada NEGADA!")