# Tratamento de exceções

## Atividade 01

- Projete uma classe chamada Conta para representar
uma conta bancária. Esta classe deve possui os
seguintes atributos privados: nome do correntista,
número da conta, saldo disponível e um flag
informando se a conta está ativa ou não. O construtor
deve inicializar o nome do correntista e o número da
conta através de parâmetros, os outros atributos
devem ser atribuídos como: saldo disponível zero e
conta ativa. Elabore dois métodos públicos para essa
classe, um para fazer depósitos e outro para fazer
saques

## Atividade 02
- Observe que valores de dinheiro são sempre
positivos e que somente é possível fazer saques se
houver saldo disponível. Caso não seja possível
fazer saques e depósitos, lançar exceções
apropriadas nos próprios métodos. Não se esqueça
de prover os métodos get e set para os atributos,
pois eles são privados. Verifique a necessidade de se
lançar exceções nesses métodos.

## Atividade 03

- Crie um programa principal. Nele, utilize a
classe Conta para testar todos os métodos
codificados, principalmente os métodos que
lançam exceções.