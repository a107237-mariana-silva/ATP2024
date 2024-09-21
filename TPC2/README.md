# Relatório
## Data: 2024-09-21
## Author: Mariana Gonçalves Silva

## Resumo

O TPC2 constituiu em criar um jogo que podia conter duas modalidades:
* O utilizador pensava num numero e o computador tentava adivinhar;
* O computador pensava num numero e o utilizador tentava adivinhar.

# O utilizador pensava num numero e o computador tentava adivinhar

Eu escolhi esta versão do jogo uma vez que era a que me sentia mais confortavel para criar. Uma parte que me deu que pensar foi logo no inicio para pensar como é que o computador ia escolher os numeros, mas depois pensei em como eu faria e obtive logo a minha resposta. Como temos indicios para saber se o numero é maior ou menor basta pegar sempre no numero que está a meio do intervalo. Ora, isso equilivale a fazer uma média que é exatamente o que o computador tinha que fazer.
Para além disso, também tinha de criar uma variavel "tentativa" que ia somando sempre 1 a cada tentativa do computador.
Isto tudo tinha de ser dentro de um loop o que explica o porquê de ter usado a variavel While.
Se a resposta do utilizador era que o numero é maior então o meu menor valor que começou com o 0 tinha de ser substituido pelo valor que deu anteriormente (ao qual eu chamei x). O mesmo acontece se o numero escolhido fosse menor (o numero maior que começou com 100 tinha de tomar o valor x).
Quando o computador encontrar o numero certo, então este iria responder em quantas tentativas conseguiu. No entanto, eu tinha criado uma situação para quando o utilizador não iria responder nenhuma das 3 hipoteses e por isso tinha que subtrair 1 às tentativas se isso acontecesse pois não era nenhuma tentativa.

O mais dificil para mim foi entender bem como iria conseguir criar a minha estrutura pois tinha o pensamento, mas não sabia bem o que usar para conseguir chegar là. Começei por usar uma função, mas percebi rapidamente que era mais facil com um While. Bastava então encontrar uma condição adequada e tinha o meu codigo.