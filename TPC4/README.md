# Relatório
## Data: 2024-10-05
## Author: Mariana Gonçalves Silva

## Resumo

O TPC4 constituiu na criação de uma aplicação em Python que colocava no monitor um certo menu onde a pessoa podia: 1 - Criar uma lista; 2 - Ler uma lista; 3 - Fazer a soma dos numeros da lista; 4 - Fazer a Média; 5 - Saber qual é o maior elemento; 6 - Saber qual é o menor; 7 - Ver se a lista está por ordem crescente; 8 - Ver se está por ordem decrescente; 9 - Procurar um elemento da lista; 0 - Sair.


# Definir as funções

Comecei por defenir todas as minhas funções num ficheiro Python para depois criar um documento py onde as iria colocar.

As funções que foram mais dificeis de fazer foram as funções das opções 7 e 8 onde o utilizador podia saber se a sua lista estava por ordem crescente ou decrescente respetivamente. O meu erro estava na posição do return pois no local onde estava o meu programa somente lia os dois primeiros valores. A partir do momento onde percebi isso, já foi muito mais fácil de faze-las.


# Ficheiro py

Finalmente, quando já tinha todas as minhas funções definidas, bastou coloca-las no meu ficheiro py e acrescentar algumas strings para aparecer no monitor o menu.
Para além disso também criei uma opção para quando o utilizador não introduzia nenhum dos numeros que deveria e nesse caso aparecia uma mensagem de resposta invalida e para selecionar um numero entre 0 e 9, mostrando novamente as opções todas (mostrando novamente o menu).

Tudo isto tinha de estar dentro de um while para que cada vez que o utilizador seleciona-se uma opção, o monitor fosse buscar a função, mostrava a resposta correspondente e no final voltasse a mostrar o menu.

Era importante definir uma variavel Interna que guardava a lista que foi ou criada pelo computador ou inserida pelo utilizador à qual eu até chamei listaInterna. Tinha de estar fora do while uma vez que se estivesse dentro, cada vez que o utilizador queria introduzir uma nova opção, a lista voltava a ficar vazia. Para além disso, para o ciclo funcionar criei uma condição verdadeira e enquanto ela não fosse falsa, aparecia sempre o menu. Na opção sair, essa condição passava então a ser falsa, aparecia no monitor a lista daquele momento e o ciclo acabava.