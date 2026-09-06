print("Classificador Vogais e cosoantes")

caracter = str(input("Caracter: "))

match caracter:
    case 'a'|'e'|'i'|'o'|'u':
        print("Você digitou uma vogal.")
    case 'b'|'c'|'d'|'f'|'g'|'j'|'k'|'l'|'m'|'n'|'p'|'q'|'r'|'s'|'t'|'v'|'w'|'x'|'z':
        print("Não é uma vogal.")
    case _:
        print("Caractere inválido!")