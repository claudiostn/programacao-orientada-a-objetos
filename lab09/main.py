from conta import Conta


def main():
    while True:
        nome = str(input("Nome do correntista: "))
        numero = str(input("Número da conta: "))
        try:
            conta = Conta(nome, numero)
            break
        except (TypeError, ValueError) as error:
            print(error)

    while True:
        deposito = int(input("Valor do depósito: "))
        try:
            print(conta.depositar(deposito))
            break
        except ValueError as error:
            print(error)

    while True:
        saque = int(input("Valor do saque: "))
        try:
            print(conta.sacar(saque))
            break
        except ValueError as error:
            print(error)



if __name__ == "__main__":
    main()
