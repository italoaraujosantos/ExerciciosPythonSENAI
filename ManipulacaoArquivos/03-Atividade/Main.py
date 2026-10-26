from gestao.aluno.Aluno import Aluno

if __name__ == '__main__':
    bandeira = True
    while bandeira:
        opcao = int(Aluno.exibirMenu())
        match opcao:
            case 1:
                aluno = Aluno.adicionaAluno()
                Aluno.gravarDadosAluno(aluno)
            case 2:
                alunos = Aluno.lerArquivo()
                pesquisa = str(input("Qual aluno deseja localizar: ").strip())
                for aluno in alunos:
                    if pesquisa.casefold() == aluno.nome.casefold():
                        media = Aluno.calcularMedia(aluno, aluno.nota1, aluno.nota2, aluno.nota3, aluno.nota4)
                        print(f"Aluno: {aluno.nome}")
                        print(f"Media: {media:.2f}")
                        print(f"Status: {aluno.status}")
                        break
                else:
                    print("Aluno não localizado!")
            case 3:
                alunos = Aluno.lerArquivo()
                pesquisa = str(input("Qual aluno deseja localizar: ").strip())

                for aluno in alunos:
                    if pesquisa.casefold() == aluno.nome.casefold():
                        print(f"Aluno: {aluno.nome} \t Status: {aluno.status}\n")
                        break
                else:
                    print("Aluno não localizado!\n")
            case 4:
                media = []
                alunos = Aluno.lerArquivo()
                turma = str(input("Qual aluno deseja localizar: ").strip())
                for aluno in alunos:
                    if turma.casefold() == aluno.turma.casefold():
                        nota = float(Aluno.calcularMedia(aluno, aluno.nota1, aluno.nota2, aluno.nota3, aluno.nota4))
                        media.append(nota)
                if media:
                    maior_media = max(media)
                    print(f"Maior média da turma {aluno.turma}: {maior_media:.2f}")
                else:
                    print("Turma não localizada ou sem alunos cadastrados!\n")
            case 5:
                print("\nFinalizando...")
                if opcao == 5:
                    bandeira = False