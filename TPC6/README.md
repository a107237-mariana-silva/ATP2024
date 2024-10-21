# Relatório
## Data: 2024-10-21
## Author: Mariana Gonçalves Silva

## Resumo

O TPC5 constituiu na construção de uma aplicação para gestão de alunos dentro de uma certa turma.
A aplicação tinha de coloca no monitor um menu de operações com as seguintes opções: 1 - Criar uma turma; 2 - Inserir um aluno na turma; 3 - Listar a turma; 4 - Consultar um aluno pelo seu id; 5 - Guardar a turma em ficheiro; 6 - Carregar uma turma de um ficheiro; 0 -  Sair da aplicação. No fim de executar uma certa operação, a aplicação tinha decolocar novamente o menu e pedir ao utilizador a opção para continuar. Ainda tinhamos de usar a aplicação para criar uma turma com 5 alunos.

# Contrução das funções

Como nos outros TPCs, defini primeiro todas as minhas funções e testei-as para ver se estavam todas a funcionar corretamente.
As funções que foram mais dificeis de definir foram as de criar um ficheiro e de carregar o mesmo. Para a primeira, decidi separar os alunos por linhas usando o \n, separar nome, id e notas usando | e finalmente separar as notas por &. Tive ainda que colocar int à frente das notas para posteriormente poder recuperar esses valores como inteiros e não como strings. Para a segunda tinha de fazer o split desses mesmos simbolos para poder obter a informaçã como esta contida dentro da turma.

Durante todo o tpc usei o facto de que dois alunos nunca podiam ter o mesmo id. Podem até ter o mesmo nome, que por vezes acontece, no entanto, nas escolas nunca dois alunos possuem o memso id pois esse é unico para cada um. Assim, para inserir um aluno dentro de uma turma, não fui verificar se já existia um aluno dentro da turma com o mesmo nome, mas sim se existia um aluno com o mesmo id. Se sim, então não era possivel inserir o mesmo.
Para além disso, para consultar um aluno usei o mesmo raciocinio sendo então possivel consultar um aluno pelo id e não pelo nome.

Ainda coloquei uma mensagem que aparecia no monitor para dizer ao utilizador que a sua lista estava vazia se queria consultar um aluno sem ter inserido pelo menos um.

# Estrutura da aplicação

A partir do momento em que todas as minhas funções estavam todas corretas, juntei-as todas num ciclo while que iria sempre mostrar no monitor o menu e perguntar ao utilizador a opção que desejava. Se o utilizador não metesse uma das opções que devia então pedia para colocar um numero entre 0 e 7 sendo o 0 a opção sair da aplicação.

# 5 Alunos

Como no final ainda tinhamos de usar a aplicação para criar uma turma com 5 alunos, usei-a e até criei o ficheiro correspondente. O nome dos alunos e a sua inserção na lista estão abaixo das funções para ser mais simples visualizar que alunos temos dentro da turma, qual é o id correspondente a cada um e quais são as suas notas.