print("Calcula Lucro produto")
nomeProduto = input("Digite o nome do produto: ")
valorVenda = float(input("Digite o valor do produto: "))
custo = float(input("Digite o custo do produto: "))

print(f"Produto: {nomeProduto}"
      f"Lucro: {valorVenda - custo}"
      f"Lucro bom: {(valorVenda - custo) >= 20.0}")
