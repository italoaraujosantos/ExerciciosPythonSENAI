
import pandas as pd

# 1. Ler o arquivo CSV original
funcionarios = pd.read_csv("funcionarios.csv", sep=";")

print("Arquivo original:")
print(funcionarios)

# 2. Remover os funcionários dos índices 0 e 1
funcionarios = funcionarios.drop(index=[0, 1]).reset_index(drop=True)

# 3. Cadastrar novos funcionários com cargos diferentes
proximo_id = int(funcionarios["id"].max()) + 1

novos_funcionarios = pd.DataFrame([
    {
        "id": proximo_id,
        "nome": "Mariana Costa",
        "salario": 7800.00,
        "cargo": "Arquiteta de Soluções"
    },
    {
        "id": proximo_id + 1,
        "nome": "Rafael Nunes",
        "salario": 6900.00,
        "cargo": "Especialista em Cibersegurança"
    },
    {
        "id": proximo_id + 2,
        "nome": "Beatriz Oliveira",
        "salario": 6200.00,
        "cargo": "Scrum Master"
    },
    {
        "id": proximo_id + 3,
        "nome": "Lucas Ferreira",
        "salario": 1800.00,
        "cargo": "Estagiário"
    }
])

# 4. Adicionar os novos funcionários ao DataFrame
funcionarios = pd.concat(
    [funcionarios, novos_funcionarios],
    ignore_index=True
)

# 5. Criar a coluna tempo_empresa com valores inteiros
# Substitua os zeros pelo tempo real de cada funcionário, em meses.
funcionarios["tempo_empresa"] = 0

# Registrar o tempo de empresa do estagiário como inteiro
funcionarios.loc[
    funcionarios["nome"] == "Lucas Ferreira",
    "tempo_empresa"
] = 3

# Garantir que a coluna seja do tipo inteiro
funcionarios["tempo_empresa"] = (
    funcionarios["tempo_empresa"].astype(int)
)

# 6. Salvar todos os funcionários atualizados
funcionarios.to_csv(
    "funcionarios_atualizado.csv",
    sep=";",
    index=False,
    encoding="utf-8"
)

# 7. Filtrar funcionários com salário acima de R$ 6.000
cargos_altos = funcionarios[
    funcionarios["salario"] > 6000
]

# 8. Salvar o novo arquivo com salários acima de R$ 6.000
cargos_altos.to_csv(
    "cargos_altos.csv",
    sep=";",
    index=False,
    encoding="utf-8"
)

# 9. Conferir os resultados
print("\nFuncionários atualizados:")
print(funcionarios.to_string(index=False))

print("\nFuncionários com salário acima de R$ 6.000:")
print(cargos_altos.to_string(index=False))

print("\nTipos de dados:")
print(funcionarios.dtypes)

# 10. Conferir se os arquivos foram salvos corretamente
conferencia = pd.read_csv(
    "funcionarios_atualizado.csv",
    sep=";"
)

conferencia_cargos = pd.read_csv(
    "cargos_altos.csv",
    sep=";"
)

assert len(conferencia) == len(funcionarios)
assert len(conferencia_cargos) == len(cargos_altos)
assert (conferencia_cargos["salario"] > 6000).all()
assert pd.api.types.is_integer_dtype(
    conferencia["tempo_empresa"]
)

print("\nVerificação concluída!")
print("Arquivos CSV salvos e conferidos com sucesso.")
