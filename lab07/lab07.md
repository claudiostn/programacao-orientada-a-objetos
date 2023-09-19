# Herança

## Atividade 01 

- Desenvolva duas classes bases chamadas de CD e
DVD. Nessas classes basta implementar um construtor
e os métodos de acesso/modificador(métodos get e
set).

- Use os seguintes campos para a classe CD:
titulo(String), tempo de reprodução(int), artista(String),
número de trilhas (int), possuo(booleano), comentário
(String)

- Use os seguintes campos para a classe DVD:
titulo(String), tempo de reprodução(int),
diretor(String), possuo(booleano), comentário (String)

## Atividade 02

- Desenvolver uma aplicação OO que permite armazenar
informações sobre CDs e DVDs. A idéia é criar um catálogo de
todos os CDs e DVDs. As funcionalidades que queremos fornecer
na aplicação devem incluir pelo menos as seguintes:

    - Deve permitir que possamos inserir informações sobre CDs e DVDs (dois métodos)
    - Deve armazenar essas informações para que elas possam ser usadas depois, mas na mesma aplicação.
    - Deve fornecer uma operação de pesquisa que permita localizar CDs e DVDs (dois métodos)
    - Deve permitir imprimir uma lista de todos os CDs e de todos os DVDs (dois métodos)
    - Deve permitir que se removam informações (dois métodos)   Não utilizar herança e usar duas coleções list, uma para     CD e outra para DVD

## Atividade 03

- Desenvolver uma aplicação OO bem projetada que permite armazenar
informações sobre CDs e DVDs. A idéia é criar um catálogo de todos os CDs e DVDs. As funcionalidades que queremos fornecer na aplicação devem incluir pelo menos as seguintes:
    - Deve permitir que possamos inserir informações sobre CDs e DVDs (1
    método)
    - Deve armazenar essas informações para que elas possam ser usadas
    depois, mas na mesma aplicação.
    - Deve fornecer uma operação de pesquisa que permita localizar CDs e
    DVDs (1 método)
    - Deve permitir imprimir uma lista de todos os CDs e de todos os DVDs (1
    método)
    - Deve permitir que se removam informações (1 método)
    - Definir uma classe Item que será a superclasse de CD e DVD.
        - Utilizar as classes CD e DVD projetadas anteriormente mas
    agora tornando-as subclasses de Item. Usar somente uma
    coleção list que armazenará objetos Item.