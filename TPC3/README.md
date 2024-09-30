# Relatório
## Data: 2024-09-29
## Author: Mariana Gonçalves Silva

## Resumo

O TPC3 constituiu em criar um jogo chamado o jogo dos 21 fósforos. 
No início do jogo, há 21 fósforos e cada jogador pode tirar entre 1 a 4 fósforos quando for a sua vez de jogar. Os jogadores (pessoa e computador) jogam alternadamente e quem tirar o último fósforo perde.
Tinha de conter dois modos:
* O jogador jogava em primeiro lugar e o computador tinha que ganhar sempre o jogo;
* O computador jogava em primeiro lugar e se o utilizador cometer um erro de cálculo, então o computador tinha de ganhar. Caso contrário, era o jogador quem ganhava o jogo.

# O jogador jogava em 1º lugar:

Tanto neste modo como no outro, tive muita dificuldade em perceber como é que se ganhava sempre o jogo. Demorei a chegar ao facto de que quem acabava por ter 5 fósforos é quem ganhava sempre ou que quem acabava com 6 perdia sempre. O problema também foi para depois encontrar um código que conseguia traduzir esse raciocinio. Tinha então que encontrar uma forma de fazer com que o jogador acabasse sempre com 6. Ora, para isso ser possivel o computador tinha de calcular quantos fósforos faltava para o próximo múltiplo de 5 e subtrair 1. Ou seja, o computador tinha de fazer a divisão inteira de 5 e a esse resto subtrair 1 para a pessoa ficar sempre a 1 fósfro do múltiplo de 5. No entanto, percebi depois que no caso do resto ser 0 (já ser um múltiplo de 5) então o computador não podia retirar -1 fósforo, mas tinha de sim de retirar 4, por isso fiz um caso especifico para esses casos.

Por outro lado, não havia o problema de a pessoa ter alguma vez um multiplo de 5 porque ela começava a jogar e, no máximo, só pode jogar 4 (21-4=17). A partir dai e com este raciocinio, o computador ganha sempre.

Ainda fiz também um caso para o qual a pessoa queria fazer batota e quando somente lhe restava 1 fósforo não punha 1. O jogo só acabava quando ela escrevia de facto o numero 1.


# O computador jogava em 1º lugar:

Aqui, o raciocinio era ao contrário pois o jogador tinha de ganhar se não erasse nos seus cálculos. Deste modo, quem tinha de ficar com 5 fósforos no final era a pessoa e não o computador. Assim, a cada jogada do computador este dava sempre um multiplo de 5 à pessoa e não o número que estava logo acima como no modo 1. No entanto, se com 5 fósforos na mesa a pessoa não tirava 4, então o compurador tirava quase todos os fósforos menos 1, deixando o último para a pessoa e nesse caso ela perdia (pois errou nos calculos).

Já tendo o raciocinio em mente, este modo foi mais fácil de elaborar, mesmo se tive de fazer mais casos (um para quando a pessoa enganava se nos calculos e outro para quando o computador só tinha 1 fósforo na mesa dizia que tinha perdido).

# Juntar os dois modos

Para não me atrapalhar a escrever o jogo, elaborei ambos os modos separadamente e depois juntei-os. Aqui ainda fiz com que o computador dissesse, no ínicio, as regras do jogo.

Para além disso também adicionei algumas strings onde o computador somente aceitava o numero 1, 2, 3 e 4 quando a pessoa estava a escolher quantos fósforos retirar e caso fosse um numero diferente então dizia que a resposta era invalida e pedia para colocar outro numero (dos 4 permitidos). Ainda fiz o mesmo para os modos, onde a pessoa somente podia colocar o modo 1 ou 2 e não outro número, caso contrário pedia outra vez.