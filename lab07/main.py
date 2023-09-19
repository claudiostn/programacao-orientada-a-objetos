from catalogo import Catalogo
from cd import CD
from dvd import DVD


def main():

  catalogo = Catalogo()

  cd1 = CD("CD 1", 120, False, "cd1", "a1", 12)
  cd2 = CD("CD 2", 120, True, "cd2", "a2", 12)
  cd3 = CD("CD 3", 120, False, "cd3", "a3", 12)

  dvd1 = DVD("DVD 1", 120, False, "dvd1", "d1")
  dvd2 = DVD("DVD 2", 120, False, "dvd2", "d2")
  dvd3 = DVD("DVD 3", 120, False, "dvd3", "d3")

  catalogo.inserir_item(cd1)
  catalogo.inserir_item(dvd1)
  catalogo.inserir_item(cd2)
  catalogo.inserir_item(dvd2)
  catalogo.inserir_item(cd3)
  catalogo.inserir_item(dvd3)

  catalogo.listar()


if __name__ == '__main__':
  main()
