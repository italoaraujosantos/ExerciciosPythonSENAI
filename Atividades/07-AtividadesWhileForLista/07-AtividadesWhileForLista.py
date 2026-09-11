"""
Resume: Crie uma lista que armazene um numero x de funcionários. Usando o while, adcione quantos funcionarios quizer.
    Com o For, imprima duas listas:
    Uma lista com todos os que redeberão um aumento. Outra lista com os funcionarios que serão demitidos.
    Decida qual funcionario sera demitido ou recebera um aumento pelo index do funcionario lista[]

"""


funcionarios = [
    {
        "nome": [],
        "produtividade": [],
        "demissao": [],
        "salario": []
    }
]

funcionarios = [
    {
        "nome": "Carlos",
        "produtividade": 85,
        "demissao": False,
        "salario": 3500.00
    },
    {
        "nome": "Ana",
        "produtividade": 92,
        "demissao": False,
        "salario": 4200.00
    },
    {
        "nome": "João",
        "produtividade": 67,
        "demissao": True,
        "salario": 2800.00
    },
    {
        "nome": "Mariana",
        "produtividade": 95,
        "demissao": False,
        "salario": 5100.00
    },
    {
        "nome": "Pedro",
        "produtividade": 73,
        "demissao": False,
        "salario": 3200.00
    }
]

promovidos =[]
demitidos = []

for funcionario in funcionarios:
    if funcionario["produtividade"] >= 80:
        funcionario["salario"] = funcionario["salario"] * 1.15
        promovidos.append(funcionario)
    else:
        demitidos.append(funcionario)

for promovido in promovidos:
    print(f"Promovido: {promovido["nome"]} Salario: {promovido["salario"]:.2f}")

for demitido in demitidos:
    print(f"Demitido: {demitido["nome"]}")