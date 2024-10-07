# Função Menu:

def menu():
    
    print("- - - - - - MENU - - - - - -")
    print("Opção 1 - Criar Lista")
    print("Opção 2 - Ler Lista")
    print("Opção 3 - Soma")
    print("Opção 4 - Média")
    print("Opção 5 - Maior")
    print("Opção 6 - Menor")
    print("Opção 7 - estaOrdenada por ordem crescente")
    print("Opção 8 - estaOrdenada por ordem decrescente")
    print("Opção 9 - Procura um elemento")
    print("Opção 0 - Sair")

from random import randint

# Opção 1 - Criar Lista

def criarL(n):
    if len(listaInterna) != 0:
        listaInterna.clear()
    for n in range(1,n+1):
        num = randint(1,100)
        listaInterna.append(num)
    return (f"A sua lista é: {listaInterna}")

# Opção 2 - Ler Lista

def lerL(n):
    i = 1
    if len(listaInterna) != 0:
        listaInterna.clear()
    for i in range(1,n+1):
        num = int(input(f"Introduza o valor {i} em {n}:"))
        listaInterna.append(num)
        i = i + 1
    return (f"A sua lista é: {listaInterna}")

# Opção 3 - Soma

def somaL(lista):
    soma = 0
    for num in lista:
        soma = soma + num
    return (f"A soma dos elementos da sua lista é: {soma}.")

# Opção 4 - Média

def mediaL(lista):
    soma = 0
    if len(lista) == 0:
        return (0)
    else:
        for num in lista:
            soma = soma + num
            media = soma / len(lista)
        return (f"A média dos elementos da sua lista é: {media}.")

# Opção 5 - Maior

def maiorL(lista):
    maior = lista[0]
    for num in lista[1:]:
        if num > maior:
            maior = num
    return (f"O maior elemento da sua lista é: {maior}.")

# Opção 6 - Menor

def menorL(lista):
    menor = lista[0]
    for num in lista[1:]:
        if num < menor:
            menor = num
    return (f"O menor elemento da sua lista é: {menor}.")

# Opção 7 - estaOrdenada por ordem crescente

def ordemCre(lista):
    menor = lista[0]
    for num in lista[1:]:
        if num < menor:
            return ("NÃO, não está ordenada por ordem crescente.")
    return ("SIM, está ordenada por ordem crescente.")

# Opção 8 - estaOrdenada por ordem decrescente

def ordemDec(lista):
    maior = lista[0]
    for num in lista[1:]:
        if num > maior:
            return ("NÃO, não está ordenada por ordem decrescente.")
    return ("SIM, está ordenada por ordem decrescente.")

# Opção 9 - Procura um elemento

def posicao(lista, elem):
    if elem in lista:
        return (f"O índice do elemento pretendido é: {lista.index(elem)}.")
    else:
        return (-1)

# Opção 0 - Sair

def sair(lista):
    return (f"A sua lista atual é: {lista}. Volte sempre!\n")


print("\nBom dia!\n")

cond = True
listaInterna = []
from random import randint
while cond:
    menu()
    opcao = int(input("Introduza a opção pretendida:"))
    if opcao == 1:
        a = int(input("Introduza quantos elementos quer que a sua lista tenha:"))
        print(criarL(a))
    elif opcao == 2:
        b = int(input("Introduza quantos elementos quer que a sua lista tenha:"))
        print(lerL(b))
    elif opcao == 3:
        print(somaL(listaInterna))
    elif opcao == 4:
        print(mediaL(listaInterna))
    elif opcao == 5:
        print(maiorL(listaInterna))
    elif opcao == 6:
        print(menorL(listaInterna))
    elif opcao == 7:
        print(ordemCre(listaInterna))
    elif opcao == 8:
        print(ordemDec(listaInterna))
    elif opcao == 9:
        d = int(input("Introduza o elemento que quer encontrar na sua lista:"))
        print(posicao(listaInterna,d))
    elif opcao == 0:
        print(sair(listaInterna))
        cond = False
    else:
        print("Resposta invalida...")
        print("Por favor introduza um numero entre 0 e 9.")
