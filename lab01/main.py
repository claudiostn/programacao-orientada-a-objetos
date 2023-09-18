from estudante import Estudante

def main():
    estudante1 = Estudante("Kenny", "69")
    estudante2 = Estudante("Stan", "20")
    estudante3 = Estudante("Cartman", "100")
    estudante4 = Estudante("Kyle", "11")

    lista_estudantes = [estudante1, estudante2, estudante3, estudante4]

    nome = input("Nome do estudante: ")
    creditos = int(input("Número de créditos: "))

    for estudante in lista_estudantes:
        if nome == estudante.get_nome():
            estudante.adicionar_creditos(creditos)
        print(f"\nNome: {estudante.get_nome()}\nMatrícula: {estudante.get_matricula()}\nCréditos: {estudante.get_creditos()}")


if __name__ == "__main__":
    main()