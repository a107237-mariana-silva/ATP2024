import json
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random

# Carregar Ficheiro
def carregarFicheiro(fnome):
    f = open("./" + fnome, encoding='utf-8')
    ficheiro = json.load(f)
    return ficheiro

# Inserir Registo
def inserir(lista):
    dict = {}
    abstract = input("Introduza o abstract:")
    if abstract != "":
        dict["abstract"] = abstract
    keyword = input("Introduza palavra(s) chave(s):")
    if keyword != "":
        dict["keywords"] = keyword
    autores = int(input("Quantos autores vai querer introduzir:"))
    lista_autores = []
    while autores > 0 :
        autor = {}
        nameA = input("Introduza o nome do autor:")
        if nameA != "":
            autor["name"] = nameA
        affiliationA = input("Introduza a afiliação do autor:")
        if affiliationA != "":
            autor["affiliation"] = affiliationA
        orcidA = input("Introduza o ORCID do autor:")
        if orcidA != "":
            autor["orcid"] = orcidA
        autores = autores - 1
        lista_autores.append(autor)
    if len(lista_autores) != 0:
        dict["authors"] = lista_autores
    cond1 = True
    while cond1:
        cond2 = False                                # Começamos por dizer que não existe nenhum registo com esse doi                          
        doi = input("Introduza o DOI:")
        for registo in lista:
            if 'doi' in registo and registo['doi'] == doi:
                cond2 = True
        if not cond2:
            dict["doi"] = doi
            cond1 = False
        else:
            print("Pedimos desculpa, mas já existe um registo na nossa base de dados com esse DOI. Por favor, introduza outro DOI.")
    pdf = input("Introduza o link para o pdf:")
    if pdf != "":
        dict["pdf"] = pdf
    date = input("Introduza a data no formato ano-mês-dia:")
    if date != "":
        dict["publish_date"] = date
    cond3 = True
    while cond3:
        cond4 = False                                # Começamos por dizer que não existe nenhum registo com esse titulo                            
        title = input("Introduza o título do registo:")
        for registo in lista:
            if 'title' in registo and registo['title'] == title:
                cond4 = True
        if not cond4:
            dict["title"] = title
            cond3 = False
        else:
            print("Pedimos desculpa, mas já existe um registo na nossa base de dados com esse título. Por favor, introduza outro título.")
    url = input("Introduza o url:")
    if url != "":
        dict["url"] = url
    return lista.append(dict)

# Apagar Registo
def apagarRegisto(lista,doi):
    res = -1                
    encontrado = False
    i = 0
    while not encontrado and i<len(lista):
        if 'doi' in lista[i]:
            if lista[i]['doi'] == doi:
                encontrado = True
                res = i
        i = i + 1
    if encontrado:
        cond = False
        while not cond:
            resposta = input("Tem a certeza que deseja apagar esse registo? Não poderá voltar atrás. Responda com 'S' ou 'N':")
            if resposta == 'S':
                del lista[res]
                cond = True
                return ("O seu registo foi apagado com sucesso.")
            elif resposta == 'N':
                cond = True
                return ("Não houve alterações da base de dados.")
            else:
                print('Resposta inválida.')
    else:
        return ("Pedimos desculpa, mas não foi encontrado nenhum registo com esse DOI.")

# Atualizar um Registo por Titulo
def atualizaTit(lista,titulo,modificacao,x):
    for registo in lista:
        if 'title' in registo and titulo == registo['title']:
            if modificacao == 'T':
                registo['title'] = x
            elif modificacao == 'AB':
                registo['abstract'] = x
            elif modificacao == 'DOI':
                registo['doi'] = x
            elif modificacao == 'PDF':
                registo['pdf'] = x
            elif modificacao == 'URL':
                registo['url'] = x
            elif modificacao == 'DATA':
                registo['publish_date'] = x
            elif modificacao == 'K':
                registo['keywords'] = x
            elif modificacao == 'A':
                nome = input("Insira o nome do autor que deseja acrescentar:")
                afiliacao = input("Insira a afilição do autor:")
                orcid = input("Insira o orcid do autor:")
                autor = {}
                if nome != "":
                    autor["name"] = nome
                if afiliacao != "":
                    autor["affiliation"] = afiliacao
                if orcid != "":
                    autor["orcid"] = orcid
                if 'authors' in registo:
                    registo['authors'].append(autor)
                else:
                    lista_autores = []
                    lista_autores.append(autor)
                    registo['authors'] = lista_autores
            return ("O registo foi modificado com sucesso.")
    return("O registo ao qual está a tentar aceder pode não possuir titulo. Nesse caso, tem de o procurar pelo doi.")

# Atualizar um Registo pelo DOI
def atualizaDoi(lista,doi,modifacao,x):
    for registo in lista:
        if 'doi' in registo and doi == registo['doi']:
            if modifacao == 'T':
                registo['title'] = x
            elif modifacao == 'AB':
                registo['abstract'] = x
            elif modifacao == 'DOI':
                registo['doi'] = x
            elif modifacao == 'PDF':
                registo['pdf'] = x
            elif modifacao == 'URL':
                registo['url'] = x
            elif modifacao == 'DATA':
                registo['publish_date'] = x
            elif modifacao == 'K':
                registo['keywords'] = x
            elif modifacao == 'A':
                nome = input("Insira o nome do autor que deseja acrescentar:")
                afiliacao = input("Insira a afilição do autor:")
                orcid = input("Insira o orcid do autor:")
                autor = {}
                if nome != "":
                    autor["name"] = nome
                if afiliacao != "":
                    autor["affiliation"] = afiliacao
                if orcid != "":
                    autor["orcid"] = orcid
                if 'authors' in registo:
                    registo['authors'].append(autor)
                else:
                    lista_autores = []
                    lista_autores.append(autor)
                    registo['authors'] = lista_autores
            return ("O registo foi modificado com sucesso.")
    return("O registo ao qual está a tentar aceder pode não possuir DOI. Nesse caso, tem de o procurar pelo titulo.")

# Guardar ficheiro -> Guardar Pesquisas
def guardarFicheiro(fnome,lista):
    f = open('./' + fnome, "w")
    json.dump(lista, f)
    f.close()
    return

# Aceder aos Registos de um Determinado Autor -> devolve um url
def acederRegistoAutor(lista,nome):
    lista_de_Registos_Tit = []
    lista_de_Registos_Url = []
    lista_de_Registos_Doi = []
    for registo in lista:
        if "authors" in registo:
            for autor in registo["authors"]:
                if autor['name'] == nome:
                    if 'title' in registo: 
                        lista_de_Registos_Tit.append(registo["title"])
                    else:
                        if 'url' in registo:
                            lista_de_Registos_Url.append(registo["url"])
                        else:
                            lista_de_Registos_Doi.append(registo["doi"])
    lista_final = lista_de_Registos_Tit + lista_de_Registos_Url + lista_de_Registos_Doi
    return "\n\n".join(lista_final) if lista_final else None

def acederURL(lista,nome):
    cond = False
    for registo in lista:
        if "title" in registo and registo['title'] == nome:
            cond = True
            if 'url' in registo:
                resposta = (f"O url desse registo é: {registo['url']}.")
            else:
                resposta = (f"O registo escolhido não possui url. O DOI correspondente é: {registo['doi']}.")
    if cond == False:
        resposta = ("O titulo introduzido não corresponde a nenhum dos que existe dentro da base de dados.")
    return resposta

# Ordenar Registos por Título e por Data
def ordenaTit(registo):
    return registo['title']

def ordena_Data(registo):
    return registo['publish_date']

# Cria Com Titulo
def criaComTitulo(lista):
    comTitulo = []
    for registo in lista:
        if 'title' in registo:
            comTitulo.append(registo)
    return comTitulo

# Consulta Registo por Título
def encontraTit_Data(lista,titulo):              # Não há por titulo porque se houver dois igais, a ordem alfabetica não conta
    registos = []
    registos_comData = []
    registos_semData = []
    registo_final = []
    for registo in lista:
        if titulo == registo["title"]: registos.append(registo)
    for registo in registos:
        if 'publish_date' in registo:
            registos_comData.append(registo)
        else:
            registos_semData.append(registo)
    a = sorted(registos_comData,key=ordena_Data)
    registo_final = a + registos_semData       
    return registo_final

def consultaRegisto_Tit(lista):
    registos = []
    a = 1
    for registo in lista:
        reg = [(f"- - - - - Registo nº {a} - - - - -\n")]
        if 'abstract' in registo:
            reg.append(f"Abstract:{registo['abstract']}\n")
        if 'keywords' in registo:
            reg.append(f"Palavras Chave:{registo['keywords']}\n")
        if 'authors' in registo:
            reg.append(f"Autores:")
            for autor in registo['authors']:
                if 'name' in autor:
                    reg.append(f"Nome: {autor['name']}")
                if 'affiliation' in autor:
                    reg.append(f"Afiliação: {autor['affiliation']}")
                if 'orcid' in autor:
                    reg.append(f"Orcid: {autor['orcid']}")
        if 'doi' in registo:
            reg.append(f"\nDoi:{registo['doi']}\n")
        if 'pdf' in registo:
            reg.append(f"Pdf:{registo['pdf']}\n")
        if 'publish_date' in registo:
            reg.append(f"Data de Publicação:{registo['publish_date']}\n")
        if 'title' in registo:
            reg.append(f"Título:{registo['title']}\n")
        if 'url' in registo:
            reg.append(f"Url:{registo['url']}\n")
        registos.append("\n".join(reg))
        a = a + 1
    return "\n".join(registos) if registos != [] else None

def gravarConsultaTit(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com um determinado título.txt'.")

# Cria Com Autor
def criaComAutor(lista):
    comAutor = []
    for registo in lista:
        if ('authors' in registo) and (registo['authors'] != []):
            comAutor.append(registo)
    return comAutor

# Consulta Registo por Nome do Autor
def encontraAut_Tit(lista,nome_autor):
    registos = []
    registos_comTit = []
    registos_semTit = []
    registo_final = []
    for registo in lista:
        for autor in registo["authors"]:
            if nome_autor == autor["name"]: registos.append(registo)
    for registo in registos:
        if 'title' in registo:
            registos_comTit.append(registo)
        else:
            registos_semTit.append(registo)
    a = sorted(registos_comTit,key=ordenaTit)
    registo_final = a + registos_semTit       
    return registo_final

def encontraAut_Data(lista,nome_autor):
    registos = []
    registos_comData = []
    registos_semData = []
    registo_final = []
    for registo in lista:
        for autor in registo["authors"]:
            if nome_autor == autor["name"]: registos.append(registo)
    for registo in registos:
        if 'publish_date' in registo:
            registos_comData.append(registo)
        else:
            registos_semData.append(registo)
    a = sorted(registos_comData,key=ordena_Data)
    registo_final = a + registos_semData       
    return registo_final

def consultaRegisto_NomeAut(lista):
    registos = []
    a = 1
    for registo in lista:
            reg = [(f"- - - - - Registo nº {a} - - - - -\n")]
            if 'abstract' in registo:
                reg.append(f"Abstract:{registo['abstract']}\n")
            if 'keywords' in registo:
                reg.append(f"Palavras Chave:{registo['keywords']}\n")
            if 'authors' in registo:
                reg.append(f"Autores:")
                for autor in registo['authors']:
                    if 'name' in autor:
                        reg.append(f"Nome: {autor['name']}")
                    if 'affiliation' in autor:
                        reg.append(f"Afiliação: {autor['affiliation']}")
                    if 'orcid' in autor:
                        reg.append(f"Orcid: {autor['orcid']}")
            if 'doi' in registo:
                reg.append(f"\nDoi:{registo['doi']}\n")                  # \n antes porque não conseguimos pôr nos autores uma vez que não sabemos quem tem o quê
            if 'pdf' in registo:
                reg.append(f"Pdf:{registo['pdf']}\n")
            if 'publish_date' in registo:
                reg.append(f"Data de Publicação:{registo['publish_date']}\n")
            if 'title' in registo:
                reg.append(f"Título:{registo['title']}\n")
            if 'url' in registo:
                reg.append(f"Url:{registo['url']}\n")
            registos.append("\n".join(reg))
            a = a + 1
    return "\n".join(registos) if registos != [] else None

def gravarConsultaNome_Tit(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de um autor (ordenados por título).txt'.")

def gravarConsultaNome_Data(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de um autor (ordenados por data).txt'.")

# Consulta Registo por Afiliação do Autor
def encontraAfilAut_Tit(lista,afiliacao):
    registos = []
    registos_comTit = []
    registos_semTit = []
    registo_final = []
    for registo in lista:
        for autor in registo["authors"]:
            if 'affiliation' in autor:                                              # Alguns não possuem afiliação
                if afiliacao == autor["affiliation"]: registos.append(registo)
    for registo in registos:
        if 'title' in registo:
            registos_comTit.append(registo)
        else:
            registos_semTit.append(registo)
    a = sorted(registos_comTit,key=ordenaTit)
    registo_final = a + registos_semTit       
    return registo_final

def encontraAfilAut_Data(lista,afiliacao):
    registos = []
    registos_comData = []
    registos_semData = []
    registo_final = []
    for registo in lista:
        for autor in registo["authors"]:
            if 'affiliation' in autor:
                if afiliacao == autor["affiliation"]: registos.append(registo)
    for registo in registos:
        if 'publish_date' in registo:
            registos_comData.append(registo)
        else:
            registos_semData.append(registo)
    a = sorted(registos_comData,key=ordena_Data)
    registo_final = a + registos_semData       
    return registo_final

def consultaRegisto_AfilAut(lista):
    registos = []
    a = 1
    for registo in lista:
            reg = [(f"- - - - - Registo nº {a} - - - - -\n")]
            if 'abstract' in registo:
                reg.append(f"Abstract:{registo['abstract']}\n")
            if 'keywords' in registo:
                reg.append(f"Palavras Chave:{registo['keywords']}\n")
            if 'authors' in registo:
                reg.append(f"Autores:")
                for autor in registo['authors']:
                    if 'name' in autor:
                        reg.append(f"Nome: {autor['name']}")
                    if 'affiliation' in autor:
                        reg.append(f"Afiliação: {autor['affiliation']}")
                    if 'orcid' in autor:
                        reg.append(f"Orcid: {autor['orcid']}")
            if 'doi' in registo:
                reg.append(f"\nDoi:{registo['doi']}\n")
            if 'pdf' in registo:
                reg.append(f"Pdf:{registo['pdf']}\n")
            if 'publish_date' in registo:
                reg.append(f"Data de Publicação:{registo['publish_date']}\n")
            if 'title' in registo:
                reg.append(f"Título:{registo['title']}\n")
            if 'url' in registo:
                reg.append(f"Url:{registo['url']}\n")
            registos.append("\n".join(reg))
            a = a + 1
    return "\n".join(registos) if registos != [] else None

def gravarConsultaAfil_Tit(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma afiliação (ordenados por título).txt'.")

def gravarConsultaAfil_Data(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma afiliação (ordenados por data).txt'.")

# Cria Com Data de Publicação
def criaComData(lista):
    comData = []
    for registo in lista:
        if 'publish_date' in registo:
            comData.append(registo)
    return comData

# Consulta Registo por Data de Publicação
def encontraDataPub_Tit(lista,data):                 # Não faz sentido ter pela data porque vão ser iguais 
    registos = []
    registos_comTit = []
    registos_semTit = []
    registo_final = []
    for registo in lista:
        if data == registo["publish_date"]: registos.append(registo)
    for registo in registos:
        if 'title' in registo:
            registos_comTit.append(registo)
        else:
            registos_semTit.append(registo)
    a = sorted(registos_comTit,key=ordenaTit)
    registo_final = a + registos_semTit       
    return registo_final

def consultaRegisto_Data(lista):
    registos = []
    a = 1
    for registo in lista:
            reg = [(f"- - - - - Registo nº {a} - - - - -\n")]
            if 'abstract' in registo:
                reg.append(f"Abstract:{registo['abstract']}\n")
            if 'keywords' in registo:
                reg.append(f"Palavras Chave:{registo['keywords']}\n")
            if 'authors' in registo:
                reg.append(f"Autores:")
                for autor in registo['authors']:
                    if 'name' in autor:
                        reg.append(f"Nome: {autor['name']}")
                    if 'affiliation' in autor:
                        reg.append(f"Afiliação: {autor['affiliation']}")
                    if 'orcid' in autor:
                        reg.append(f"Orcid: {autor['orcid']}")
            if 'doi' in registo:
                reg.append(f"\nDoi:{registo['doi']}\n")
            if 'pdf' in registo:
                reg.append(f"Pdf:{registo['pdf']}\n")
            if 'publish_date' in registo:
                reg.append(f"Data de Publicação:{registo['publish_date']}\n")
            if 'title' in registo:
                reg.append(f"Título:{registo['title']}\n")
            if 'url' in registo:
                reg.append(f"Url:{registo['url']}\n")
            registos.append("\n".join(reg))
            a = a + 1
    return "\n".join(registos) if registos != [] else None

def gravarConsultaData(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma determinada data.txt'.")

# Cria Com Palavras Chave
def criaComPalChave(lista):
    comPalChave = []
    for registo in lista:
        if 'keywords' in registo:
            comPalChave.append(registo)
    return comPalChave

# Consulta Registo por Palavras Chave
def encontraPalChave_Tit(lista,pal_chave):
    registos = []
    registos_comTit = []
    registos_semTit = []
    registo_final = []
    for registo in lista:
        if pal_chave in registo["keywords"]: registos.append(registo)       # Meter in porque temos muitas palavras chaves
    for registo in registos:
        if 'title' in registo:
            registos_comTit.append(registo)
        else:
            registos_semTit.append(registo)
    a = sorted(registos_comTit,key=ordenaTit)
    registo_final = a + registos_semTit
    return registo_final

def encontraPalChave_Data(lista,pal_chave):
    registos = []
    registos_comData = []
    registos_semData = []
    registo_final = []
    for registo in lista:
        if pal_chave in registo["keywords"]: registos.append(registo)
    for registo in registos:
        if 'publish_date' in registo:
            registos_comData.append(registo)
        else:
            registos_semData.append(registo)
    a = sorted(registos_comData,key=ordena_Data)
    registo_final = a + registos_semData       
    return registo_final

def consultaRegisto_PalChave(lista):
    registos = []
    a = 1
    for registo in lista:
            reg = [(f"- - - - - Registo nº {a} - - - - -\n")]
            if 'abstract' in registo:
                reg.append(f"Abstract:{registo['abstract']}\n")
            if 'keywords' in registo:
                reg.append(f"Palavras Chave:{registo['keywords']}\n")
            if 'authors' in registo:
                reg.append(f"Autores:")
                for autor in registo['authors']:
                    if 'name' in autor:
                        reg.append(f"Nome: {autor['name']}")
                    if 'affiliation' in autor:
                        reg.append(f"Afiliação: {autor['affiliation']}")
                    if 'orcid' in autor:
                        reg.append(f"Orcid: {autor['orcid']}")
            if 'doi' in registo:
                reg.append(f"\nDoi:{registo['doi']}\n")
            if 'pdf' in registo:
                reg.append(f"Pdf:{registo['pdf']}\n")
            if 'publish_date' in registo:
                reg.append(f"Data de Publicação:{registo['publish_date']}\n")
            if 'title' in registo:
                reg.append(f"Título:{registo['title']}\n")
            if 'url' in registo:
                reg.append(f"Url:{registo['url']}\n")
            registos.append("\n".join(reg))
            a = a + 1
    return "\n".join(registos) if registos != [] else None

def gravarConsultaPalChave_Tit(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com uma determinada palavra-chave (ordenados por título).txt'.")

def gravarConsultaPalChave_Data(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write(lista)
    f.close()
    return ("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com uma determinada palavra-chave (ordenados por data).txt'.")

# Listar os Autores por Ordem Alfabética
def removeAcentos(texto):
    acentos = {
        'á': 'a', 'à': 'a', 'ã': 'a', 'â': 'a', 'ä': 'a',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'í': 'i', 'ì': 'i', 'î': 'i', 'ï': 'i',
        'ó': 'o', 'ò': 'o', 'õ': 'o', 'ô': 'o', 'ö': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u', 'ü': 'u',
        'ç': 'c',
        'Á': 'A', 'À': 'A', 'Ã': 'A', 'Â': 'A', 'Ä': 'A',
        'É': 'E', 'È': 'E', 'Ê': 'E', 'Ë': 'E',
        'Í': 'I', 'Ì': 'I', 'Î': 'I', 'Ï': 'I',
        'Ó': 'O', 'Ò': 'O', 'Õ': 'O', 'Ô': 'O', 'Ö': 'O',
        'Ú': 'U', 'Ù': 'U', 'Û': 'U', 'Ü': 'U',
        'Ç': 'C',
        'Ş': 'S'
    }
    return ''.join(acentos.get(x,x) for x in texto)

def listarAutoresOrdAlf(lista):
    lista_autores = []
    for registo in lista:
        for autor in registo['authors']:
            if autor['name'] not in lista_autores:
                lista_autores.append(autor['name'])
    lista_autores = sorted(lista_autores,key=removeAcentos)
    return lista_autores

def gravarListaOrdAlf(fnome,lista):
    f = open(fnome,"w",encoding="utf-8")
    f.write("- - - - - Lista de Autores por Ordem Alfabética - - - - -\n")
    for autores in lista:
        f.write(f"{autores}\n")
    f.close()
    return ("A sua lista foi guardada num ficheiro sob o nome de:'Lista de Autores por Ordem Alfabética.txt'.")

# Listar os Autores por Frequencia
def OrdenaAutores(lista_autores):
    return lista_autores[1]

def listarAutoresFreq(lista):
    autores={}
    for registo in lista:
        if "authors" in registo:
            for autor in registo['authors']:
                if autor['name'] in autores:
                    autores[autor['name']] = autores[autor['name']] + 1
                elif autor['name'] not in autores:
                    autores[autor['name']] = 1
    aut = sorted(autores.items(), key=OrdenaAutores, reverse=True)
    return aut

def gravarListaAutFreq(fnome, dict):
    f = open(fnome,"w",encoding="utf-8")
    f.write("- - - - - Lista de Autores Por Frequência - - - - -\n")
    f.write("Nome | Nº de artigos\n\n")
    for autores in dict:
        f.write(f"{autores[0]} | {autores[1]}\n")
    f.close()
    return ("A sua lista foi guardada num ficheiro sob o nome de:'Lista de Autores por Frequência.txt'.")

# Listar Palavras-Chave por Ordem Alfabética
def analise_pal_chave_alf(lista):
    palschave={}
    for registo in lista:
        if "keywords" in registo:
            listapc=registo['keywords'].split(', ')
            for pchave in listapc:
                if pchave in palschave:
                    palschave[pchave] = palschave[pchave] + 1
                else:
                    palschave[pchave] = 1
    pc_alf=sorted(palschave.items(),key=lambda x: removeAcentos(x[0].lower()))
    return pc_alf

def gravarPalChaveOrdAlf(fnome, dict):
    f = open(fnome,"w",encoding="utf-8")
    f.write("- - - - - Lista de Palavras-Chave Por Ordem Alfabética - - - - -\n")
    f.write('Palavras-Chave | Nº de Ocorrências\n\n')
    for pc in dict:
        f.write(f"{pc[0]} | {pc[1]}\n")
    f.close()
    return ("A sua lista foi guardada num ficheiro sob o nome de:'Lista de Palavras-Chave por Ordem Alfabética.txt'.")

# Listar Palavras-Chave por Nº de Ocorrências
def analise_pal_chave_ocorr(lista):
    palschave={}
    for registo in lista:
        if "keywords" in registo:
            listapc=registo['keywords'].split(', ')
            for pchave in listapc:
                if pchave in palschave:
                    palschave[pchave] = palschave[pchave] + 1
                else:
                    palschave[pchave] = 1
    pc_alf=sorted(palschave.items(),key=lambda x: x[1],reverse=True)
    return pc_alf

def gravarPalChaveOcorr(fnome, dict):
    f = open(fnome,"w",encoding="utf-8")
    f.write("- - - - - Lista de Palavras-Chave Por Ocorrência - - - - -\n")
    f.write('Palavras-Chave | Nº de Ocorrências\n\n')
    for pc in dict:
        f.write(f"{pc[0]} | {pc[1]}\n")
    f.close()
    return ("A sua lista foi guardada num ficheiro sob o nome de:'Lista de Palavras-Chave por Ocorrência.txt'.")

# Distribuição TOP 20 autores
def autores_top_20(lista):
    autores_20 = {}
    for registo in lista:
        if "authors" in registo:
            for autor in registo['authors']:
                if autor['name'] in autores_20:
                    autores_20[autor['name']] = autores_20[autor['name']] + 1
                elif autor['name'] not in autores_20:
                    autores_20[autor['name']] = 1
    top = sorted(autores_20.items(),key=OrdenaAutores,reverse=True)
    top_20 = top[:20]
    return dict(top_20)

def graf_autores_top20(d):

    valores = list(d.values())
    labels = list(d.keys())

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]

    plt.figure(figsize=(10,10))
    plt.bar(labels,valores,color = cores_2)
    plt.title('Distribuição dos Autores por Frequência')
    plt.ylabel("Nº de Artigos",fontsize=11)
    plt.xticks(rotation=45,ha='right',fontsize=8)

    plt.show()
    return ("")

# Distribuição de publicações por ano
def OrdenaData(lista):
    return lista[0]

def ano(lista):
    distrib = {}
    for registo in lista:
        if "publish_date" in registo:
            ano = registo['publish_date'][:4]
            if ano in distrib:
                distrib[ano] = distrib[ano] + 1
            else:
                distrib[ano] = 1
    d = sorted(distrib.items(),key=OrdenaData,reverse=False)
    return d

def publicacoes_ano(d):

    labels = [item[0] for item in d]
    valores = [item[1] for item in d]

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]

    plt.figure(figsize=(10,10))
    plt.bar(labels,valores,color = cores_2)
    plt.title('Distribuição de Publicações por Ano')
    plt.ylabel("Nº de Publicações",fontsize=11)
    plt.xticks(rotation=45,ha='right',fontsize=8)

    plt.show()
    return ("")

# Distribuição de publicações por mês de um determinado ano
def verificaMesAno(lista,ano):
    registos = []
    for registo in lista:
        if "publish_date" in registo and ano == registo['publish_date'][:4]:
            registos.append(registo)
    return registos if registos else None

def mes(lista):
    meses = {
        "01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
        "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto",
        "09": "Setembro", "10": "Outubro", "11": "Novembro", "12": "Dezembro"
    }
    distrib = {}
    for registo in lista:
        mes_num = registo['publish_date'][5:7]  
        if mes_num in meses:
            mes_nome = meses[mes_num]
            if mes_nome in distrib:
                distrib[mes_nome] = distrib[mes_nome] + 1
            else:
                distrib[mes_nome] = 1
    d = sorted(distrib.items(),key=lambda x: list(meses.values()).index(x[0]),reverse=False)        # Extrai x[0] -> o nome do mês ; Busca a posição desse nome na lista de meses em meses.values()
    return d

def publicacoes_mes(d):

    labels = [item[0] for item in d]
    valores = [item[1] for item in d]

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]

    plt.figure(figsize=(10,10))
    plt.bar(labels,valores,color = cores_2)
    plt.title('Distribuição de Publicações por Ano')
    plt.ylabel("Nº de Publicações",fontsize=11)
    plt.xticks(rotation=45,ha='right',fontsize=8)

    plt.show()
    return ("")

# Distribuição de publicações de um autor por anos
def verificaAutor(lista,nomeA):
    registo_aut = []
    for registo in lista:
        if "authors" in registo:
            for autores in registo['authors']:
                if nomeA == autores['name']:
                    registo_aut.append(registo)
    return registo_aut if registo_aut else None

def verificaPub_Date(lista):
    registo_data = []
    for registo in lista:
        if "publish_date" in registo:
            registo_data.append(registo)
    return registo_data

def pub_autor_ano(lista):
    distrib = {}
    for registo in lista:
        ano = registo['publish_date'][:4] 
        if ano in distrib:
            distrib[ano] = distrib[ano] + 1
        else:
            distrib[ano] = 1
    d = sorted(distrib.items(),key=OrdenaData,reverse=False)
    return d

def graf_pub_autor_ano(d):
    labels = [item[0] for item in d]
    valores = [item[1] for item in d]

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]

    plt.figure(figsize=(10,10))
    plt.bar(labels, valores, color = cores_2)
    plt.title('Distribuição de Publicações de um autor por anos')
    plt.ylabel("Nº de Ocorrências",fontsize=11)
    plt.xticks(rotation=45,ha='right',fontsize=8)
    
    plt.show()
    return ("")

# Distribuição de palavras-chave mais frequente por ano
def verifica_pc_ano(lista,ano):
    listapc_ano=[]
    for registo in lista:
        if "publish_date" in registo:
            if ano==registo['publish_date'][:4]:
                listapc_ano.append(registo)
    return listapc_ano if listapc_ano else None

def pal_chave_ano(lista):
    pal_chave={}
    for registo in lista:
        if "keywords" in registo:
            listapc=registo['keywords'].split(', ')
            for pchave in listapc:
                if pchave in pal_chave:
                    pal_chave[pchave] = pal_chave[pchave] + 1
                else:
                    pal_chave[pchave] = 1
    top_pc_ano = sorted(pal_chave.items(), key=lambda x: x[1],reverse=True)
    top_20_pc_ano = top_pc_ano[:20]
    return dict(top_20_pc_ano)

def graf_palchave_ano(d):

    valores = list(d.values())
    labels = list(d.keys())

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]

    plt.figure(figsize=(10,10))
    plt.bar(labels, valores, color = cores_2)
    plt.title('Distribuição de Palavras-Chave Mais Frequentes')
    plt.ylabel("Nº de Ocorrências",fontsize=11)
    plt.xticks(rotation=20,ha='right',fontsize=8)
    
    plt.show()
    return ("")

# Distribuição de palavras-chave pela sua frequência (top 20 palavras-chave)  NÃO CONSIGO VER!!!
def freq_palchave(lista):
    pc_20 = {}
    for registo in lista:
        if "keywords" in registo:
            listapc=registo['keywords'].split(', ')
            for pchave in listapc:
                if pchave in pc_20:
                    pc_20[pchave] = pc_20[pchave] + 1
                else:
                    pc_20[pchave] = 1
    top_pc = sorted(pc_20.items(), key=lambda x: x[1],reverse=True)
    top_20_pc = top_pc[:20]
    return dict(top_20_pc)

def graf_palchave_top20(d):

    valores = list(d.values())
    labels = list(d.keys())

    cores = list(x for x in ("LightBlue","LightGrey","LightGreen","LightCoral","LightPink","LightYellow","Lavender","MistyRose","PeachPuff","PaleGreen","LemonChiffon","PowderBlue","LavenderBlush","Honeydew","AliceBlue","Seashell","BlanchedAlmond","CornflowerBlue","Thistle","AntiqueWhite","PeachPuff"))
    random.shuffle(cores)
    cores_2 = cores[:len(labels)]
    
    plt.figure(figsize=(10,10))
    plt.bar(labels, valores, color = cores_2)
    plt.title('Distribuição de Palavras-Chave pela Frequência')
    plt.ylabel("Nº de Ocorrências",fontsize=11)
    plt.xticks(rotation=20,ha='right',fontsize=8)
    
    plt.show()
    return ('')