# Relatório
## Data: 2024-10-15
## Author: Mariana Gonçalves Silva

## Resumo

O TPC4 constituiu numa aplicação para gerir um cinema. Tinhamos de desenvolver uma aplicacão para gestão de um conjunto de salas de cinema de um centro comercial. Existiam varias salas de cinema, cada uma com uma determinada lotação, uma lista com a referência dos bilhetes vendidos e onde cada sala tem um filme associado.

# Definir as Funções

O meu primeiro passo foi definir todas as minhas funções, as que foram pedidas e as que achei necessárias.
Para além das que foram pedidas, criei uma função para saber se existem salas com o mesmo filme a ser exibido que me foi necessária para a função inserir sala uma vez que tinhamos que verificar se já exitia.
Criei também uma função reembolso que permitia a um lugar que estava na categoria dos vendidos passar para a categoria dos lugares que estão disponiveis, uma vez que o bilhete foi reembolsado e está novamente disponivel.
Ainda criei uma função vendidos para saber que lugares estavam vendidos para ver um certo filme numa certa sala.
Finalmente, criei uma função sair que mostrava uma mensagem final para quando o utilizador cria sair da aplicação, fazendo acabar o ciclo. Ainda criei uma função menu para apresentar todas as opções possiveis que podem ser escolhidas pelo utilizador.

# Aplicação

No final de ter todas as minhas funções e de já as ter testado, coloquei tudo dentro de um ciclo while com cada opção correspondente a uma função. Esse ciclo funcionava enquanto que a minha condição fosse verdadeira e só se tornava falsa quando a função sair fosse solicitada. Para além disso, introduzi um else para quando o utilizador não colocava uma das opções possiveis e repetia a pergunta.