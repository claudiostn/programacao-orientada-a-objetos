class Item:
    def __init__(self, titulo, tempo, possuo, comentario):
        self.__titulo = titulo
        self.__tempo = tempo
        self.__possuo = possuo
        self.__comentario = comentario

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, novo_titulo):
        self.__titulo = novo_titulo
    
    def get_tempo(self):
        return self.__tempo

    def set_tempo(self, novo_tempo):
        self.__tempo = novo_tempo    

    def get_possuo(self):
        return self.__possuo

    def set_possuo(self, novo_possuo):
        self.__possuo = novo_possuo 

    def get_comentario(self):
        return self.__comentario
    
    def set_comentario(self, novo_comentario):
        self.__comentario = novo_comentario
