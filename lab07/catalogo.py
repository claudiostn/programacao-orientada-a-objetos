from cd import CD
from dvd import DVD


class Catalogo:

  def __init__(self):
    self.__lista = []

  def inserir_item(self, item):
    if not self.pesquisa_item(item):
      self.__lista.append(item)
      return True
    else:
      return False

  def pesquisa_item(self, item):
    return item in self.__lista

  def listar(self):
    cds = []
    dvds = []
    for item in self.__lista:
      if isinstance(item, CD):
        cds.append(item)
      else:
        dvds.append(item)

    for cd in cds:
      print(cd.get_titulo())

    for dvd in dvds:
      print(dvd.get_titulo())

  def remover_item(self, item):
    if self.pesquisa_item(item):
      self.__lista.remove(item)
      return True
    else:
      return False
