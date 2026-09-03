print("Sistema Escolar \n")

nota1 = float(input("Informe sua primeira nota: "))
nota2 = float(input("Informe sua primeira nota: "))
media = (nota1 + nota2) / 2

total_Aulas = int(input("Informe sua quantidade de Aulas: "))
faltas = int(input("Informe sua quantidade de faltas: "))
frequencia = (total_Aulas - faltas / total_Aulas )


print(f"Aluno {media >= 6.0 and frequencia >= 75} com {media} e {frequencia} de frenquencia.")