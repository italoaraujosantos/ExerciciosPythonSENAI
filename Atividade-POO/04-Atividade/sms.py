# Implementação concreta de notificação por SMS.

from notificacao import Notificacao


class SMS(Notificacao):
    def __init__(self, destinatario="", mensagem=""):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self, destinatario: str, mensagem: str):
        # Mantém apenas os dígitos para validar números com ou sem pontuação.
        telefone = "".join(caractere for caractere in destinatario if caractere.isdigit())

        if len(telefone) >= 9:
            print(f"SMS enviado para {destinatario}: {mensagem}")
        else:
            print(f"Erro: telefone inválido ({destinatario}). São necessários pelo menos 9 dígitos.")
