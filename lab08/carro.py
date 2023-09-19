from veiculo import Veiculo

class Carro(Veiculo):
	def __init__(self, placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo, portas):
		super().__init__(placaveiculo, fabricanteveiculo, numerorodas, tipoveiculo)
		self.__portas = portas
	
	def getPortas(self):
		return self.__portas
	
	def setPortas(self, portas):
		self.__portas = portas
	
	def imprime(self):
		super().imprime()
		print("Quant. de portas: " + str(self.getPortas()) + "\n")
		