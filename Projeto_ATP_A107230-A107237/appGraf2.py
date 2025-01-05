import app
import FreeSimpleGUI as sg

sg.theme("LightBlue")
ata_medica = []

# Definir o layout 
layout = [
    [sg.Text('MENU', justification = 'center', size=(40, 1), font=('Calibri Light', 18))],
    [
        sg.Button('Carregar Ata Médica', key="-CARREGAR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Inserir Registo', key="-INSERIR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Apagar Registo por DOI', key="-APAGAR-", size=(22, 2), font=('Calibri Light', 15))
    ],
    [
        sg.Button('Atualizar', key="-ATUALIZAR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Guardar Ata Médica', key="-GUARDAR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Aceder ao URL/DOI', key="-ACEDE-URL-", size=(22, 2), font=('Calibri Light', 15))
    ],
    [
        sg.Button('Consultar', key="-CONSULTAR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Listar', key="-LISTAR-", size=(22, 2), font=('Calibri Light', 15)),
        sg.Button('Distribuições', key="-DISTRIB-", size=(22, 2), font=('Calibri Light', 15))
    ],
    [sg.Push(),sg.Button('SAIR', key="-SAIR-", size=(8, 2),font=('Calibri Light', 15))]
]

# Criar a janela principal
window = sg.Window('Interface Gráfica', layout, element_justification = 'center', font=('Calibri Light', 15))

# Carregar ata médica
def carregar():
    layout=[
        [sg.Text("Introduza o nome do ficheiro que deseja carregar:"), sg.InputText(key="-FICHEIRO-", size=(40, 1))],
        [sg.Button("Carregar"), sg.Button("Cancelar")]
    ]
    window=sg.Window('Carregar Ata Médica',layout,font=('Calibri Light', 15))
    ata_medica = []
    stop = False
    while not stop:
        event, values = window.read()  # Captura o evento e os valores
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop = True
        elif event == "Carregar":
            ficheiro=values["-FICHEIRO-"]
            if ficheiro:
                try:
                    ata_medica = app.carregarFicheiro(ficheiro)
                    sg.popup("O seu ficheiro foi carregado com sucesso!",title="Sucesso")
                except FileNotFoundError:
                    sg.popup_error("Erro", "Pedimos desculpa, mas esse ficheiro não existe ou não se encontra nesta pasta.",title="Erro")
                except Exception as e:
                    sg.popup_error("Erro", f"Pedimos desculpa, mas ocorreu um erro ao carregar o ficheiro: {e}",title="Erro")
        else:
            sg.popup_error("Erro", "Por favor, insira o nome do ficheiro.",title="Erro")
        window.close()
    return ata_medica

# Inserir registo                                                             
def inserirReg(lista):
    layout_ins = [
        [sg.Text("Introduza o abstract:"), sg.InputText(key="-ABSTRACT-")],
        [sg.Text("Introduza palavra(s) chave(s):"), sg.InputText(key="-KEYWORDS-")],
        [sg.Text("Quantos autores deseja inserir?"), sg.InputText(key="-NUM_AUTORES-", size=(5, 1),enable_events=True)],
        [sg.Button("Adicionar Autores"), sg.Text("", size=(40, 1), key="-AD_AUTORES-")],
        [sg.Text("Introduza o DOI:"), sg.InputText(key="-DOI-")],
        [sg.Text("Introduza o link para o PDF:"), sg.InputText(key="-PDF-")],
        [sg.Text("Introduza a data (ano-mês-dia):"), sg.InputText(key="-PUBLISH_DATE-",enable_events=True)],
        [sg.Text("Introduza o título do registo:"), sg.InputText(key="-TITLE-")],
        [sg.Text("Introduza o URL:"), sg.InputText(key="-URL-")],
        [sg.Button("Inserir"), sg.Button("Cancelar")]
    ]

    window = sg.Window("Inserir Registo", layout_ins,font=('Calibri Light', 15))

    autores=[]
    stop = False
    while not stop:
        event, values = window.read() 
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop = True
        if event=='-NUM_AUTORES-':
            if len(values['-NUM_AUTORES-']) == 1 and values['-NUM_AUTORES-'][0] not in '0123456789':
                window['-NUM_AUTORES-'].update(values['-NUM_AUTORES-'][:-1])
            elif len(values['-NUM_AUTORES-']) > 1 and values['-NUM_AUTORES-'][-1] not in '0123456789':
                window['-NUM_AUTORES-'].update(values['-NUM_AUTORES-'][:-1])
            
        if event == "Adicionar Autores":
            if not values["-NUM_AUTORES-"]:
                sg.popup("Por favor, selecione o número de autores antes de adicionar.",title="Número de Autores")
            else:
                num_autores = int(values["-NUM_AUTORES-"][0])
                for _ in range(num_autores):
                    autor_layout = [
                        [sg.Text("Introduza o nome do autor:"), sg.InputText(key="-NAME-")],
                        [sg.Text("Introduza a afiliação do autor:"), sg.InputText(key="-AFFILIATION-")],
                        [sg.Text("Introduza o ORCID do autor:"), sg.InputText(key="-ORCID-")],
                        [sg.Button("Inserir Autor"), sg.Button("Cancelar")]
                    ]
                    autor_window = sg.Window("Adicionar Autor", autor_layout,font=('Calibri Light', 15))
                    stop2=False
                    while not stop2:
                        autor_event, autor_values = autor_window.read()
                        
                        if autor_event == sg.WINDOW_CLOSED or autor_event == "Cancelar":
                            autor_window.close()
                            stop2=True
                        
                        if autor_event == "Inserir Autor":
                            autor = {}
                            if autor_values["-NAME-"]:
                                autor["name"] = autor_values["-NAME-"]
                            if autor_values["-AFFILIATION-"]:
                                autor["affiliation"] = autor_values["-AFFILIATION-"]
                            if autor_values["-ORCID-"]:
                                autor["orcid"] = autor_values["-ORCID-"]
                            autores.append(autor)
                            sg.popup("Autor adicionado com sucesso!",title="Sucesso")
                            autor_window.close()
                            stop2=True
        if event== "-PUBLISH_DATE-":
            data=values["-PUBLISH_DATE-"]
            if len(data) > 0 and data[-1] not in '0123456789-':
                window['-PUBLISH_DATE-'].update(data[:-1])
            if len(data) == 5 and data[4] != '-':
                window['-PUBLISH_DATE-'].update(data[:-1]) 
            elif len(data) == 8 and data[7] != '-':
                window['-PUBLISH_DATE-'].update(data[:-1])
            if len(data) >= 7:
                mes = int(data[5:7]) if data[5:7].isdigit() else 0
                if mes < 1 or mes > 12:
                    window["-PUBLISH_DATE-"].update(data[:5])  

            if len(data) == 10:
                dia = int(data[8:10]) if data[8:10].isdigit() else 0
                if dia < 1 or dia > 31:
                    window["-PUBLISH_DATE-"].update(data[:8])

            if len(data) > 10:
                window['-PUBLISH_DATE-'].update(data[:-1])

        if event == "Inserir":
            doi = values["-DOI-"]
            title = values["-TITLE-"]

            doi_existe = False
            for registo in lista:
                if "doi" in registo and registo["doi"] == doi:
                    doi_existe = True
            
            if doi_existe:
                sg.popup_error("Já existe um registo com este DOI. Insira outro.",title="Erro")
                window["-DOI-"].update('')
            else:
                titulo_existe = False
                for registo in lista:
                    if "title" in registo and registo["title"] == title:
                        titulo_existe = True
                
                if titulo_existe:
                    sg.popup_error("Já existe um registo com este título. Insira outro.",title="Erro")
                    window["-TITLE-"].update('')
                else:
                    dict = {}
                    if values["-ABSTRACT-"]:
                        dict["abstract"] = values["-ABSTRACT-"]
                    if values["-KEYWORDS-"]:
                        dict["keywords"] = values["-KEYWORDS-"]
                    if autores:
                        dict["authors"] = autores
                    if values["-DOI-"]:
                        dict["doi"] = doi
                    if values["-PDF-"]:
                        dict["pdf"] = values["-PDF-"]
                    if values["-PUBLISH_DATE-"]:
                        dict["publish_date"] = values["-PUBLISH_DATE-"]
                    if values["-TITLE-"]:
                        dict["title"] = title
                    if values["-URL-"]:
                        dict["url"] = values["-URL-"]
                    
                    lista.append(dict)
                    sg.popup("Registo inserido com sucesso!",title="Sucesso")
                    stop=True
    window.close()
    
# Guardar ficheiro
def guardarAta():
    layout=[
        [sg.Text("Nome do ficheiro que quer guardar:"), sg.InputText(key="-NOME-")],
        [sg.Button("Guardar"), sg.Button("Cancelar",key='-SAIR-')]

    ]
    window=sg.Window('Guardar Ata Médica',layout,font=('Calibri Light', 15))
    stop = False
    while not stop:
        event, values = window.read()  
        if event == sg.WINDOW_CLOSED or event == "-SAIR-":
            stop = True
        elif event == "Guardar":
            nome=values['-NOME-']
            if len(nome) < 5 or nome[-5:] != ".json":  
                sg.popup_error("Por favor, introduza um nome do tipo '.json'. Tente novamente.",title="Erro")
            else:
                try:
                    app.guardarFicheiro(nome, ata_medica)  
                    sg.popup("Ficheiro guardado com sucesso!", title="Sucesso")
                    stop = True  
                except Exception as e:
                    sg.popup_error(f"Erro ao guardar o ficheiro: {e}", title="Erro")
    window.close()

# Apagar registo 
def apagarRegisto(lista):
    layout = [
        [sg.Text("Digite o DOI do registo que deseja apagar:")],
        [sg.InputText(key="-DOI-")],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]
    window = sg.Window("Apagar Registo", layout,font=('Calibri Light', 15))

    stop=False
    while not stop:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop=True  

        if event == "Ok":
            doi = values["-DOI-"]
            if not doi:
                sg.popup_error("Por favor, insira um DOI válido.", title="Erro")
            else:
                encontrado = False
                for i in range(len(lista)):
                    if "doi" in lista[i] and lista[i]["doi"] == doi:
                        encontrado = True
                        stop=True

                if encontrado:
                    layout_confirma = [
                        [sg.Text(f"Tem a certeza que deseja apagar o registo com o DOI: '{doi}'?")],
                        [sg.Button("Sim"), sg.Button("Não")]
                    ]
                    window_confirma = sg.Window("Confirmação", layout_confirma,font=('Calibri Light', 15))
                    stop2=False
                    while not stop2:
                        confirm_event, _ = window_confirma.read()
                        if confirm_event == sg.WINDOW_CLOSED:
                            window_confirma.close()
                            stop2=True

                        elif confirm_event == "Sim":
                            del lista[i]
                            window_confirma.close()
                            sg.popup("O seu registo foi apagado com sucesso.", title="Sucesso", button_type=sg.POPUP_BUTTONS_OK)
                            stop2=True

                        elif confirm_event == "Não":
                            window_confirma.close()
                            sg.popup("Não foi apagado nenhum registo.", title="Cancelar", button_type=sg.POPUP_BUTTONS_OK)
                            stop2=True
                else:
                    sg.popup_error("Pedimos desculpa, mas não foi encontrado nenhum registo com esse DOI.", title="Erro")
                    window['-DOI-'].update("")
    window.close()

# Atualizar
def atualiza(lista):
    layout_procura = [
        [sg.Text("Deseja procurar o registo por Título ou DOI?")],
        [sg.Radio("Título", "PROCURAR", key='-TITULO-'), 
         sg.Radio("DOI", "PROCURAR", key='-DOI-')],
        [sg.Button("Ok"), sg.Button("Cancelar")]
    ]

    window_procura = sg.Window("Procurar Registo", layout_procura, font=('Calibri Light', 15))

    procura_opcao = None
    stop = False
    while not stop:
        event, values = window_procura.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop = True
        elif values['-TITULO-']: 
            procura_opcao = "titulo"
            stop = True
        elif values['-DOI-']:  
            procura_opcao = "doi"
            stop = True
    window_procura.close()

    # Obter Título ou DOI do registo
    if procura_opcao == "titulo":
        layout_titulo = [
            [sg.Text("Introduza o título do registo que deseja modificar:")],
            [sg.InputText(key="-TITULO-")],
            [sg.Button("Ok"), sg.Button("Cancelar")]
        ]
        window_titulo = sg.Window("Procura pelo Título", layout_titulo, font=('Calibri Light', 15))
        stop2 = False
        while not stop2:
            event, values = window_titulo.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                stop2 = True
            elif event == "Ok":
                titulo = values["-TITULO-"]
                cond=True
                i=0
                while cond and i<len(ata_medica):
                    for registo in ata_medica:
                        if 'title' in registo and titulo==registo['title']:
                            cond=False
                            stop2 = True
                        i=i+1
                if cond:
                    sg.popup_error("Por favor, insira um título válido.", title="Erro")
        window_titulo.close()

    elif procura_opcao == "doi":
        layout_doi = [
            [sg.Text("Introduza o DOI do registo que deseja modificar:")],
            [sg.InputText(key="-DOI-")],
            [sg.Button("Ok"), sg.Button("Cancelar")]
        ]
        window_doi = sg.Window("Procura pelo DOI", layout_doi, font=('Calibri Light', 15))
        stop3 = False
        while not stop3:
            event, values = window_doi.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                stop3 = True
            elif event == "Ok":
                doi = values["-DOI-"]
                cond=True
                i=0
                while cond and i<len(ata_medica):
                    for registo in ata_medica:
                        if 'doi' in registo and doi==registo['doi']:
                            cond=False
                            stop3 = True
                        i=i+1
                if cond:
                    sg.popup_error("Por favor, insira um DOI válido.", title="Erro")
        window_doi.close()

    layout_modificacao = [
        [sg.Text("O que deseja modificar?")],
        [sg.Button("Abstract"), sg.Button("Autores"), sg.Button("DOI"),
         sg.Button("Palavras-chave"), sg.Button("PDF"), sg.Button("Data de Publicação"),
         sg.Button("Título"), sg.Button("URL")],
        [sg.Push(),sg.Button("Cancelar")]
    ]
    window_modificacao = sg.Window("Selecionar Modificação", layout_modificacao, font=('Calibri Light', 15))

    modificacao = None
    stop4 = False
    while not stop4:
        event, _ = window_modificacao.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop4 = True
        elif event in ["Abstract", "Autores", "DOI", "Palavras-chave", "PDF", "Data de Publicação", "Título", "URL"]:
            modificacao = event
            stop4 = True
    window_modificacao.close()

    # Obter valor novo para modificação
    if modificacao == "Autores":
        layout_autor = [
            [sg.Text("Introduza os dados do novo autor:")],
            [sg.Text("Nome:"), sg.InputText(key="-NOME-")],
            [sg.Text("Afiliação:"), sg.InputText(key="-AFILIACAO-")],
            [sg.Text("ORCID:"), sg.InputText(key="-ORCID-")],
            [sg.Button("Ok"), sg.Button("Cancelar")]
        ]
        window_autor = sg.Window("Adicionar Autor", layout_autor, font=('Calibri Light', 15))
        stop6 = False
        while not stop6:
            event, values = window_autor.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                stop6 = True
            elif event == "Ok":
                novo_valor={}
                nome = values["-NOME-"]
                afiliacao = values["-AFILIACAO-"]
                orcid = values["-ORCID-"]
                if nome:
                    novo_valor['name']=nome
                if afiliacao:
                    novo_valor['affiliation']=afiliacao
                if orcid:
                    novo_valor['orcid']=orcid
                stop6 = True
        window_autor.close()
    elif modificacao in ["Abstract","DOI", "Palavras-chave", "PDF", "Data de Publicação", "Título", "URL"]:
        layout_valor = [
            [sg.Text(f"Introduza o novo valor para {modificacao}:")],
            [sg.InputText(key="-VALOR-")],
            [sg.Button("Ok"), sg.Button("Cancelar")]
        ]
        window_valor = sg.Window("Introduzir Novo Valor", layout_valor, font=('Calibri Light', 15))
        stop5 = False
        while not stop5:
            event, values = window_valor.read()
            if event == sg.WINDOW_CLOSED or event == "Cancelar":
                stop5 = True
            elif event == "Ok":
                novo_valor = values["-VALOR-"]
                if novo_valor:
                    stop5 = True
                else:
                    sg.popup_error("Por favor, insira um valor válido.", title="Erro")
        window_valor.close()
    
    # Atualizar o registo
    for registo in lista:
        if (procura_opcao == "titulo" and registo.get('title') == titulo) or (procura_opcao == "doi" and registo.get('doi') == doi):
            if modificacao == 'Título':
                registo['title'] = novo_valor
            elif modificacao == 'Abstract':
                registo['abstract'] = novo_valor
            elif modificacao == 'DOI':
                registo['doi'] = novo_valor
            elif modificacao == 'PDF':
                registo['pdf'] = novo_valor
            elif modificacao == 'URL':
                registo['url'] = novo_valor
            elif modificacao == 'Data de Publicação':
                registo['publish_date'] = novo_valor
            elif modificacao == 'Palavras-chave':
                registo['keywords'] = novo_valor
            elif modificacao == 'Autores':
                autor = novo_valor
                if 'authors' in registo:
                    registo['authors'].append(autor)
                else:
                    registo['authors'] = [autor]
            sg.popup("O registo foi modificado com sucesso.", title="Sucesso")
            return

    sg.popup_error("Registo não encontrado.", title="Erro")

# Aceder 
def aceder(lista):
    layout_autor = [
        [sg.Text("Digite o nome do autor para consultar os registos:")],
        [sg.InputText(key="-AUTHOR-")],
        [sg.Button("Procurar"), sg.Button("Cancelar")]
    ]
    window_autor = sg.Window("Consultar Registos por Autor", layout_autor, font=('Calibri Light', 15))

    stop = False
    while not stop:
        event, values = window_autor.read()

        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            stop=True

        elif event == "Procurar":
            nome_autor = values["-AUTHOR-"]
            if not nome_autor:
                sg.popup_error("Por favor, insira um nome de autor válido.", title="Erro")
            else:
                lista_tit = []
                lista_url = []
                lista_doi = []
                for registo in lista:
                    if "authors" in registo:
                        for autor in registo["authors"]:
                            if autor.get("name") == nome_autor:
                                if 'title' in registo:
                                    lista_tit.append(registo["title"])
                                elif 'url' in registo:
                                    lista_url.append(registo["url"])
                                elif 'doi' in registo:
                                    lista_doi.append(registo["doi"])
                
                if not lista_tit and not lista_url and not lista_doi:
                    sg.popup_error("Nenhum registo encontrado para o autor fornecido.", title="Erro")
                else:
                    lista_final = lista_tit + lista_url + lista_doi
                    layout_registos = [
                        [sg.Text("Selecione um registo para aceder ao URL ou ao DOI:")],
                        [sg.Listbox(lista_final, size=(60, 20), key="-REGISTO-", enable_events=True)],
                        [sg.Button("Abrir URL/DOI"), sg.Button("Fechar")]
                    ]
                    window_registos = sg.Window("Registos Encontrados", layout_registos, font=('Calibri Light', 15))

                    stop2=False
                    while not stop2:
                        event_reg, values_reg = window_registos.read()

                        if event_reg == sg.WINDOW_CLOSED or event_reg == "Fechar":
                            window_registos.close()
                            stop2=True

                        elif event_reg == "Abrir URL/DOI":
                            if values_reg["-REGISTO-"]:
                                registo_selecionado = values_reg["-REGISTO-"][0]
                                url_doi = None

                                for registo in lista:
                                    if ("title" in registo and registo["title"] == registo_selecionado) or ("url" in registo and registo["url"] == registo_selecionado) or ("doi" in registo and registo["doi"] == registo_selecionado):

                                        if "url" in registo:
                                            url_doi = registo["url"]
                                            sg.popup(f"O URL do registo selecionado é:\n{url_doi}", title="URL", button_type=sg.POPUP_BUTTONS_OK)
                                        elif "doi" in registo:
                                            url_doi = registo["doi"]
                                            sg.popup(f"O DOI do registo selecionado é:\n{url_doi}", title="DOI", button_type=sg.POPUP_BUTTONS_OK)

                                if not url_doi:
                                    sg.popup_error("O registo selecionado não possui URL nem DOI.", title="Erro")
    window_autor.close()

# Janela secundária consultar
def formatar_registo(registo,numero):
    reg = [(f"- - - - - Registo nº {numero} - - - - -\n")]
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
    return "\n".join(reg) if reg != "" else None

def janela_opcao_consultar(opcoes, titulo, ata_medica):
    layout = [[sg.Button(opcao, size=(22, 2))] for opcao in opcoes] + [[sg.Push(),sg.Button('VOLTAR', key= '-VOLTAR-', size=(7, 2))]]
    window = sg.Window("Consultar Registo", layout)
    stop = False
    while not stop:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED or event == "-VOLTAR-":
                stop = True
            elif event == "Por Título":
                title = sg.popup_get_text("Introduza o titulo do registo que deseja consultar:",title="Consulta")
                if title:
                    novaAta = app.criaComTitulo(ata_medica)
                    lista = app.encontraTit_Data(novaAta,title)
                    if lista == []:
                        sg.popup_error("Pedimos desculpa, mas o título colocado não corresponde a nenhum registo da nossa base de dados ou pode possuir uma incorreção ortográfica.",title="Erro")
                    else:
                        cond = False
                        while cond == False:
                            resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                            "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                            if resposta and resposta.upper() == 'S':
                                cond = True
                                lista_registos = []
                                a = 1
                                for r in lista:
                                    lista_registos.append(formatar_registo(r,a))
                                    a = a + 1
                                texto_final = ("\n".join(lista_registos))
                                app.gravarConsultaTit("Registos com um determinado título.txt",texto_final)
                                sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com um determinado título.txt'.",title="Sucesso")
                            elif resposta and resposta.upper() == 'N':
                                cond = True
                                lista_registos = []
                                a = 1
                                for r in lista:
                                    lista_registos.append(formatar_registo(r,a))
                                    a = a + 1
                                texto_final = ("\n".join(lista_registos))
                                sg.popup_scrolled(texto_final,
                                title="Lista de Registos Consultados",
                                size=(80, 30))
                            elif not resposta:
                                sg.popup("Operação Cancelada!",title='Cancelar')
                                cond=True
                            else:
                                sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")     
                else:
                    sg.popup("Operação cancelada.",title="Cancelar")
            elif event == "Por Nome de um Autor":
                sg.popup("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem uma lista de autores.\n"
                "Se não o encontrar, por favor, tente com outro parâmetro.",title="Alerta")
                nomeAut = sg.popup_get_text("Introduza o nome do autor do registo que deseja consultar:",title="Nome Autor")
                if nomeAut:
                    condicao=True
                    i=0
                    while condicao and i<len(ata_medica):
                        for registo in ata_medica:
                            if 'authors' in registo: 
                                for autor in registo['authors']:
                                    if autor['name']==nomeAut:
                                        condicao=False
                            i=i+1
                    if condicao == True:
                        sg.popup_error("Pedimos desculpa, mas o autor colocado não possui nenhum registo na nossa base de dados ou pode possuir uma incorreção ortográfica.",title="Erro") 
                    else:
                        novaAta = app.criaComAutor(ata_medica)
                        selecao = sg.popup_get_text("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)?\n"
                        "Por favor, responda com 1 ou 2:",title="Escolha")
                        cond = False
                        while not cond:
                            if selecao == '1':
                                cond = True
                                lista = app.encontraAut_Tit(novaAta,nomeAut)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaNome_Tit("Registos de um autor (ordenados por título).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de um autor (ordenados por título).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif selecao == '2':
                                cond = True
                                lista = app.encontraAut_Data(novaAta,nomeAut)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaNome_Data("Registos de um autor (ordenados por data).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de um autor (ordenados por data).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif not selecao:
                                sg.popup("Operação Cancelada!",title='Cancelar')
                                cond=True
                            else:
                                sg.popup_error("Resposta inválida, por favor, introduza '1' ou '2'.",title="Erro")
                else:
                    sg.popup("Operação cancelada.",title="Cancelar")
            elif event == "Por Afiliação de um Autor":
                sg.popup("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem uma lista de autores.\n"
                "Se não o encontrar, por favor, tente com outro parâmetro.",title='Alerta')
                afiliacao = sg.popup_get_text("Introduza a afiliação do autor do registo que deseja consultar:",title="Afiliação")
                if afiliacao:
                    condicao=True
                    i=0
                    while condicao and i<len(ata_medica):
                        for registo in ata_medica:
                            if 'authors' in registo: 
                                for autor in registo['authors']:
                                    if autor.get('affiliation') == afiliacao:
                                        condicao=False
                            i=i+1
                    if condicao == True:
                        sg.popup_error("Pedimos desculpa, mas o autor colocado não possui nenhum registo na nossa base de dados ou pode possuir uma incorreção ortográfica.",title="Erro") 
                    else:
                        novaAta = app.criaComAutor(ata_medica)
                        selecao = sg.popup_get_text("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)?\n"
                        "Por favor, responda com 1 ou 2:",title="Escolha")
                        cond = False
                        while not cond:
                            if selecao == '1':
                                cond = True
                                lista = app.encontraAfilAut_Tit(novaAta,afiliacao)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':", title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaAfil_Tit("Registos de uma afiliação (ordenados por título).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma afiliação (ordenados por título).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif selecao == '2':
                                cond = True
                                lista = app.encontraAfilAut_Data(novaAta,afiliacao)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaAfil_Data("Registos de uma afiliação (ordenados por data).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma afiliação (ordenados por data).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif not selecao:
                                sg.popup("Operação Cancelada!",title='Cancelar')
                                cond=True
                            else:
                                sg.popup_error("Resposta inválida, por favor, introduza '1' ou '2'.",title="Erro")
                else:
                    sg.popup("Operação cancelada.",title="Cancelar")
            elif event == 'Por Data de Publicação':
                sg.popup("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem data de publicação.\n"
                "Se não o encontrar, por favor, tente com outro parâmetro.",title="Alerta")
                data = sg.popup_get_text("Introduza a data de publicação do registo que deseja consultar sob a forma de ano-mês-dia:",title="Data de Publicação")
                if data:
                    novaAta = app.criaComData(ata_medica)
                    lista = app.encontraDataPub_Tit(novaAta,data)
                    if lista == []:
                        sg.popup_error("Pedimos desculpa, mas a data colocada não corresponde a nenhum registo da nossa base de dados ou pode possuir uma incorreção ortográfica.",title="Erro")
                    else:
                        cond = False
                        while cond == False:
                            resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                            "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                            if resposta and resposta.upper() == 'S':
                                cond = True
                                lista_registos = []
                                a = 1
                                for r in lista:
                                    lista_registos.append(formatar_registo(r,a))
                                    a = a + 1
                                texto_final = ("\n".join(lista_registos))
                                app.gravarConsultaData("Registos de uma determinada data.txt",texto_final)
                                sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos de uma determinada data.txt'.",title="Sucesso")
                            elif resposta and resposta.upper() == 'N':
                                cond = True
                                lista_registos = []
                                a = 1
                                for r in lista:
                                    lista_registos.append(formatar_registo(r,a))
                                    a = a + 1
                                texto_final = ("\n".join(lista_registos))
                                sg.popup_scrolled(texto_final,
                                title="Lista de Registos Consultados",
                                size=(80, 30))
                            elif not resposta:
                                sg.popup("Operação Cancelada!",title='Cancelar')
                                cond=True
                            else:
                                sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                else:
                    sg.popup("Operação cancelada.",title="Cancelar")
            elif event == 'Por Palavra Chave':
                sg.popup("Ao selecionar esta opção, pode não ter acesso a alguns registos uma vez que nem todos possuem palavras chave ou podem estar incompletas.\n"
                "Se não o encontrar, por favor, tente com outro parâmetro.",title="Alerta")
                pal_chave = sg.popup_get_text("Introduza a palavra-chave do registo que deseja consultar:",title="Palavra-Chave")
                if pal_chave:
                    condicao=True
                    i=0
                    while condicao and i<len(ata_medica):
                        for registo in ata_medica:
                            if 'keywords' in registo and pal_chave in registo['keywords']:
                                condicao=False
                            i=i+1
                    if condicao == True:
                        sg.popup_error("Pedimos desculpa, mas nenhum registo da nossa base de dados possui essa palavra chave ou pode possuir uma incorreção ortográfica.",title="Erro") 
                    else:
                        novaAta = app.criaComPalChave(ata_medica)
                        selecao = sg.popup_get_text("Prefere os registos ordenados pelo título (1) ou pela data de publicação (2)?\n"
                        "Por favor, responda com 1 ou 2:",title="Escolha")
                        cond = False
                        while not cond:
                            if selecao == '1':
                                cond = True
                                lista = app.encontraPalChave_Tit(novaAta,pal_chave)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaPalChave_Tit("Registos com uma determinada palavra-chave (ordenados por título).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com uma determinada palavra-chave (ordenados por título).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif selecao == '2':
                                cond = True
                                lista = app.encontraPalChave_Data(novaAta,pal_chave)
                                cond2 = False
                                while not cond2:
                                    resposta = sg.popup_get_text("Deseja guardar a informação consultada num ficheiro?\n"
                                    "Por favor, responda com: 'S' ou 'N':",title="Escolha")
                                    if resposta and resposta.upper() == 'S':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        app.gravarConsultaPalChave_Data("Registos com uma determinada palavra-chave (ordenados por data).txt",texto_final)
                                        sg.popup("A informação que consultou foi guardada num ficheiro sob o nome de:'Registos com uma determinada palavra-chave (ordenados por data).txt'.",title="Sucesso")
                                    elif resposta and resposta.upper() == 'N':
                                        cond2 = True
                                        lista_registos = []
                                        a = 1
                                        for r in lista:
                                            lista_registos.append(formatar_registo(r,a))
                                            a = a + 1
                                        texto_final = ("\n".join(lista_registos))
                                        sg.popup_scrolled(texto_final,
                                        title="Lista de Registos Consultados",
                                        size=(80, 30))
                                    elif not resposta:
                                        sg.popup("Operação Cancelada!",title='Cancelar')
                                        cond2=True
                                    else:
                                        sg.popup_error("Resposta inválida. Por favor, responda com as opções referidas.",title="Erro")
                            elif not selecao:
                                sg.popup("Operação Cancelada!",title='Cancelar')
                                cond=True
                            else:
                                sg.popup_error("Resposta inválida, por favor, introduza '1' ou '2'.",title="Erro")
                else:
                    sg.popup("Operação cancelada.",title="Cancelar")
    window.close()

# Janelas secundária listar
def janela_opcao_listar(opcoes, titulo, ata_medica):
    layout = [[sg.Button(opcao, size=(35, 2))] for opcao in opcoes] + [[sg.Push(),sg.Button('VOLTAR', key= '-VOLTAR-', size=(7, 2))]]
    window = sg.Window("Listar Autores por Ordem Alfabética", layout)
    stop = False
    while not stop:
            event, values = window.read()  # Captura o evento e os valores
            if event == sg.WINDOW_CLOSED or event == "-VOLTAR-":
                stop = True
            elif event == "Autores - Ordem Alfabética":
                lista_autores = app.listarAutoresOrdAlf(ata_medica)
                resposta = sg.popup_get_text("Deseja guardar a lista num ficheiro? Responda com 'S' ou 'N'.",title='Escolha')
                if resposta:
                    cond = False
                    while not cond:
                        if resposta and resposta.upper() == 'S':
                            cond = True
                            app.gravarListaOrdAlf("Lista de Autores por Ordem Alfabética.txt", lista_autores)
                            sg.popup(
                                "A sua lista foi guardada num ficheiro com o nome:\n"
                                "'Lista de Autores por Ordem Alfabética.txt'.",title='Sucesso')
                        elif resposta and resposta.upper() == 'N':
                            cond = True
                            sg.popup_scrolled(
                                "- - - - - Lista de Autores Por Ordem Alfabética - - - - -\n",
                                "\n".join(lista_autores),
                                title = "Lista de Autores",
                                size=(80, 30))
                        elif not resposta:
                            sg.popup("Operação Cancelada!",title='Cancelar')
                            cond=True
                        else:
                            sg.popup_error("Resposta inválida. Por favor, responda com 'S' ou 'N'.",title='Erro')
                else:
                    sg.popup("Operação cancelada.",title='Cancelar')
            elif event == "Autores - Frequência":
                lista_autores = app.listarAutoresFreq(ata_medica)
                resposta = sg.popup_get_text("Deseja guardar a lista num ficheiro? Responda com 'S' ou 'N'.",title='Escolha')
                if resposta:
                    cond = False
                    while not cond:
                        if resposta and resposta.upper() == 'S':
                            cond = True
                            app.gravarListaAutFreq("Lista de Autores por Frequência.txt", lista_autores)
                            sg.popup(
                                "A sua lista foi guardada num ficheiro com o nome:\n"
                                "'Lista de Autores por Frequência.txt'.",title='Sucesso')
                        elif resposta and resposta.upper() == 'N':
                            cond = True
                            lista_formatada = [
                            f"{autor[0]} | {autor[1]}" for autor in lista_autores]
                            sg.popup_scrolled(
                            "- - - - - Lista de Autores Por Frequência - - - - -\n",
                            "Nome | Nº de artigos\n\n",
                            "\n".join(lista_formatada),
                            title="Lista de Autores",
                            size=(80, 30)
                        )
                        elif not resposta:
                            sg.popup("Operação Cancelada!",title='Cancelar')
                            cond=True
                        else:
                            sg.popup_error("Resposta inválida. Por favor, responda com 'S' ou 'N'.",title='Erro')
                else:
                    sg.popup("Operação cancelada.",title='Cancelar')
            elif event == "Palavras Chave - Ordem Alfabética":
                a = app.analise_pal_chave_alf(ata_medica)
                resposta = sg.popup_get_text("Deseja guardar a lista num ficheiro? Responda com 'S' ou 'N'.",title='Escolha')
                if resposta:
                    cond = False
                    while not cond:
                        if resposta and resposta.upper() == 'S':
                            cond = True
                            app.gravarPalChaveOrdAlf("Lista de Palavras-Chave por Ordem Alfabética.txt",a)
                            sg.popup(
                                "A sua lista foi guardada num ficheiro com o nome:\n"
                                "'Lista de Palavras-Chave por Ordem Alfabética.txt'.",title='Sucesso')
                        elif resposta and resposta.upper() == 'N':
                            cond = True
                            lista_pc = [
                            f"{pc[0]} | {pc[1]}" for pc in a]
                            sg.popup_scrolled(
                            "- - - - - Lista de Palavras-Chave por Ordem Alfabética - - - - -\n",
                            "Palavras-Chave | Nº de Ocorrências\n\n",
                            "\n".join(lista_pc),
                            title="Lista de Palavras-Chave",
                            size=(80, 30)
                        )
                        elif not resposta:
                            sg.popup("Operação Cancelada!",title='Cancelar')
                            cond=True
                        else:
                            sg.popup_error("Resposta inválida. Por favor, introduza 'S' ou 'N'.",title='Erro')
                else:
                    sg.popup("Operação cancelada.",title='Cancelar')
            elif event == "Palavras Chave - Frequência":
                a = app.analise_pal_chave_ocorr(ata_medica)
                resposta = sg.popup_get_text("Deseja guardar a lista num ficheiro? Responda com 'S' ou 'N'.",title='Escolha')
                if resposta:
                    cond = False
                    while not cond:
                        if resposta and resposta.upper() == 'S':
                            cond = True
                            app.gravarPalChaveOcorr("Lista de Palavras-Chave Por Ocorrência.txt",a)
                            sg.popup(
                                "A sua lista foi guardada num ficheiro com o nome:\n"
                                "'Lista de Palavras-Chave Por Ocorrência.txt'.",title='Sucesso')
                        elif resposta and resposta.upper() == 'N':
                            cond = True
                            lista_pc = [
                            f"{pc[0]} | {pc[1]}" for pc in a]
                            sg.popup_scrolled(
                            "- - - - - Lista de Palavras-Chave Por Ocorrência - - - - -\n",
                            "Palavras-Chave | Nº de Ocorrências\n\n",
                            "\n".join(lista_pc),
                            title="Lista de Palavras-Chave",
                            size=(80, 30)
                        )
                        elif not resposta:
                            sg.popup("Operação Cancelada!",title='Cancelar')
                            cond=True
                        else:
                            sg.popup_error("Resposta inválida. Por favor, introduza 'S' ou 'N'.",title='Erro')
                else:
                    sg.popup("Operação cancelada.",title='Cancelar')
    window.close()

# Janela secundária Distrib
def janela_opcao_distrib(opcoes, titulo, ata_medica):
    layout = [[sg.Button(opcao, size=(35, 2))] for opcao in opcoes] + [[sg.Push(),sg.Button('VOLTAR', size=(10, 2))]]
    window = sg.Window("Distribuições", layout, resizable=True, finalize=True)
    stop = False
    while not stop:
            event,_ = window.read()
            if event == sg.WINDOW_CLOSED or event == "VOLTAR":
                stop = True
            elif event == "Top 20 Autores por Frequência":
                top_20 = app.autores_top_20(ata_medica)
                app.graf_autores_top20(top_20)
            elif event == "Publicações por Ano":
                sg.popup("Ao usar esta distribuição, pode não aparecer o nº total de artigos,uma vez que alguns registos não possuem data de publicação.",title='Alerta')
                anos = app.ano(ata_medica)
                app.publicacoes_ano(anos)
            elif event == "Publicações por Mês de um Determinado Ano":
                sg.popup("Ao usar esta distribuição, pode não aparecer o nº total de artigos,uma vez que alguns registos não possuem data de publicação.",title='Alerta')
                ano = sg.popup_get_text("Introduza o ano das publicações:",title='Ano de Publicação')
                if not ano:
                    sg.popup('Opção Cancelada!',title='Cancelar')
                else:
                    lista_ano = app.verificaMesAno(ata_medica,ano)
                    if lista_ano == None:
                        sg.popup_error("Pedimos desculpa, mas não existe nenhum artigo da base de dados com esse ano de publicação.",title='Erro')
                    else:
                        distrib_meses = app.mes(lista_ano)
                        app.publicacoes_mes(distrib_meses)
            elif event == "Publicações de um Autor por Anos":
                sg.popup("Ao usar esta distribuição, pode não aparecer o nº total de artigos escritos pelo autor selecionado, uma vez que alguns registos não possuem data de publicação.",title='Alerta')
                nome = sg.popup_get_text("Introduza o nome do autor:")
                lista_aut = app.verificaAutor(ata_medica,nome)
                if lista_aut == None:
                    sg.popup_error("Pedimos desculpa, mas esse autor não escreveu nenhum artigo da base de dados.",title='Erro')
                else:
                    lista_d=app.verificaPub_Date(lista_aut)
                    final=app.pub_autor_ano(lista_d)
                    app.graf_pub_autor_ano(final)
            elif event == "Palavras-chave mais Frequente por Ano":
                sg.popup("Ao usar esta distribuição, pode não aparecer o nº total de artigos,uma vez que alguns registos não possuem data de publicação.",title='Alerta')
                ano = sg.popup_get_text("Introduza o ano de publicação:",title='Ano de Publicação')
                lista_pc_ano = app.verifica_pc_ano(ata_medica,ano)
                if lista_pc_ano == None:
                    sg.popup_error("Pedimos desculpa, mas não existe nenhum artigo da base de dados com esse ano de publicação.",title='Erro')
                else:
                    top_20_pc = app.pal_chave_ano(lista_pc_ano)
                    app.graf_palchave_ano(top_20_pc)
            elif event == "Palavras-Chave pela Frequência (Top 20)":
                top_20_pc = app.freq_palchave(ata_medica)
                app.graf_palchave_top20(top_20_pc)
    window.close()

# Loop de eventos
stop = False
while not stop:

    event, values = window.read()

    # Condição para fechar a janela
    if event == sg.WINDOW_CLOSED:
        stop = True
    elif event == "-SAIR-":
        sg.popup("Obrigado pela sua preferência. Volte sempre!", auto_close=True, auto_close_duration=1,title="Saída")
        stop = True

    elif event == '-CARREGAR-':
        ata_medica = carregar()
    elif event == '-INSERIR-':
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                        "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            inserirReg(ata_medica)
    elif event == '-APAGAR-':
        if not ata_medica :
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                        "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            apagarRegisto(ata_medica)
    elif event == '-ATUALIZAR-':
        if not ata_medica :
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                        "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            atualiza(ata_medica)
    elif event == '-GUARDAR-':
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                        "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            guardarAta()
    elif event == "-ACEDE-URL-":
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                        "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            aceder(ata_medica)
    elif event == '-CONSULTAR-':
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                    "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            janela_opcao_consultar(['Por Título', 'Por Nome de um Autor','Por Afiliação de um Autor','Por Data de Publicação','Por Palavra Chave'], 'Consultar',ata_medica)
    elif event == '-LISTAR-':
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                    "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            janela_opcao_listar(['Autores - Ordem Alfabética', 'Autores - Frequência', 'Palavras Chave - Ordem Alfabética', 'Palavras Chave - Frequência'], 'Listar Autores',ata_medica)
    elif event == '-DISTRIB-':
        if not ata_medica:
            sg.popup("Ainda não usou a função carregar ficheiro.\n"
                    "Para que qualquer opção funcione tem que utilizar primeiro a opção 1.",title="Alerta")
        else:
            janela_opcao_distrib(['Top 20 Autores por Frequência', 'Publicações por Ano', 'Publicações por Mês de um Determinado Ano', 'Publicações de um Autor por Anos', 'Palavras-chave mais Frequente por Ano', 'Palavras-Chave pela Frequência (Top 20)'], 'Distribuições',ata_medica)
    
    print(f'Você clicou em {event}.')

# Fechar a janela principal
window.close()