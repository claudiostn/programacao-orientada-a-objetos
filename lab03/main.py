from professor import Professor

def main():
    professor = Professor("Lembravitas", "01", 30)
    
    professor.mais_horas(10)
    professor.menos_horas(5)

    print(f"Professor {professor.get_nome()} Matrícula {professor.get_matricula()} {professor.get_carga_horaria()} horas semanais")

main()