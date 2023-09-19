from veiculo import Veiculo

class Moto(Veiculo):
	def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, cilindradas):
		super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
		self.__cilindradas = cilindradas
	
	def getCilindradas(self):
		return self.__cilindradas
	
	def setCilindradas(self, cilindradas):
		self.__cilindradas = cilindradas
	
	def imprime(self):
		super().imprime()
		print("Quant. de cilindradas: " + str(self.getCilindradas()) + "\n")