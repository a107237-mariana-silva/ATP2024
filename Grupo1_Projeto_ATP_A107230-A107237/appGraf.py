import app
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random


def sair():
    return ("Aplicação encerrada. Obrigado pela sua visita, volte sempre!")

def menu():
    print("""\n
- - - - - MENU - - - - -
1 - Carregar Ata Médica
2 - Inserir Registo
3 - Apagar Registo pelo DOI
4 - Atualizar um Registo
5 - Guardar Ata Médica
6 - Aceder ao URL de um Registo (a partir de uma lista de registos por Autor)
7 - Consultar Registo por Título
8 - Consultar Registo por Nome de um Autor
9 - Consultar Registo por Afiliação de um Autor
10 - Consultar Registo por Data de Publicação
11 - Consultar Registo por Palavra-Chave
12 - Listar Autores por Ordem Alfabética
13 - Listar Autores por Frequência
14 - Listar Palavras-Chave por Ordem Alfabética
15 - Listar Palavras-Chave por Frequência
16 - Distribuição de Autores por Frequência (Top 20)
17 - Distribuição de Publicações por Ano
18 - Distribuição de Publicações por Mês de um Determinado Ano
19 - Distribuição de Publicações de um Autor por Anos
20 - Distribuição de Palavras-Chave mais Frequente por Ano
21 - Distribuição de Palavras-Chave pela Frequência (Top 20)
0 - Sair\n
""")


# Modelo de memoria
ata_medica = []

# App principal
cond = True
while cond:
    menu()
    opcao = input("Introduza a opção desejada:")
    if opcao == "1":
        ficheiro = input("Introduza o nome do ficheiro que deseja carregar:")
        try:
            ata_medica = app.carregarFicheiro(ficheiro)
            print("O seu ficheiro foi carregado com sucesso.")
        except FileNotFoundError:
            print("Pedimos desculpa, mas esse ficheiro não existe ou não se encontra nesta pasta.")
        except Exception as f:
            print(f"Pedimos desculpa, mas ocorreu um erro ao carregar o ficheiro {f}.")
    elif opcao == "2":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            app.inserir(ata_medica)
            print("O registo foi guardado com sucesso.")
    elif opcao == "3":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            doi = input("Introduza o DOI do registo que deseja apagar:")
            print(app.apagarRegisto(ata_medica,doi))
    elif opcao == "4":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            cond1 = False
            while cond1 == False:
                procura = input("Deseja selecionar o registo que quer atualizar procurando-o pelo título (1) ou pelo DOI (2). Por favor, responda com 1 ou 2:")
                if procura == '1':
                    titulo = input("Introduza o título do registo que deseja modificar:")
                    cond1 = True
                elif procura == '2':
                    doi = input("Introduza o DOI do registo que deseja modificar:")
                    cond1 = True
                else:
                    print("Resposta inválida. Por favor introduza 1 ou 2:")
            cond2 = False
            while cond2 == False:
                modif = input("O que deseja modificar? Abstract (1); Autores (2); DOI (3); Palavras Chaves (4); PDF (5); Data de publicação (6); Título (7); URL (8):")
                if modif == '1':
                    a = 'resumo'
                    modificacao = 'AB'
                    cond2 = True
                elif modif == '2':
                    a = 'autor(e)'
                    modificacao = 'A'
                    cond2 = True
                elif modif == '3':
                    a = 'DOI'
                    modificacao = 'DOI'
                    cond2 = True
                elif modif == '4':
                    a = 'palavras chaves'
                    modificacao = 'K'
                    cond2 = True
                elif modif == '5':
                    a = 'PDF'
                    modificacao = 'PDF'
                    cond2 = True
                elif modif == '6':
                    a = 'data de publicação'
                    modificacao = 'DATA'
                    cond2 = True
                elif modif == '7':
                    a = 'título'
                    modificacao = 'T'
                    cond2 = True
                elif modif == '8':
                    a = 'URL'
                    modificacao = 'URL'
                    cond2 = True
                else:
                    print("Resposta inválida. Por favor, introduza um número entre 1 e 8 inclusive:")
            if modif != '2':
                x = input(f"Introduza o(a) novo(a) {a}:")
            else:
                x = ''
            if procura == '1':
                print(app.atualizaTit(ata_medica,titulo,modificacao,x))
            if procura == '2':
                print(app.atualizaDoi(ata_medica,doi,modificacao,x))
    elif opcao == "5":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            nome = input("Introduza o nome do ficheiro que quer guardar na base de dados:")
            app.guardarFicheiro(nome,ata_medica)
            print(f"O ficheiro {nome} foi guardado na base de dados.")
    elif opcao == '6':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Alguns artigos do autor que irá introduzir poderão não ter título. Nesse caso, será apresentado diretamente o url correspondente ou DOI se este não possuir url.")
            nomeAut = input("Introduza o nome do autor para o qual deseja o(s) registo(s):")
            x = app.acederRegistoAutor(ata_medica,nomeAut)
            if x != None:
                print(x)
                cond = False
                while not cond:
                    escolha = input("Deseja consultar um registo desse autor pelo título? Introduza 'S' ou 'N':")
                    if escolha == 'S':
                        nomeReg = input("Introduza o nome do registo que deseja consultar:")
                        print(app.acederURL(ata_medica,nomeReg))
                        cond = True
                    elif escolha == 'N':
                        cond = True
                    else:
                        print("Resposta inválida. Por favor, responda com as opções referidas.")
            else:
                print("Pedimos desculpa, mas esse autor não existe na nossa base de dados.")
    elif opcao == "7":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem título. Se não o encontrar, por favor, tente com outro parâmetro.")
            title = input("Introduza o titulo do registo que deseja consultar:")
            novaAta = app.criaComTitulo(ata_medica)
            lista = app.encontraTit_Data(novaAta,title)
            registo = app.consultaRegisto_Tit(lista)
            if registo == None:
                print("Pedimos desculpa, mas o título colocado não corresponde a nenhum registo da nossa base de dados ou pode possuir uma incorreção ortográfica.")
            else:
                cond = False
                while cond == False:
                    resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                    if resposta == 'S':
                        cond = True
                        print(app.gravarConsultaTit("Registos com um determinado título.txt",registo))
                    elif resposta == 'N':
                        cond = True
                        print(registo)
                    else:
                        print("Resposta inválida. Por favor, responda com as opções referidas.")
    elif opcao == "8":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem uma lista de autores. Se não o encontrar, por favor, tente com outro parâmetro.")
            nomeAut = input("Introduza o nome do autor do registo que deseja consultar:")
            cond1 = False
            while cond1 == False:
                selecao = input("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)? Por favor, responda com 1 ou 2:")
                if selecao == '1':
                    cond1 = True
                    novaAta = app.criaComAutor(ata_medica)
                    lista = app.encontraAut_Tit(novaAta,nomeAut)
                    registo = app.consultaRegisto_NomeAut(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas se esse autor tiver escrito um registo da nossa base de dados não está referenciado ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond2 = False
                        while cond2 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond2 = True
                                print(app.gravarConsultaNome_Tit("Registos de um autor (ordenados por título).txt",registo))
                            elif resposta == 'N':
                                cond2 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                elif selecao == '2':
                    cond1 = True
                    novaAta = app.criaComAutor(ata_medica)
                    lista = app.encontraAut_Data(novaAta,nomeAut)
                    registo = app.consultaRegisto_NomeAut(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas se esse autor tiver escrito um registo da nossa base de dados não está referenciado ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond2 = False
                        while cond2 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond2 = True
                                print(app.gravarConsultaNome_Data("Registos de um autor (ordenados por data).txt",registo))
                            elif resposta == 'N':
                                cond2 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                else:
                    print("Resposta inválida, por favor, introduza '1' ou '2'.")
    elif opcao == '9':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem uma lista de autores. Se não o encontrar, por favor, tente com outro parâmetro.")
            afiliacao = input("Introduza a afiliação do autor do registo que deseja consultar:")
            cond = False
            while cond == False:
                selecao = input("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)? Por favor, responda com 1 ou 2:")
                if selecao == '1':
                    cond = True
                    novaAta = app.criaComAutor(ata_medica)
                    lista = app.encontraAfilAut_Tit(novaAta,afiliacao)
                    registo = app.consultaRegisto_AfilAut(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas se esse autor tiver escrito um registo da nossa base de dados não está referenciado ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond1 = False
                        while cond1 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond1 = True
                                print(app.gravarConsultaAfil_Tit("Registos de uma afiliação (ordenados por título).txt",registo))
                            elif resposta == 'N':
                                cond1 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                elif selecao == '2':
                    cond = True
                    novaAta = app.criaComAutor(ata_medica)
                    lista = app.encontraAfilAut_Data(novaAta,afiliacao)
                    registo = app.consultaRegisto_AfilAut(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas se esse autor tiver escrito um registo da nossa base de dados não está referenciado ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond2 = False
                        while cond2 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond2 = True
                                print(app.gravarConsultaAfil_Data("Registos de uma afiliação (ordenados por data).txt",registo))
                            elif resposta == 'N':
                                cond2 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                else:
                    print("Resposta inválida, por favor, introduza '1' ou '2'.")
    elif opcao == "10":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem data de publicação. Se não o encontrar, por favor, tente com outro parâmetro.")
            data = str(input("Introduza a data de publicação do registo que deseja consultar sob a forma de ano-mês-dia:"))
            novaAta = app.criaComData(ata_medica)
            lista = app.encontraDataPub_Tit(novaAta,data)
            registo = app.consultaRegisto_Data(lista)
            if registo == None:
                print("Pedimos desculpa, mas a data colocada não corresponde a nenhum registo da nossa base de dados ou pode possuir uma incorreção ortográfica.")
            else:
                cond = False
                while cond == False:
                    resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                    if resposta == 'S':
                        cond = True
                        print(app.gravarConsultaData("Registos de uma determinada data.txt",registo))
                    elif resposta == 'N':
                        cond = True
                        print(registo)
                    else:
                        print("Resposta inválida. Por favor, responda com as opções referidas.")
    elif opcao == "11":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem palavras-chave ou podem estar incompletas. Se não o encontrar, por favor, tente com outro parâmetro.")
            pal_chave = str(input("Introduza a palavra-chave do registo que deseja consultar:"))
            cond = False
            while cond == False:
                selecao = input("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)? Por favor, responda com 1 ou 2:")
                if selecao == '1':
                    cond = True
                    novaAta = app.criaComPalChave(ata_medica)
                    lista = app.encontraPalChave_Tit(novaAta,pal_chave)
                    registo = app.consultaRegisto_PalChave(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas nenhum registo da nossa base de dados possui essa palavra chave ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond1 = False
                        while cond1 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond1 = True
                                print(app.gravarConsultaPalChave_Tit("Registos com uma determinada palavra-chave (ordenados por título).txt",registo))
                            elif resposta == 'N':
                                cond1 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                elif selecao == '2':
                    cond = True
                    novaAta = app.criaComPalChave(ata_medica)
                    lista = app.encontraPalChave_Data(novaAta,pal_chave)
                    registo = app.consultaRegisto_PalChave(lista)
                    if registo == None:
                        print("Pedimos desculpa, mas nenhum registo da nossa base de dados possui essa palavra chave ou pode possuir uma incorreção ortográfica.")
                    else:
                        cond2 = False
                        while cond2 == False:
                            resposta = input("Deseja guardar a informação consultada num ficheiro? Por favor, responda com: 'S' ou 'N':")
                            if resposta == 'S':
                                cond2 = True
                                print(app.gravarConsultaPalChave_Data("Registos com uma determinada palavra-chave (ordenados por data).txt",registo))
                            elif resposta == 'N':
                                cond2 = True
                                print(registo)
                            else:
                                print("Resposta inválida. Por favor, responda com as opções referidas.")
                else:
                    print("Resposta inválida, por favor, introduza '1' ou '2'.")
    elif opcao == "12":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            a = app.listarAutoresOrdAlf(ata_medica)
            cond = False
            while cond == False:
                resposta = input("Deseja guardar a sua lista num ficheiro? Por favor, responda com: 'S' ou 'N'.")
                if resposta == 'S':
                    cond = True
                    print(app.gravarListaOrdAlf("Lista de Autores por Ordem Alfabética.txt",a))
                elif resposta == 'N':
                    cond = True
                    print("- - - - - Lista de Autores Por Ordem Alfabética - - - - -\n\n")
                    for autores in a:
                        print(f"{autores}\n")
                else:
                    print("Resposta inválida. Por favor, introduza 'S' ou 'N'.")
    elif opcao == "13":
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            a = app.listarAutoresFreq(ata_medica)
            cond = False
            while cond == False:
                resposta = input("Deseja guardar a sua lista num ficheiro? Por favor, responda com: 'S' ou 'N'.")
                if resposta == 'S':
                    cond = True
                    print(app.gravarListaAutFreq("Lista de Autores por Frequência.txt",a))
                elif resposta == 'N':
                    cond = True
                    print("- - - - - Lista de Autores Por Frequência - - - - -\n")
                    print("Nome | Nº de Artigos\n\n")
                    for autores in a:
                        print(f"{autores[0]} | {autores[1]}\n")
                else:
                    print("Resposta inválida. Por favor, introduza 'S' ou 'N'.")
    elif opcao == '14':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            a = app.analise_pal_chave_alf(ata_medica)
            cond = False
            while cond == False:
                resposta = input("Deseja guardar a sua lista num ficheiro? Por favor, responda com: 'S' ou 'N'.")
                if resposta == 'S':
                    cond = True
                    print(app.gravarPalChaveOrdAlf("Lista de Palavras-Chave por Ordem Alfabética.txt",a))
                elif resposta == 'N':
                    cond = True
                    print("- - - - - Lista de Palavras-Chave por Ordem Alfabética - - - - -\n")
                    print("'Palavras-Chave | Nº de Ocorrências\n\n'")
                    for pc in a:
                        print(f"{pc[0]} | {pc[1]}\n")
                else:
                    print("Resposta inválida. Por favor, introduza 'S' ou 'N'.")
    elif opcao == '15':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            a = app.analise_pal_chave_ocorr(ata_medica)
            cond = False
            while cond == False:
                resposta = input("Deseja guardar a sua lista num ficheiro? Por favor, responda com: 'S' ou 'N'.")
                if resposta == 'S':
                    cond = True
                    print(app.gravarPalChaveOcorr("Lista de Palavras-Chave Por Ocorrência.txt",a))
                elif resposta == 'N':
                    cond = True
                    print("- - - - - Lista de Palavras-Chave Por Ocorrência - - - - -\n")
                    print("'Palavras-Chave | Nº de Ocorrências\n\n'")
                    for pc in a:
                        print(f"{pc[0]} | {pc[1]}\n")
                else:
                    print("Resposta inválida. Por favor, introduza 'S' ou 'N'.")
    elif opcao == '16':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            top_20 = app.autores_top_20(ata_medica)
            print(app.graf_autores_top20(top_20))
    elif opcao == '17':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao usar esta distribuição, pode não aparecer o nº total de artigos, uma vez que alguns registos não possuem data de publicação.")
            anos = app.ano(ata_medica)
            print(app.publicacoes_ano(anos))
    elif opcao == '18':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao usar esta distribuição, pode não aparecer o nº total de artigos escritos, uma vez que alguns registos não possuem data de publicação.")
            ano = input("Introduza o ano das publicações:")
            lista_ano = app.verificaMesAno(ata_medica,ano)
            if lista_ano == None:
                print("Pedimos desculpa, mas não existe nenhum artigo da base de dados com esse ano de publicação.")
            else:
                distrib_meses = app.mes(lista_ano)
                print(app.publicacoes_mes(distrib_meses))
    elif opcao == '19':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao usar esta distribuição, pode não aparecer o nº total de artigos escritos pelo autor selecionado, uma vez que alguns registos não possuem data de publicação.")
            nome = input('Introduza o nome do autor:')
            lista_aut = app.verificaAutor(ata_medica,nome)
            if lista_aut == None:
                print("Pedimos desculpa, mas esse autor não escreveu nenhum artigo da base de dados.")
            else:
                lista_d=app.verificaPub_Date(lista_aut)
                final=app.pub_autor_ano(lista_d)
                print(app.graf_pub_autor_ano(final))
    elif opcao == '20':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            print("Ao usar esta distribuição, pode não aparecer o nº total de artigos escritos, uma vez que alguns registos não possuem data de publicação.")
            ano = input("Introduza o ano de publicação:")
            lista_pc_ano = app.verifica_pc_ano(ata_medica,ano)
            if lista_pc_ano == None:
                print("Pedimos desculpa, mas não existe nenhum artigo da base de dados com esse ano de publicação.")
            else:
                top_20_pc = app.pal_chave_ano(lista_pc_ano)
                print(app.graf_palchave_ano(top_20_pc))
    elif opcao == '21':
        if len(ata_medica) == 0:
            print("Pedimos desculpa, mas não existe nenhum ficheiro carregado. Tem de usar primeiro a opção 1.")
        else:
            top_20_pc = app.freq_palchave(ata_medica)
            print(app.graf_palchave_top20(top_20_pc))
    elif opcao == '0':
        cond = False
        print(sair())
    else:
        print("A opção que introduziu não é válida. Por favor, escolha uma opção entre 0 e ...")