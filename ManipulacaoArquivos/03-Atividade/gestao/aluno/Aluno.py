class Aluno:
    def __init__(self, nome, turma, nota1, nota2, nota3, nota4, status ):
        self.nome = nome
        self.turma = turma
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.status = status

    def exibirMenu() -> int:
        print("1 - Adicionar Aluno")
        print("2 - Calcula a media de um aluno")
        print("3 - Buscar por nome de Alunos")
        print("4 - Maior média")
        print("5 - Finalizar")
        opcao = int(input("Informe a opcao: "))
        return opcao

    def adicionaAluno() -> Aluno:
        nome = str(input("Digite o nome do aluno: "))
        turma = str(input("Informe a turma: "))
        nota1 = float(input("Informe a nota 1: "))
        nota2 = float(input("Informe a nota 2: "))
        nota3 = float(input("Informe a nota 3: "))
        nota4 = float(input("Informe a nota 4: "))
        media = float((nota1 + nota2 + nota3 + nota4)/4.0)
        if media >= 7:
            status = "Aprovado"
        else:
            status = "Reprovado"
        return Aluno(nome, turma, nota1, nota2, nota3, nota4, status)

    def gravarDadosAluno(aluno: Aluno):
        with open("alunos.txt", "a+", encoding="utf-8") as arquivo:
            arquivo.write(str(f"{aluno.nome};{aluno.turma};{aluno.nota1};{aluno.nota2};{aluno.nota3};{aluno.nota4};{aluno.status}\n"))

    def lerArquivo() -> list[Aluno]:
        alunos = []
        with open("alunos.txt", "r", encoding="utf-8") as arquivo:
            for numero_linha, linha in enumerate(arquivo, start=1):
                linha = linha.strip()
                if not linha:
                    continue
                dados = linha.split(";")
                if len(dados) != 7:
                    print(f"Linha {numero_linha}: quantidade de campos inválida.")
                    continue
                try:
                    nome = dados[0]
                    turma = dados[1]
                    nota1 = float(dados[2])
                    nota2 = float(dados[3])
                    nota3 = float(dados[4])
                    nota4 = float(dados[5])
                    status = dados[6]
                    aluno = Aluno(nome, turma, nota1, nota2,nota3, nota4, status)
                    alunos.append(aluno)
                except ValueError:
                    print(f"Linha {numero_linha}: nota inválida.")
        return alunos

    def calcularMedia(self, nota1: float, nota2: float, nota3: float, nota4: float) -> float:
        media = (nota1 + nota2 + nota3 + nota4)/4
        return media
