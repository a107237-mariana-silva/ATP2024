# TabMeteo = [(Data,TempMin,TempMax,Precipitacao)]    -> Lista de Tuplos
    # Data = (Int,Int,Int)                            -> Tuplo de 3 inteiros
    # TempMin = Float
    # TempMax = Float
    # Precipitacao = Float

tabMeteo1 = [((2022,1,20), 2, 16, 0),((2022,1,21), 1, 13, 0.2), ((2022,1,22), 7, 17, 0.01)]

def verLista(tabMeteo):
    print("- - - - - Lista - - - - -")
    for dia in tabMeteo:
        print(f"Data:{dia[0][2]}/{dia[0][1]}/{dia[0][2]} | Temperatura Mínima: {dia[1]} | Temperatura Máxima: {dia[2]} | Precipitação: {dia[3]}")
    return ("Fim da lista.")

def medias(tabMeteo):
    res = []
    for dia in tabMeteo:
        media = ( dia[1] + dia[2] ) / 2
        tuplo = (dia[0],media)
        res.append(tuplo)
    return res

def guardaFicheiro(t, fnome):
    file = open(fnome,"w")
    for dia in t:
        data,min,max,pre = dia
        ano,mes,dia = data
        registo = f"{ano}-{mes}-{dia} & {min} & {max} & {pre}\n"
        file.write(registo)
    file.close()
    return ("O seu ficheiro foi criado com sucesso.")

def carregaFicheiro(fnome):
    res = []
    file = open(fnome,"r")
    for linha in file:
        linha = linha.strip()
        campos = linha.split("&")
        data,min,max,pre = campos
        ano,mes,dia = data.split("-")
        dia = ((int(ano),int(mes),int(dia)),float(min),float(max),float(pre))
        res.append(dia)
    file.close()
    return res

def tempMin(tabMeteo):
    minima = tabMeteo[0][1]
    for dia in tabMeteo[1:]:
        if dia[1] < minima:
            minima = dia[1]
    return minima

def amplTerm(tabMeteo):
    res = []
    for dia in tabMeteo:
        amplitude = dia[2] - dia[1]
        res.append((dia[0],amplitude))
    return res 

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][2]
    for dia in tabMeteo:
        if dia[2] > max_prec:
            max_prec = dia[2]
            max_data = dia[0]
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for dia in tabMeteo:
        if dia[3] > p:
            res.append((dia[0],dia[3]))
    return res

def maxPeriodo(tabMeteo, p):
    consec_local = 0
    consec_global = 0
    for dia in tabMeteo:
        if dia[3] < p:
            consec_local = consec_local + 1
        else:
            if consec_global < consec_local:
                consec_global = consec_local
            consec_local = 0
    if consec_global < consec_local:
        consec_global = consec_local
    return consec_global

import matplotlib.pyplot as plt

def graf(t):
    datas = [f"{data[0]}-{data[1]}-{data[2]}" for data, *_ in t]
    temps_min = [ min for _, min, *_ in t]
    temps_max = [ max for _, _, max, *_ in t]
    precs = [ prec for _, _, ma_, prec in t]

    plt.plot(datas,temps_min,label="Temp Mínima")
    plt.plot(datas,temps_max,label="Temp Máxima")
    plt.xlabel("Data")
    plt.ylabel("Temperatura (ºC)")
    plt.title("Temperatura Mínima e Máxima")
    plt.legend()
    plt.show()
    
    plt.bar(datas,precs)
    plt.xlabel("Data")
    plt.ylabel("Precipitação (mm)")
    plt.title("Pluviosidade")
    plt.show()

    return lista

def sair():
    return ("Obrigada pela sua preferência. A aplicação irá encerrar.")

def menu():
    print(""" - - - - - MENU - - - - -
1 - Inserir Dia
2 - Ver Lista
3 - Temperatura Média
4 - Guardar Ficheiro
5 - Carregar Ficheiro
6 - Temperatura Minima
7 - Amplitude Térmica
8 - Precipitação Máxima
9 - Precipitação Superior a p
10 - Precipitação Inferior a p
11 - Gráficos
0 - Sair""")


lista = []
cond = True
while cond:
    menu()
    opcao = int(input("Introduza a opção pretendida:"))
    if opcao == 1:
        ano = int(input("Introduza o ano:"))
        mes = int(input("Introduza o mes:"))
        dia = int(input("Introduza o dia:"))
        data = (ano,mes,dia)
        temp_min = float(input("Introduza a temperatura mínima que foi registada nesse dia:"))
        temp_max = float(input("Introduza a temperatura máxima que foi registada nesse dia:"))
        prec = float(input("Intoduza a precipitação registada nesse dia:"))
        dia = (data,temp_min,temp_max,prec)
        lista.append(dia)
        print("Operação realizada com sucesso.")
    elif opcao == 2:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(verLista(lista))
    elif opcao == 3:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(medias(lista))
    elif opcao == 4:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            nome = input("Introduza o nome do ficheiro colocando '.txt' no final:")
            print(guardaFicheiro(lista,str(nome)))
    elif opcao == 5:
            nome = str(input("Introduza o nome do ficheiro colocando '.txt' no final:"))
            print(carregaFicheiro(nome))
    elif opcao == 6:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(tempMin(lista))
    elif opcao == 7:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(amplTerm(lista))
    elif opcao == 8:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(maxChuva(lista))
    elif opcao == 9:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            valor = float(input("Dias em que a precipitação foi maior a:"))
            print(diasChuvosos(lista,valor))
    elif opcao == 10:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            valor = float(input("Dias consecutivos em que a precipitação foi inferior a:"))
            print(maxPeriodo(lista,valor))
    elif opcao == 11:
        if len(lista) == 0:
            print("A sua lista está vazia. Por favor, introduza pelo menos um dia graças à opção 1.")
        else:
            print(graf(lista))
    elif opcao == 0:
        print(sair())
        cond = False
    else:
        print("Resposta invalida. Por favor, introduza um número entre 0 e 11.")