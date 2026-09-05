print("Menu Lanchonete")
opcao = int(input("Qual o código do produto?"))
match opcao:
    case 1:
        print('Código: 01\n Produto: Cachorro-quente\nPreço: R$ 10.00')
    case 2:
        print('Código: 02\n Produto: Hamburguer\nPreço: R$ 15.00')
    case 3:
        print('Código: 03\n Produto: Batata-frita\nPreço: R$ 8.00')
    case 4:
        print('Código: 04\n Produto: Refrigerante\nPreço: R$ 5.00')
    case _:
        print("Código inválido!")