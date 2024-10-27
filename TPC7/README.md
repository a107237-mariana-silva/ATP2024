# Relatório
## Data: 2024-10-xx
## Author: Mariana Gonçalves Silva

## Resumo

O TPC7 constitui na criação de uma aplicação Python que permitia ao utilizador usar todas as funcionalidades pedidas na ficha P7. Nessa ficha, tinhamos um certo modelo para guardar os registos de temperatura e precipitação ao longo de vários dias.

# Criação das Funções

As funções criadas foram as seguintes:
1 - Inserir Dia; 
2 - Ver a Lista;
3 - Calcular a temperatura média de cada dia, dando como resultado uma lista de pares: [(data, temperaturaMédia)]; 
4 - Definir uma função para guardar uma tabela meteorológica num ficheiro de texto;
5 - Definir uma função para carregar uma tabela meteorológica de um ficheiro de texto;
6 - Calcular a temperatura mínima mais baixa registada na tabela, dando como resultado esse valor;
7 - Calcular a amplitude térmica (diferença entre a temperatura máxima e a temperatura mínima) de cada dia, dando como resultado uma lista de pares: [(data, amplitude)];
8 - Calcular o dia em que a precipitação registada teve o seu valor máximo e indica esse valor, dando como resultado o par (data, valor);
9 - Define uma função que recebe uma tabela meteorológica e um limite p e retorna uma lista de pares [(data, precipitação)] correspondente aos dias em que a precipitação foi superior ao mesmo;
10 - Definir uma função que recebe uma tabela meteorológica e um limite p e retorna o maior número consecutivo de dias com precipitação abaixo desse limite;
11 - Definir uma função que recebe uma tabela meteorológica e desenha os gráficos da temperatura mínima, máxima e de pluviosidade;
0 - Sair.

Tive de criar uma função para o utilizador introduzir um dia com a data do mesmo (ano,mês,dia), temperatura mínima registada nesse dia, temperatura máxima registada nesse dia e a precipitação observada nesse dia.
Ainda criei outra função que nos mostrasse a lista e o que tinhamos dentro.
Todas as minhas outras funções somente funcionavam se o utilizador tivesse introduzido pelo menos um dia, caso contrário aparecia no monitor uma mensagem a dizer que a lista estava vazia e que a aplicação não poderia funcionar.
Ainda criei uma opção sair para quando o utilizador queria encerrar a aplicação.


# Construção da Aplicação

Para construir a minha aplicação criei uma ciclo while que funcionava enquanto a minha condição fosse verdadeiro e esta só viria a ser falsa se o utilizador escolhesse a opção 0 que era a opção sair. Nesse caso imprimia uma mensagem no monitor a sinalizar que a aplicação ia encerrar e o ciclo acabava (a condição tornava-se Falsa e o ciclo terminava).
Ainda criei uma opção para quando o utilizador não respondia com nenhuma das opções possiveis e nesse caso aparecia uma mensagem de resposta invalida e as opções possiveis, mostrando novamente o menu.
Para além disso era importante criar uma variavel lista, que correspondia a uma lista inicialmente vazia dentro do ciclo, de modo a guardar a informação para depois poder usar a aplicação corretamente.

É de notar que todos as minhas opções, exceto a 1 (Criar Dia) funcionam, como referido, somente se a lista não estiver vazia. No entanto, a opção 5 funciona, mesmo estando a lista vazia, uma vez que podiamos querer carregar um ficheiro que já existisse.