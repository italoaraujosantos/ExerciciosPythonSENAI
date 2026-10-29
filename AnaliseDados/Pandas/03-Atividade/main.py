import pandas as pd
import re

ARQUIVO_ENTRADA = "dados_despadronizados.csv"
ARQUIVO_SAIDA = "dados_padronizados.csv"


def validar_cpf(cpf):
    """Valida o CPF pelos dígitos verificadores."""
    if not cpf or len(cpf) != 11 or cpf == cpf[0] * 11:
        return False

    numeros = [int(digito) for digito in cpf]

    soma = sum(numeros[i] * (10 - i) for i in range(9))
    resto = (soma * 10) % 11
    digito1 = 0 if resto == 10 else resto

    soma = sum(numeros[i] * (11 - i) for i in range(10))
    resto = (soma * 10) % 11
    digito2 = 0 if resto == 10 else resto

    return numeros[9] == digito1 and numeros[10] == digito2


def formatar_telefone(numero):
    """Formata telefones brasileiros com DDD."""
    if not numero:
        return ""

    # .str.replace é usado no DataFrame para remover caracteres antes
    # desta função; aqui mantemos somente os dígitos como proteção extra.
    digitos = re.sub(r"\D", "", numero)

    # Remove o código do país quando vier junto (ex.: +55).
    if len(digitos) in (12, 13) and digitos.startswith("55"):
        digitos = digitos[2:]

    if len(digitos) == 11:
        return f"({digitos[:2]}) {digitos[2]}{digitos[3:7]}-{digitos[7:]}"
    if len(digitos) == 10:
        return f"({digitos[:2]}) {digitos[2:6]}-{digitos[6:]}"
    return ""


def validar_telefone(numero):
    """Verifica se o telefone tem DDD e 10 ou 11 dígitos."""
    digitos = re.sub(r"\D", "", numero or "")
    if len(digitos) in (12, 13) and digitos.startswith("55"):
        digitos = digitos[2:]
    return len(digitos) in (10, 11) and digitos[:2] != "00"


def converter_salario(valor):
    """Converte salários em formatos brasileiros ou com ponto decimal."""
    if pd.isna(valor):
        return None

    texto = str(valor).strip()
    texto = texto.replace("R$", "").replace(" ", "")

    if not texto:
        return None

    # Quando há vírgula, ela é considerada separador decimal brasileiro:
    # 2.350,50 -> 2350.50
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    # Sem vírgula, um ponto final é tratado como decimal: 6100.00 -> 6100.00

    try:
        return float(texto)
    except ValueError:
        return None


def formatar_moeda(valor):
    if pd.isna(valor):
        return ""
    # 1234.56 -> "R$ 1.234,56"
    texto = f"{valor:,.2f}"
    texto = texto.replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {texto}"


# Lê todas as colunas como texto para preservar os valores originais.
df = pd.read_csv(ARQUIVO_ENTRADA, dtype=str, keep_default_na=False)

# Limpa espaços extras nos campos de texto.
df["nome"] = df["nome"].str.strip()
df["cpf"] = df["cpf"].str.strip()
df["numero"] = df["numero"].str.strip()
df["salario"] = df["salario"].str.strip()

# .str.replace remove tudo que não for dígito, padronizando CPF e telefone.
df["cpf_digitos"] = df["cpf"].str.replace(r"\D", "", regex=True)