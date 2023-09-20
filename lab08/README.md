# Herança, Polimorfismo e Vinculação dinâmica

## Atividade 1

- Usar a classe Veiculo (disponível no SIGAA) de modo que
ela seja uma superclasse das classes Carro, Moto e
Bicicleta.
- Desenvolver as classes Carro, Moto e Bicicleta de modo que
elas sejam subclasses de Veiculo. Não se esqueçam de
acrescentar os campos privados exclusivos dessas
subclasses, por exemplo(número de portas para Carro,
cilindrada para Moto e número de marchas para Bicicleta)
- Para as classes Carro, Moto e Bicicleta, basta definir os
campos como privados e fornecer os métodos get e set. O
método imprime() de Veiculo deve ser sobrecarregado nas
subclasses.

## Atividade 2

- Elabore uma classe chamada de MainTransporte para
testar todos os construtores e todos os métodos das
classes Veiculo, Carro, Moto e Bicicleta. Testar
principalmente os métodos imprime() das classes.

## Atividade 3

- Desenvolver uma aplicação OO bem projetada que permite armazenar
informações sobre carros, motos e bicicletas. A idéia é criar uma frota de
todos os veículos. As funcionalidades que queremos fornecer na aplicação
devem incluir pelo menos as seguintes:
- Deve permitir que possamos inserir informações sobre carros, motos e
bicicletas.
- Deve fornecer uma operação de pesquisa que permita verificar se
determinado carro, moto ou bicicleta estão na coleção.
- Deve permitir imprimir uma lista de todos os carros, motos e bicicletas,
nessa ordem.
- Deve permitir que se removam informações.
- Para construir a frota, desenvolva uma Lista da classe Veiculo da
atividade 1.

## Atividade 4

- Elabore uma classe chamada de MainFrota para testar
todos os métodos da classe Frota (classe que
armazena a coleção de veículos).