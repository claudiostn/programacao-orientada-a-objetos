from carro import Carro
from moto import Moto
from bicicleta import Bicicleta
from frota import Frota


def main():
    carro = Carro("CAR3254", "Nissan", 4, "Automovel", 4)

    moto = Moto("KYL7777", "Honda", 2, "Motocicleta", 150)

    bicicleta = Bicicleta("KEN6969", "Caloi", 2, "Bicicleta", 6)

    def testar_transporte():
        carro.setFabricanteVeiculo("Honda")
        carro.setPlacaVeiculo("AAA1234")
        carro.setNumeroRodas(5)
        carro.setTipoVeiculo("Carro")
        carro.setPortas(2)
        carro.imprime()

        moto.setFabricanteVeiculo("Yamaha")
        moto.setPlacaVeiculo("BBB1234")
        moto.setNumeroRodas(4)
        moto.setTipoVeiculo("Moto")
        moto.setCilindradas(300)
        moto.imprime()

        bicicleta.setFabricanteVeiculo("Monark")
        bicicleta.setPlacaVeiculo("CCC1234")
        bicicleta.setNumeroRodas(3)
        bicicleta.setTipoVeiculo("Bicicleta")
        bicicleta.setMarchas(12)
        bicicleta.imprime()

    def testar_frota():
        frota = Frota()

        frota.inserir(moto)
        frota.inserir(bicicleta)
        frota.inserir(carro)

        frota.imprimir()

        if frota.pesquisar(carro):
            print("\nVeiculo encontrado")
        else:
            print("\nVeiculo nao econtrado")

        frota.remover(moto)

        frota.imprimir()

    testar_transporte()
    testar_frota()
    
if __name__ == "__main__":
  main()
