# Relatório
## Data: 2024-11-03
## Author: Mariana Gonçalves Silva

## Resumo

O TPC8 foi uma conjunção de 3 tpcs.

# TPC1

O primeiro foi a construção de três funções, todas em compreensão.
A primeira foi a mais fácil de fazer e escrevi logo tudo no return.
Na segunda usei o split para o programa somente ver as palavras e não os espaços entre elas e devolvesse então as que tinham mais de 3 letras.
Na terceira também escrevi logo tudo no return e usei a funçã index que me dava o index de cada palavra da lista ao qual somei 1 para não aparecer a posição 0 e começar logo com o 1.

# TPC2

Por sua vez, o segundo tpc2 contitui na contrução de 4 funções.
A primeira foi para mim a mais complicada uma vez que tinha de pensar em como percorrer a minha string com o comprimento da minha substring. Usando o slicing e um ciclo while acaba por ser fácil.
Na segunda, a minha função ia percorrendo a lista toda até encontrar o meu menor e fazia o append desse numero numa nova lista para depois retirar esse mesmo numero da lista original. Fazendo isto num ciclo que funcionava 3 vezes, obtive uma pequena lista dos 3 menores numeros da lista orginal que eu só multipliquei no return. 
Na terceira, como a função tinha de receber um número e fazer a soma dos dois digitos, o que eu fiz foi converter para uma string e fazer um slicing para depois converter novamente para inteiros e os adicionar. Fazendo isto 2 vezes obtemos o resultado pretendido.
A quarta função foi feita usando o index da palavra que queremos procurar pois se fossemos só pela primeira letra e que tinhamos, por acaso, essa mesma letra antes da palavra que queremos, iriamos ter um index inferior ao que queriamos.

# TPC3

Finalmente, o terceiro constitui na criação de uma aplicação Python para gerir uma rede social. Para além das funções que foram pedidas, ainda tive de adicionar algumas para a aplicação funcionar como queria. Criei 3 funções auxiliares para averiguar se existia o post que o utilizador queria procurar; se existia o autor do post que qeuriamos procurar; e se existia o autor do comentário que queriamos procurar. Inseri estas funções noutras funções e caso não exitisse, aparecia uma mensagem no monitor.
Para além disso ainda criei uma função de ids que gerava o número do id automaticamente indo sempre acrescentando 1 ao número anterior e com um p antes. No entanto, isto somente funcionava se a lista da rede social não fosse vazia, caso contrário, o id gerado seria o p1.
Ainda criei uma função para inserir um comentário num certo post pois ao criar o post, os comentarios eram uma lista vazia que se ia preencher há medida que as pessoas iam comentando.
Finalmente criei as minhas funções menu e sair e no menu inseri uma opção para ver a lista e para inserir um comentário num certo post.

Juntei tudo num ciclo que funcionava enquanto a minha condição fosse verdadeira e que somente viria a ser falsa se o utilizador escolhia a opção 0, abrindo também a minha função sair.
Se o utilizador introduzia outra opção que uma das que eram suposto, então aparecia uma mensagem no monitor de resposta incorreta e para escolher um numero entre 0 e 9, voltando a pedir para selecionar uma opção.