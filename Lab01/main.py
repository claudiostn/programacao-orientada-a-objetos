from estudante import Estudante

def main():
	estudante = Estudante("Kenny", "69")

    estudante.adicionar_creditos(10)

    print(f"Nome:{estudante.get_nome()}\nMatrícula{estudante.get_matricula}\nCréditos:{estudante.get_creditos}")