# Implementação concreta de notificação por e-mail.

from notificacao import Notificacao


class Email(Notificacao):
    def __init__(self, destinatario="", mensagem=""):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def enviar(self, destinatario: str, mensagem: str):
        if "@" in destinatario and "." in destinatario.split("@")[-1]:
            print(f"E-mail enviado para {destinatario}: {mensagem}")
        else:
            print(f"Erro: endereço de e-mail inválido ({destinatario}).")
