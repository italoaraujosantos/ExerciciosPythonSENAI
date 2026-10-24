
from ItemPedido import ItemPedido
from Mesa import Mesa


# Registra um pedido sem deixar que um valor inválido
# interrompa a execução do programa.
def registrar_pedido_seguro(mesa, descricao, valor):
    try:
        item = ItemPedido(descricao, valor)
        mesa.adicionar_pedido(item)

    except ValueError as erro:
        print(f"ALERTA DO SISTEMA: {erro}")


# 1. Instanciando a mesa
mesa1 = Mesa("Mesa 1")


# 2. Registrando pedidos válidos
registrar_pedido_seguro(mesa1, "Pizza Margherita", 45.90)
registrar_pedido_seguro(mesa1, "Refrigerante", 8.50)


# 3. Testando entradas inválidas
print("\n--- TESTANDO ENTRADA INVÁLIDA ---")

registrar_pedido_seguro(mesa1, "Pudim", "quinze")
registrar_pedido_seguro(mesa1, "Café", "5,50")


# 4. Registrando outro pedido válido após os erros
registrar_pedido_seguro(mesa1, "Suco de Laranja", 12.00)


# 5. Fechando a conta com taxa de serviço de 10%
print("\n--- FECHAMENTO DA CONTA ---")
mesa1.fechar_conta(taxa_servico=10)


# 6. Verificando se a mesa foi limpa
print("\n--- VERIFICANDO STATUS DA MESA APÓS FECHAMENTO ---")
mesa1.fechar_conta(taxa_servico=10)
