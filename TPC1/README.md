# Relatório
## Data: 2024-09-18
## Author: Mariana Gonçalves Silva

## Resumo

O TP1 constitui na realização de dois exerccios:
* resolver o exercicio 10 do Maze;
* desenhar com o Turtle uma casa, um sol e uma arvore.

# Exercio 10 do Maze
No exercio 10, se analisamos o circuito reparamos que cada vez que chegamos a um cruzamento que tenha caminho para a frente ele tem sempre que dar prioridade a virar à direita e só depois virar à esquerda, caso contrario deve seguir em frente.
Por outro lado, quando não tem caminho pela frente, como acontece no ultimo cruzamento, ele já tem de dar prioridade ao caminho da esquerda.
Nos três primeiros cruzamentos estamos então no primeiro caso: no primeiro como não tem caminho à direito vai para esquerda; no segundo vai então à direita; no terceiro repetimos a situação do primeiro cruzamneto.
No ultimo cruzamento, não havendo caminho para a frente, embora tenho caminhopara a direita, ele vai escolher ir para a esquerda.
Todo este circuito repete-se até chegar ao ponto de partida.

# Casa no Turtle

Aqui, comecei por construir os 4 muros da casa com um loop, desenhando depois a porta e as janelas. Deixei o meu telhado para o fim uma ez que sabia que o telhado tinha de tocar nas pontas superiores da cada e de que os dois lados tinham de ser do mesmo tamanho e cruzar-se a meio da casa. Para isso, usei regras de trigonometria de modo a calcular então o tamanho de um traço. Tinha de adicionar aos 25 que desci 80/cos(45º) pois sabia que metade da casa era 80 e que esse traço fazia 45º com a parte de cima da casa (180º-135º=45º). Acabei por repetir o mesmo calculo para o outro lado.

# Arvore no Turtle

Para a arvore começei por fazer o tronco e fiz depois as folhas. 
Para fazer um circulo bastava avançar até 75 e escrever somente um traço de 1 e a cada vez que o lapis voltava para o centro do tronco, girar de 1º. Repetindo isto 180 vezes temos metade de um circulo, ou seja, a parte de cima da arvore.

# Sol no Turtle

Comecei por desenhar o circulo do Sol e para isso, como foi dito no desenho da arvore basta avançar de 49, desenhar um traço de 1, recuar e rodar de 1º cada vez e ficamos, aqui, com um circulo de raio 50. Como queremos um circulo completo, repetimos estes passos 360 vezes.
Apos isto, rodei de 45 graus para a esquerda e desenhei os 3 traços de cima cada um com 50 (o que nos faz recuar 100 para voltar ao centro), cada um deles com um angulo e 45 entre eles.
Depois de repetir isto 3 vezes e como o lapis está virado para o lado direiro, virei masi uns 45º para a direita e voltei a repetir o mesmo procedimento dentro de outro loop (por isso é que o repetimos 2 vezes uma vez que são os mesmo traços).

