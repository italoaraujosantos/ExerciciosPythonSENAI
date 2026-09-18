class Produto:

    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def quantidade(self):
        return self.__quantidade
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__quantidade += quantidade
        else:
            f"Erro: Quantidade deve ser maior que zero"

    def realizar_venda(self, quantidade):
        if self.__quantidade > quantidade:
            self.__quantidade -= quantidade
        else:
            f"Venda negada: Estoque insuficiente."

    def aplicar_desconto(self, percentual):
        if percentual <= 0.80:
            self.__preco = self.preco * percentual
        else:
            f"Erro: Desonto inválido."