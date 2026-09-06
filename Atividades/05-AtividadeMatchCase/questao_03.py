print("Turno de Estudo")

turno = str(input("Turno de Estudo: "))

match turno:
    case 'M'|'m':
        print("Aluno(a) estuda no turno matutino.")
    case 'V'|'v':
        print("Aluno(a) estuda no turno vespertino.")
    case 'N'|'n':
        print("Aluno(a) estuda no turno noturno.")
    case _:
        print("Opção invalida!.")