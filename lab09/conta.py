class Conta:
    def __init__(self, correntista, conta):
        self.__correntista = "Indefinido"
        self.__conta = "Indefinido"
        self.__saldo = 0
        self.__ativa = True

        self.set_correntista(correntista)
        self.set_conta(conta)

    def get_correntista(self):
        return self.__correntista

    def get_conta(self):
        return self.__conta

    def get_saldo(self):
        return self.__saldo

    def get_ativa(self):
        return self.__ativa

    def set_correntista(self, nome):
        conta_ativa = self.__ativa is True
        nome_valido = type(nome) is str and nome is not None

        if conta_ativa:
            if nome_valido:
                self.__correntista = nome
                print(f"Nome do correntista alterado para {self.__correntista}")
            else:
                raise TypeError("Nome nao e uma string")
        else:
            raise ValueError("Conta desativada")

    def set_conta(self, numero):
        conta_ativa = self.__ativa is True
        numero_valido = type(numero) is str and numero is not None

        if conta_ativa:
            if numero_valido:
                self.__conta = numero
                print(f"Numero da conta alterado para {self.__conta}")
            else:
                raise TypeError("Numero da conta nao e uma string")
        else:
            raise ValueError("Conta desativada")

    def set_ativa(self, flag):
        conta_ativa = self.__ativa is True
        flag_valida = type(flag) is bool and flag is not None

        if conta_ativa:
            if flag_valida:
                if flag is not True:
                    self.__ativa = flag
                    return "Sua conta está desativada"
                else:
                    raise ValueError("Sua conta ja esta ativa")
            else:
                raise TypeError("Tipo invalido")
        else:
            if flag_valida:
                if flag != False:
                    self.__ativa = flag
                    return "Sua conta está ativa"
                else:
                    raise ValueError("Sua conta ja esta desativada")
            else:
                raise TypeError("Tipo invalido")

    def depositar(self, valor):
        conta_ativa = self.__ativa is True
        valor_valido = valor > 0 and valor is not None

        if conta_ativa:
            if valor_valido:
                self.__saldo += valor
                return f"Saldo: R$ {self.__saldo}"
            else:
                raise ValueError("Valor invalido para deposito")
        else:
            raise ValueError("Conta desativada")

    def sacar(self, valor):
        saldo_positivo = self.__saldo > 0
        valor_valido = 0 < valor <= self.__saldo and valor is not None
        conta_ativa = self.__ativa is True

        if conta_ativa:
            if saldo_positivo:
                if valor_valido:
                    self.__saldo -= valor
                    return f"Saldo: R$ {self.__saldo}"
                else:
                    raise ValueError("Valor invalido para saque")
            else:
                raise ValueError("Saldo negativo")
        else:
            raise ValueError("Conta desativada")
