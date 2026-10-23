# Tema escolhido: Sistema de Notificações
# Demonstra abstração, herança e polimorfismo em processamento em lote.

from notificacao import Notificacao
from email_notificacao import Email
from sms import SMS


def processar_lote(lista_de_objetos):
    """Processa diferentes notificações usando o contrato da classe abstrata."""
    for item in lista_de_objetos:
        item.registrar_log()
        item.enviar(item.destinatario, item.mensagem)
        print("-" * 30)


if __name__ == "__main__":
    # 1. Tentativa de instanciar a classe abstrata (DEVE GERAR ERRO).
    # Descomente a linha abaixo para testar e comprovar o bloqueio:
    # objeto_generico = Notificacao()

    # 2. Instanciando as classes filhas.
    obj1 = Email("usuario@exemplo.com", "Seu cadastro foi confirmado.")
    obj2 = SMS("(61) 98765-4321", "Seu código de confirmação é 123456.")

    # 3. Criando um lote de processamento (pode repetir tipos).
    lote = [obj1, obj2, obj1]

    # 4. Processando em lote (demonstrando polimorfismo e abstração).
    print("\n--- INICIANDO PROCESSAMENTO EM LOTE ---")
    processar_lote(lote)

    # Testes adicionais para verificar as validações.
    print("\n--- TESTANDO DADOS INVÁLIDOS ---")
    obj1.enviar("email-invalido", "Teste de validação.")
    obj2.enviar("12345", "Teste de validação.")
