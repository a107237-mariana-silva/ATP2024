# Funções do projeto 2024/25
## Data: 2024-01-05
## Autores: Ana Rita Costa (a107230) e Mariana Gonçalves Silva (a107237)

## Estrutura

**app.py** - ficheiro com todas as funções criadas para o bom funcionamento da aplicação

**appGraf.py** - ciclo que aparece no terminal com o menu onde o utilizador introduz as opções desejadas

Todas as funções colocadas na pasta *app.py* estão por ordem do menu da *appGraf.py*.

**appGraf2.py** - correspondente à *appGraf.py*, mas numa interface gráfica


## Interface de linha de comando

O menu aparece sempre que é realizada uma opção. Apenas as funções carregar e sair funcionam quando ainda não foi carregada numa base de dados. Para as outras funcionarem, o utilizador tem de usar a opção 1.

As várias opções são:

* **Carregar Ata Médica** - carregar um dataset para o sistema
    - *carregarFicheiro(ficheiro)* - ficheiro corresponde ao nome do ficheiro que o utilizador deseja carregar

* **Inserir Registo** - inserir um registo no dataset
    - *inserir(ata_medica)* - ata_medica corresponde ao dataset carregado

* **Apagar Registo pelo DOI** - apagar um registo do dataset procurando-o pelo DOI
    - *apagarRegisto(ata_medica,doi)* - doi corresponde ao DOI do registo que o utilizador deseja apagar

* **Atualizar um Registo** - atualizar um registo do dataset procurando-o pelo título ou pelo DOI
    - *app.atualizaTit(ata_medica,titulo,modificacao,x)* - ata_medica corresponde ao dataset carregado; titulo corresponde ao título do registo que o utilizador deseja modificar; modificação corresponde à categoria que o utilizador deseja modificar; x corresponde à modificação em si (que somente é perguntada se o utilizador não quiser fazer modificações na categoria "authors")
    - *app.atualizaDoi(ata_medica,doi,modificacao,x)* - doi corresponde ao DOI do registo que o utilizador deseja modificar.

* **Guardar Ata Médica** - guardar o dataset num ficheiro 
    - *guardarFicheiro(nome,ata_medica)* - nome corresponde ao nome do ficheiro que o utilizador deseja guardar.

* **Aceder ao URL de um Registo (a partir de uma lista de registos por Autor)** - permite aceder ao URL de registos de um determinado autor
    - *app.acederRegistoAutor(ata_medica,nomeAut)* - ata_medica corresponde ao dataset carregado; nomeAut corresponde ao nome de autor para o qual vão aparecer os registos escrtitos pelo mesmo<br>O título do registo aparece por defeito, mas se algum não possuir título aparece diretamente o URL ou DOI, caso este não pussua URL.
    - *app.acederURL(ata_medica,nomeReg)* - nomeReg corresponde ao nome do registo que o utilizador deseja consultar.

* **Consultar Registo por Título** - permite consultar um registo pelo título do mesmo
    - *app.criaComTitulo(ata_medica)* - ata_medica corresponde ao dataset carregado
    - *app.encontraTit_Data(novaAta,title)* - novaAta corresponde à lista retornada pela função anterior; title corresponde ao titulo do registo que o utilizador deseja consultar
    - *app.consultaRegisto_Tit(lista)* - lista corresponde à lista retornada pela função anterior
    - *app.gravarConsultaTit("Registos com um determinado título.txt",registo)* - registo corresponde ao registo retornado pela função anterior<br>Esta função somente é usada se o utilizador desejar guardar a informação num ficheiro.

* **Consultar Registo por Nome de um Autor** - permite consultar um registo pelo nome de um autor que o escreveu
    - *app.criaComAutor(ata_medica)*
    - *app.encontraAut_Tit(novaAta,nomeAut)*
    - *app.consultaRegisto_NomeAut(lista)*
    - *app.gravarConsultaNome_Tit*
    - *app.encontraAut_Data(novaAta,nomeAut)*
    - *app.gravarConsultaNome_Data*
    - Tem um modo de funcionamento semelhante à *Consultar Registo por Título*.

* **Consultar Registo por Afiliação de um Autor** - permite consultar um registo pela afiliação de um autor que o escreveu
    - *app.criaComAutor(ata_medica)*
    - *app.encontraAfilAut_Tit(novaAta,afiliacao)*
    - *app.consultaRegisto_AfilAut(lista)*
    - *app.gravarConsultaAfil_Tit*
    - *app.encontraAfilAut_Data*
    - *app.gravarConsultaAfil_Data*
    - Tem um modo de funcionamento semelhante à *Consultar Registo por Título*.

* **Consultar Registo por Data de Publicação** - permite consultar um registo pela data de publicação do mesmo
    - *app.criaComData(ata_medica)*
    - *app.encontraDataPub_Tit(novaAta,data)*
    - *app.consultaRegisto_Data(lista)*
    - *app.gravarConsultaData*
    - Tem um modo de funcionamento semelhante à *Consultar Registo por Título*.

* **Consultar Registo por Palavra-Chave** - permite consultar um registo por uma palavra-chave do mesmo
    - *app.criaComPalChave(ata_medica)*
    - *app.encontraPalChave_Tit(novaAta,pal_chave)*
    - *app.consultaRegisto_PalChave(lista)*
    - *app.gravarConsultaPalChave_Tit*
    - *app.encontraPalChave_Data(novaAta,pal_chave)*
    - *app.gravarConsultaPalChave_Data*
    - Tem um modo de funcionamento semelhante à *Consultar Registo por Título*.

* **Listar Autores por Ordem Alfabética** - permite listar os autores do dataset por ordem alafabética
    - *app.listarAutoresOrdAlf(ata_medica)* - ata_medica corresponde ao dataset carregado
    - *app.gravarListaOrdAlf("Lista de Autores por Ordem Alfabética.txt",a)* - a corresponde à lista retornada pela função anterior

* **Listar Autores por Frequência** - permite listar os autores do dataset por frequência
    - *app.listarAutoresFreq(ata_medica)*
    - *app.gravarListaAutFreq("Lista de Autores por Frequência.txt",a)*
    - Tem um modo de funcionamento semelhante à *Listar Autores por Ordem Alfabética*.

* **Listar Palavras-Chave por Ordem Alfabética** - permite listar as palavras-chave do dataset por frequência
    - *app.analise_pal_chave_alf(ata_medica)*
    - *app.gravarPalChaveOrdAlf("Lista de Palavras-Chave por Ordem Alfabética.txt",a)*
    - Tem um modo de funcionamento semelhante à *Listar Autores por Ordem Alfabética*.

* **Listar Palavras-Chave por Frequência** - permite listar as palavras-chave do dataset por frequência
    - *app.analise_pal_chave_ocorr(ata_medica)*
    - *app.gravarPalChaveOcorr("Lista de Palavras-Chave Por Ocorrência.txt",a)*
    - Tem um modo de funcionamento semelhante à *Listar Autores por Ordem Alfabética*.

* **Distribuição de Autores por Frequência (Top 20)** - permite criar um gráfico com o top 20 dos autores pela frequência
    - *app.autores_top_20(ata_medica)* - ata_medica corresponde ao dataset carregado
    - *app.graf_autores_top20(top_20)* - top_20 corresponde ao dicionário que é retornado da função anterior

* **Distribuição de Publicações por Ano** - permite criar um gráfico com o número de publicações por ano
    - *app.ano(ata_medica)*
    - *app.publicacoes_ano(anos)*
    - Tem um modo de funcionamento semelhante à *Distribuição de Autores por Frequência (Top 20)*.

* **Distribuição de Publicações por Mês de um Determinado Ano** - permite criar um gráfico com o número de publicações por mês de um determinado ano
    - *app.verificaMesAno(ata_medica,ano)* - ata_medica corresponde ao dataset carregado; ano corresponde ao ano de publicação das publicações
    - *app.mes(lista_ano)* - lista_ano corresponde à lista que é retornada da função anterior
    - *app.publicacoes_mes(distrib_meses)* - distrib_meses corresponde ao dicionário que é retornado da função anterior

* **Distribuição de Publicações de um Autor por Anos** - permite criar um gráfico com o número de publicações por ano de um certo autor
    - *app.verificaAutor(ata_medica,nome)*
    - *app.verificaPub_Date(lista_aut)*
    - *app.pub_autor_ano(lista_d)*
    - *app.graf_pub_autor_ano(final)*
    - Tem um modo de funcionamento semelhante à *Distribuição de Publicações por Mês de um Determinado Ano*.

* **Distribuição de Palavras-chave mais Frequente por Ano** - permite criar um gráfico com o número de publicações com uma determinada palavra-chave de um certo ano
    - *app.verifica_pc_ano(ata_medica,ano)*
    - *app.pal_chave_ano(lista_pc_ano)*
    - *app.graf_palchave_ano(top_20_pc)*
    - Tem um modo de funcionamento semelhante à *Distribuição de Publicações por Mês de um Determinado Ano*.

* **Distribuição de Palavras-Chave pela Frequência (Top 20)** - permite criar um gráfico com o top 20 das palavras-chave pela frequência
    - *app.freq_palchave(ata_medica)*
    - *app.graf_palchave_top20(top_20_pc)*
    - Tem um modo de funcionamento semelhante à *Distribuição de Autores por Frequência (Top 20)*.


Outras funções auxiliares:

* *ordena_Data(registo)* - recebe uma lista de registos ordenando-os pela data de publicação (*registo['publish_date']*)

* *ordenaTit(registo)* - recebe uma lista de registos ordenando-os pelo título (*registo['title']*)

* *OrdenaAutores(lista_autores)* - recebe uma lista de autores para os ordenadar pela frequência (*lista_autores[1]*)

* *removeAcentos(texto)* - recebe strings e ordena-as por ordem alfabética, removendo os acentos e depois colocando-os outra vez


## Interface gráfica

Somente foi criada uma função para além das já criadas. Todas as funções funcionam exatamente como explicado anteriormente, com as mesmas restrições e raciocinios.

* *formatar_registo(registo,numero)* - substituir uma das funções das opções consultar e listar para os registos aparecerem num popup_scrolled