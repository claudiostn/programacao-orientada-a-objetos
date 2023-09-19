# Interação entre objetos

## Descrição do Lab

- Neste laboratório vc irá construir as classes
NumberDisplay e ClockDisplay vistas na aula expositiva. É preciso aproveitar parte do código visto em sala e depois completar as classes com novos métodos solicitados.

- O Lab consiste de 6 atividades. Os
objetivos são: 
    - testar o relógio completo (acionando todos os seus métodos) - fazer uma modificação no relógio para trabalhar também com segundos.

## Atividade 1

- Na classe NumberDisplay acrescente um método de acesso chamado
de getValue(self) que somente retorna o atributo __value.

- Acrescente um método chamado de setValue(self, replacementValue) que estabelece o atributo __value para o valor do parâmetro formal. O método deve verificar os limites válidos para o parâmetro formal.

## Atividade 2

- Faça um programa principal para testarsomente a classe NumberDisplay criando alguns objetos e acionando todos os seus
métodos.

## Atividade 3

- Na classe ClockDisplay acrescente um método de acesso getTime(self) que apenas retorna o atributo __displayString.

- Acrescente um método modificador chamado de setTime(self,hour,minute) que estabelece os atributos para os valores dos parâmetros formais. Esse método também atualiza o display do relógio.

## Atividade 4

- Faça um outro programa principal para testar a classe ClockDisplay criando alguns objetos ClockDisplay e chamando todos os seus métodos.

- Observe como classe ClockDisplay depende da classe NumberDisplay

## Atividade 5

- Crie um objeto ClockDisplay selecionando seu construtor. Chame seu método getTime para descobrir a hora inicial em que o relógio foi ajustado.

- Quantas vezes você precisaria chamar o método timeTick em um objeto ClockDisplay recém-criado para fazer sua hora alcançar 01:00? De que outra forma você faria ele exibir essa hora?

## Atividade 6

- Altere a classe ClockDisplay para que ela possa ser usada com segundos além de horas e minutos. Teste novamente a classe. É necessário alterar a classe NumberDisplay?

- Utilize um outro programa principal para testar a classe.