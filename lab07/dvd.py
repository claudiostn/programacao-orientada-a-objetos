from item import Item

class DVD(Item):
    def __init__(self, titulo, tempo, possuo, comentario, diretor):
        super().__init__(titulo, tempo, possuo, comentario)
        self.__diretor = ""

    def get_diretor(self):
        return self.__diretor
        
    def set_diretor(self, novo_diretor):
        self.__diretor = novo_diretor 

    