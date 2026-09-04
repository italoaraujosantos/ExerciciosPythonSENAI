'''
Justificativa: senha_cadastrara recebe um valor inteiro de senha
                e ao compara com senha_cadastrada == senha_digitada,
                gerar por efetuar uma comparação entre tipos de variaveis
                integer e string na senha_digita.
'''
senha_cadastrada = 1234
senha_digitada = input("Digite sua senha: ")
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado)