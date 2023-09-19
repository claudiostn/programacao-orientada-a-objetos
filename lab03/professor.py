class Professor:
    def __init__(self, nome, matricula, carga_horaria):
        self.__nome = nome
        self.__matricula = matricula
        self.__carga_horaria = carga_horaria

    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def get_carga_horaria(self):
        return self.__carga_horaria
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
    
    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    def mais_horas(self, valor):
        self.__carga_horaria += valor

    def menos_horas(self, valor):
        self.__carga_horaria -= valor