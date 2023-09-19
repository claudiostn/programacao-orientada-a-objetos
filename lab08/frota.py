from carro import Carro
from moto import Moto
from bicicleta import Bicicleta


class Frota:

  def __init__(self):
    self.__frota = []

  def inserir(self, veiculo):
    if not self.pesquisar(veiculo):
      self.__frota.append(veiculo)
      return True
    else:
      return False

  def pesquisar(self, veiculo):
    return veiculo in self.__frota

  def remover(self, veiculo):
    if self.pesquisar(veiculo):
      self.__frota.remove(veiculo)
      return True
    else:
      return False

  def imprimir(self):
    print("\nLista de Veiculos")
    carros = []
    motos = []
    bicicletas = []

    for veiculo in self.__frota:
      if type(veiculo) == Carro:
        carros.append(veiculo)
      elif type(veiculo) == Moto:
        motos.append(veiculo)
      else:
        bicicletas.append(veiculo)

    print("\nCarros")
    for carro in carros:
      print(f"{carro.getFabricanteVeiculo()} {carro.getPlacaVeiculo()}")

    print("\nMotos")
    for moto in motos:
      print(f"{moto.getFabricanteVeiculo()} {moto.getPlacaVeiculo()}")

    print("\nBicicletas")
    for bicicleta in bicicletas:
      print(
          f"{bicicleta.getFabricanteVeiculo()} {bicicleta.getPlacaVeiculo()}")
