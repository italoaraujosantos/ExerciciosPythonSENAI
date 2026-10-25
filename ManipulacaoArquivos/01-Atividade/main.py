def main():
    # 1. Captura do nome do cliente
    usuario = input("Digite seu nome para iniciar a compra: ").strip()

    while not usuario:
        print("O nome não pode ficar vazio.")
        usuario = input("Digite seu nome para iniciar a compra: ").strip()

    # 2. Loop para adicionar produtos ao carrinho
    produtos = []
    total = 0.0

    while True:
        nome_produto = input("Digite o nome do produto (ou 'fim' para encerrar): ").strip()

        if nome_produto.lower() in ("fim", "sair", "encerrar"):
            break

        if not nome_produto:
            print("O nome do produto não pode ficar vazio.")
            continue

        entrada_preco = input(f"Digite o preço de '{nome_produto}' (ex.: 12.50): ").strip()
        entrada_preco = entrada_preco.replace(",", ".")

        try:
            preco = float(entrada_preco)
            if preco < 0:
                print("O preço não pode ser negativo.")
                continue
        except ValueError:
            print("Preço inválido. Digite um número, por exemplo 12.50.")
            continue

        produtos.append([nome_produto, preco])
        total += preco
        print(f"Produto '{nome_produto}' adicionado ao carrinho.")

    # 3. Geração do arquivo pagamento.txt
    print("\n--- FINALIZANDO COMPRA ---")

    with open("pagamento.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("RECIBO DE COMPRA\n")
        arquivo.write("=================\n")
        arquivo.write(f"Cliente: {usuario}\n\n")
        arquivo.write("Produtos:\n")

        if produtos:
            for nome, preco in produtos:
                arquivo.write(f"- {nome}: R$ {preco:.2f}\n")
        else:
            arquivo.write("Nenhum produto comprado.\n")

        arquivo.write("\n")
        arquivo.write(f"TOTAL: R$ {total:.2f}\n")

    print("Recibo gravado em pagamento.txt.")

    # 4. Leitura do arquivo e extração do total
    print("\n--- PROCESSANDO PAGAMENTO ---")

    with open("pagamento.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()

    marcador = "TOTAL: R$ "
    posicao = conteudo.find(marcador)

    if posicao != -1:
        inicio_total = posicao + len(marcador)
        fim_total = conteudo.find("\n", inicio_total)

        if fim_total == -1:
            fim_total = len(conteudo)

        total_gravado = conteudo[inicio_total:fim_total].strip()
        print(
            "Compra processada com sucesso! "
            f"Valor cobrado: R$ {total_gravado}"
        )
    else:
        print("Não foi possível localizar o total no recibo.")


if __name__ == "__main__":
    main()
