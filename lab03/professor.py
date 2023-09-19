class Professor:
    def __init__(self, nome, matricula, carga_horaria):
        self.__nome = nome
        self.__matricula = matricula
        self.__carga_horaria = carga_horaria
        self.__carga_horaria_minima = 8
        self.__carga_horaria_maxima = 20
        
    def get_nome(self):
        return self.__nome
    
    def get_matricula(self):
        return self.__matricula
    
    def get_carga_horaria(self):
        return self.__carga_horaria
    
    def get_carga_minima(self):
        return self.__carga_horaria_minima
    
    def get_carga_maxima(self):
        return self.__carga_horaria_maxima
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
    
    def set_carga_horaria(self, carga_horaria):
        self.__carga_horaria = carga_horaria

    def mais_horas(self, valor):
        carga = self.__carga_horaria + valor

        if self.__carga_horaria_minima <= carga <= self.__carga_horaria_maxima:
            self.__carga_horaria = carga

    def menos_horas(self, valor):
        carga = self.__carga_horaria - valor

        if self.__carga_horaria_minima <= carga <= self.__carga_horaria_maxima:
            self.__carga_horaria = carga