# Tema escolhido: Sistema de Notificações
# Classe pai abstrata: define o contrato comum para todas as notificações.

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def registrar_log(self):
        """Método concreto compartilhado por todas as notificações."""
        print("Sistema central: iniciando operação de notificação.")

    @abstractmethod
    def enviar(self, destinatario: str, mensagem: str):
        """Contrato obrigatório: cada tipo de notificação deve implementar o envio."""
        pass
