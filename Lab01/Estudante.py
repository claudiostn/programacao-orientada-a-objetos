class Estudante:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__creditos = 0

    def get_nome():
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula

    def get_creditos(self):
        return self.__creditos
    
    def set_nome(self, novo_nome):
        set_nome = novo_nome
    
    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
    
    def set_creditos(self, valor):
        self.__creditos = valor

    def adicionar_creditos(self, valor):
        self.__creditos += valor