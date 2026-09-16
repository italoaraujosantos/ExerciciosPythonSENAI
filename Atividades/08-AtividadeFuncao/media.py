def media(nome, nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4) / 4
    if media >= 7:
        print(f"{nome} Aprovado com média {media}.")
    else:
        print(f"{nome} Reprovado com media {media}.")

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media(nome, nota1, nota2, nota3, nota4)
