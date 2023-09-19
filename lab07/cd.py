from item import Item

class CD(Item):
    def __init__(self, titulo, tempo, possuo, comentario, artista, trilhas):
        super().__init__(titulo, tempo, possuo, comentario)
        self.__artista = ""
        self.__trilhas = 0

    def get_artista(self):
        return self.__artista
        
    def set_artista(self, novo_artista):
        self.__artista = novo_artista 

    def get_trilhas(self):
        return self.__trilhas

    def set_trilhas(self, nova_trilhas):
        self.__tempo = nova_trilhas 


        

        