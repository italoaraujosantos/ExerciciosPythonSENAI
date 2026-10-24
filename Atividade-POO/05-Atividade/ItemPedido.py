
class ItemPedido:

    def __init__(self, descricao, valor):
        self.descricao = descricao

        try:
            self.valor = float(valor)
        except (ValueError, TypeError):
            raise ValueError(
                f"Erro: O valor para '{descricao}' "
                "deve ser estritamente numérico."
            )
