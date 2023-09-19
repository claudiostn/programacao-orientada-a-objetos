from veiculo import Veiculo

class Bicicleta(Veiculo):
	def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, marchas):
		super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
		self.__marchas = marchas
	
	def getMarchas(self):
		return self.__marchas
	
	def setMarchas(self, marchas):
		self.__marchas = marchas

	def imprime(self):
		super().imprime()
		print("Quant. de marchas: " + str(self.getMarchas()) + "\n")