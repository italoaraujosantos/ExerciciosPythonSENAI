
class Mesa:

    def __init__(self, numero_mesa):
        self.numero_mesa = numero_mesa
        self.pedidos = []

    def adicionar_pedido(self, item):
        if not isinstance(item, ItemPedido):
            raise ValueError(
                "O pedido deve ser um objeto ItemPedido."
            )

        self.pedidos.append(item)

        print(
            f"-> {item.descricao} adicionado à "
            f"{self.numero_mesa}."
        )

    def somar_total(self):
        return sum(item.valor for item in self.pedidos)

    def fechar_conta(self, taxa_servico):
        try:
            taxa = float(taxa_servico)

            if taxa < 0:
                raise ValueError(
                    "A taxa de serviço não pode ser negativa."
                )

        except (ValueError, TypeError):
            raise ValueError(
                "A taxa de serviço deve ser numérica e não negativa."
            )

        print(f"\n===== EXTRATO: {self.numero_mesa} =====")

        for item in self.pedidos:
            print(f"{item.descricao}: R$ {item.valor:.2f}")

        subtotal = self.somar_total()
        valor_taxa = subtotal * taxa / 100
        total = subtotal + valor_taxa

        print("-" * 35)
        print(f"Subtotal:       R$ {subtotal:.2f}")
        print(f"Taxa ({taxa:g}%):      R$ {valor_taxa:.2f}")
        print(f"Total a pagar:  R$ {total:.2f}")
        print("=" * 35)

        self.pedidos.clear()


# Importação necessária para validar os objetos ItemPedido.
from ItemPedido import ItemPedido
