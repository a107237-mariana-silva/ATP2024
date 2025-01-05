# Relatório de entrega do projeto 2024/25
## Data: 2024-01-05
## Autores: Ana Rita Costa (a107230) e Mariana Gonçalves Silva (a107237)
<br>

O presente ficheiro é constituído por três partes:
* Como usar o Sistema – resume simples que serve de manual de utilização;
* Criação – explica detalhadamente a criação das funções usadas;
* Exemplo de Execução – constituído por um exemplo que visa facilitar a utilização do programa de modo a oferecer ao utilizador uma ajuda visual.
<br>
<br>
# Como Usar o Sistema

Este sistema tem como objetivo gerir registos de publicações científicas, permitindo inserção, edição, exclusão e consulta de dados de maneira simples e eficiente. É composto por uma interface de linha de comando e uma interface gráfica. Aqui está um guia para a sua utilização:

## Requisitos
* Python
* Matplotlib
* FreeSimpleGUI ou PySimpleGUI
* Arquivo JSON com os registos (para carregamento inicial)

## Opções Disponíveis
1.	*Carregar Ata Médica*: Carrega os dados de um ficheiro JSON para manipulação. Deve ser disponibilizado o nome do ficheiro a ser carregado.
2.	*Inserir Registo*: Adiciona um novo registo à base de dados. São solicitadas informações como abstract, palavras-chave, autores, DOI, data de publicação, título, PDF e URL.
3.	*Apagar Registo pelo DOI*: Remove um registo existente baseado no seu DOI, após confirmação do usuário.
4.	*Atualizar um Registo*: Permite atualizar campos específicos de um registo, utilizando o DOI ou título para que seja identificado.
5.	*Guardar Ata Médica*: Salva os dados manipulados num arquivo JSON.
6.	*Aceder ao URL de um Registo*: Lista os registos associados a um autor, retornando o URL, ou DOI caso o URL não esteja disponível.
7.	*Consultar Registos*: Permite consultas filtradas por título, nome do autor, afiliação, data de publicação ou palavras-chave. Também é possível ordenar os resultados por data de publicação ou título.
8.	*Listar*: Gera listas ordenadas de autores ou palavras-chave por ordem alfabética ou frequência.
9.	*Distribuições*: Cria visualizações como gráficos de distribuição de autores, publicações e palavras-chave.
10.	*Sair*: Fecha o sistema.

## Interface Gráfica

### Navegação Inicial
1.	Carregar Ata Médica: Selecione o botão correspondente e insira o nome do arquivo JSON.
2.	Inserir Registo: Siga as etapas do formulário para adicionar um novo registo.
3.	Apagar Registo: Insira o DOI do registo a ser removido e confirme a operação.

### Consultas
Na interface gráfica pode selecionar diferentes parâmetros de consulta e visualizar os resultados diretamente na janela ou salvar num ficheiro.

### Distribuições Gráficas
Aceda à opção "Distribuições" para visualizar gráficos, como:
* Frequência de autores (Top 20).
* Publicações por ano ou mês.
* Palavras-chave mais frequentes por ano.

## Observações
* As operações só podem ser realizadas após o carregamento de uma ata médica.
* Certifique-se de salvar os dados antes de sair do sistema para evitar a perda de informações.
<br>
<br>

# Criação
## Etapas

Começamos o nosso projeto pela criação das nossas funções base, como o carregar ou guardar uma ata médica, uma vez que sem elas era impossível começar a fazer as outras e verificar que estavam a funcionar corretamente. Todas as nossas funções estão numa pasta chamada *app.py* e o ciclo usado para o terminal está na pasta *appGraf.py*. Para além disso, todas as funções da *app.py* estão por ordem do menu da *appGraf.py*.

Construimos logo o nosso menu com essas duas opções, a opção sair (opção 0) e o nosso ciclo. Decidimos guardar o dataset fornecido numa lista vazia no ínicio, chamada *ata_medica*.

Decidimos também deixar a interface gráfica para último, uma vez que ainda não tinhamos tido as aulas teóricas sobre esse tema quando começamos o nosso projeto.


## Requisitos Mínimos

Para assegurar a nota mínima, começamos por fazer todas as funções que faziam parte dos requisitos mínimos.

As duas primeiras funções que eram **Ler a informação do dataset para uma estrutura de dados em memória** e **Guardar a estrutura de dados em memória num ficheiro** já estavam criadas, como foi referido.
Escolhemos trabalhar com um ficheiro json por ser aquele com o qual estamos mais habituados a trabalhar, fazendo então um *json.load(f)* na função *carregarFicheiro*. Para esta primeira função, tem de aparecer no final a mensagem: *O seu ficheiro foi carregado com sucesso.*, o entanto, se o nome do ficheiro selecionado não for encontrado aparece: *Pedimos desculpa, mas esse ficheiro não existe ou não se encontra nesta pasta.*, ou caso algum erro ocorreu durante o seu carregamento criamos a f string: *Pedimos desculpa, mas ocorreu um erro ao carregar o ficheiro {f}.* onde f é o erro em questão.
Para a segunda, é primeiro pedido ao utilizador para introduzir o nome do ficheiro e é seguida criado o mesmo usando um *json.dump(lista,f)*. No final criamos uma f string: *O ficheiro {nome} foi guardado na base de dados.*, onde nome é o nome do ficheiro criado que o utilizador introduziu.

A seguinte foi **Inserir um registo novo** e para isso criamos um dicionário inicialmente vazio uma vez que todos os artigos do dataset são dicionários. Escolhemos pedir ao utilizador para adicionar todas as informações na função e se ele não introduzisse nada em certas categorias, elas nem aparecem no dicionário, como está no dataset (só são adicionadas se a informação introduzida fosse diferente de '' - string vazia) graças a um *if abstract*, por exemplo. No entanto, para introduzir os autores tivemos de criar uma *lista_autores* vazia que se preenche com os vários autores onde cada um corresponde a um dicionário, como no dataset. Para além disso, decidimos fazer com que o utilizador somente pudesse introduzir um certo título ou DOI se este não existir no dataset pois têm ambos de ser únicos. Caso já se encontre um artigo com um desses valores, o utilizador tem de introduzir um diferente. No final, esse dicionário é então introduzido dentro do dataset, na nossa lista *ata_medica*. No final aprece a mensagem: *O registo foi guardado com sucesso. *.

A função **Apagar um registo** funciona partindo do princípio de que cada artigo possui um DOI único e, por isso, o artigo que o utilizador deseja procurar é feito selecionando-o pelo mesmo. Se o que tinha sido introduzido estivesse de facto no dataset, então aparece uma mensagem de alerta onde se pergunta ao utilizador se deseja mesmo apagar esse registo sendo esta uma operação irreversível. Se a resposta for positiva, então esse mesmo registo é eliminado da ata médica aparecendo: *O seu registo foi apagado com sucesso.*, caso contrário, a operação é cancelada.

Por sua vez, a função **Consultar um registo** foi inicialmente concebida procurando o registo em questão pelo título. Para não dar erro, uma vez que certos artigos não possuem título, tivemos de criar uma função auxiliar que filtrava a ata médica carregada deixando somente os registos que possuem a categoria "title". Estes são depois introduzidos na função de *consultaRegisto_Tit*. Para aparecer direitinho e organizado no terminal, o artigo é primeiro escrito numa lista e somente aparecem as categorias que estão de facto no mesmo. Isto evita encontrar por exemplo: "publish_date": (string vazia). No final de tudo a função retorna então uma string usando *"\n".join(registos)*. No entanto, se o registo não fosse encontrado, a lista estaria vazia retornando 'None' e, nesse caso, aparece uma mensagem a dizer que não foi encontrado nenhum registo com esse nome e que o utilizador pode escolher procurar usando outra categoria, uma vez que as funções iam ser criadas depois.
Esta função foi posteriormente melhorada e iremos explicar as modificações mais à frente.

A função **Listar autores** foi criada primeiro listando os autores por ordem alfabética e foi depois criada outra para os listar consoante a frequência de artigos escritos. Mais uma vez, essa função foi melhorada depois de introduzida a possibilidade de o utilizador escolher se deseja guardar a listagem num ficheiro ou se prefere vê-la no terminal.
É de referir que para ordenar os autores por ordem alfabética tivemos de usar uma função que remove os acentos, usando a *key=removeAcentos*, que ordena os nomes dos autores e retorna os mesmos com os acentos, caso contrário todos os nomes que continham acentos ficavam no final da lista, o que não é o desejável. É então feito um 'print' inicial *- - - - - Lista de Autores Por Ordem Alfabética - - - - -\n\n* e depois graças a um ciclo *for*, outros prints sucediam cada um para cada nome de autor.

Finalmente, o primeiro gráfico criado foi o que corresponde à **Distribuição de autores por frequência (Top 20)**. Para isso, foi necessário usar uma função auxiliar para ter uma distribuição com o top 20 dos autores onde cada nome é associado ao número de artigos escritos no dataset. Para termos o top 20 foi realizado um sorted com *reverse=True* e um *slicing* para termos os 20 primeiros. A função retorna um dicionário graças a *dict(top_20)* sendo o top_20 uma lista, uma vez que o *sorted* converte o dicionário usado inicialmente para uma lista. Assim, após a criação desta função, utilizamos o matplotlib para termos um gráfico de barras e escolhemos cores pastel. Demos um título ao gráfico, no qual aparece no eixo dos yy *Nº de Artigos* sendo que no eixo dos xx os nomes dos autores apresentam-se rodados de 45º para não haver sobreposição dos mesmos.
Todos os gráficos foram feitos usando o matplotlib, como foi feito nas aulas.
<br>
<br>
Todas estas funções foram adicionadas pouco a pouco ao ciclo e sempre testadas antes de avançar para termos a certeza que estavam a funcionar corretamente.
Quando todas as nossas funções estavam a funcionar como queríamos, começamos a fazer as outras.

É de realçar também que todas as funções foram inseridas no ciclo funcionando somente se a lista *ata_medica* não estivesse vazia usando um *len(ata_medica)* uma vez que para ela não estar vazia o utilizador tinha de usar primeiro a opção 1. Isto evitava o surgimento de erros estando todas as funções como que encerradas antes da introdução de um dataset no sistema.

## Funções Restantes

A função **Atualizar um Registo** foi dividida em duas em que damos a escolher ao utilizador a possibilidade de procurar o registo desejado pelo título ou pelo DOI. É então perguntado ao utilizador o que quer modificar no artigo, somente podendo modificar uma categoria de cada vez. Cada categoria corresponde a um número e o utilizador escolhe uma que é depois enviada à função correspondente sob a forma de uma sigla, reconhecida depois na mesma função. Finalmente o utilizador tem de introduzir a modificação que deseja, no entanto, tivemos de criar uma string vazia para o caso de ele querer inserir um autor pois as informações necessárias têm de ser introduzidas dentro da mesma, facilitando o uso das funções.
Deste modo, as funções *atualizaTit* e *atualizaDoi* recebem ambas uma lista correspondente ao dataset carregado, um título/DOI respetivamente, uma modificação, cuja sigla é depois associada a uma característica dentro das funções e uma variável *x* que corresponde à modificação introduzida. Se o utilizador quer introduzir um autor (*x=''*) é criado um novo dicionário no qual são introduzidas as várias características do mesmo e que é depois inserido na lista de autores do artigo funcionando exatamente com o mesmo raciocínio que a função *Inserir registo* uma vez que somente as categorias com um certo conteúdo aparecem. No final, aparece a mensagem: *O registo foi modificado com sucesso.*.
Como é obvio, em cada uma destas funções houve antes de tudo uma busca pelo dataset e aparece uma mensagem no terminal dizendo que o registo não foi encontrado caso o título/DOI não corresponda a nenhum dos que se encontram no dataset carregado e para procurar o registo usando a opção alternativa.

A função **Listar Autores** foi, como referido anteriormente, melhorada. Como a lista de autores é bastante grande, o utilizador pode não a querer ver no terminal e por isso ao usar esta função, tem de escolher se prefere que a lista seja guardada num ficheiro ou não. Se sim, é aberta uma nova função *gravarListaOrdAlf* que cria um ficheiro *Lista de Autores por Ordem Alfabética.txt* (graças ao modo write - *w*) e que coloca todos os nomes dos autores por ordem alfabética. 
A função listar os autores pela frequência foi fácil de criar uma vez que já tínhamos a anterior. Criamos uma distribuição na qual cada autor tem como correspondência o seu número de artigos e é depois usado um *sorted* com *key=OrdenaAutores* que retorna a lista ordenada pela frequéncia (*[1]*).
As outras duas funções **Listar Palavras Chave** quer por ordem alfabética, quer por frequência são muito semelhantes, e aqui o utilizador também pode escolher guardar a informação desejada num ficheiro ou vê-la no terminal.

As duas funções **Listar Autores** são semelhantes à função **Aceder aos Registos de um Determinado Autor** que tinha de devolver um URL. É pedido ao utilizador para introduzir o nome do autor para o qual quer ver uma lista de todos os artigos escritos pelo mesmo. No entanto, certos artigos não possuem título e, por isso, em vez de aparecer o nome do artigo aparece diretamente o URL ou, se este também não existir, aparece o DOI do mesmo. Esta função é a *acederRegistoAutor* e dentro da mesma foram criadas 3 listas *lista_de_Registos_Tit*, *lista_de_Registos_Url* e *lista_de_Registos_Doi* que somente retorna a junção destas listas se todas elas fossem não vazias, caso contrário isso iria significar que o autor introduzido não escreveu nenhum artigo do dataset, aparecendo a mensagem: *Pedimos desculpa, mas esse autor não existe na nossa base de dados.*.
Após aparecer os títulos do registo ou dos URL's / DOI's, é pedido ao utilizador para dizer se quer inserir o título de um certo registo e se a resposta é positiva, então aparece o URL correspondente ou, mais uma vez, o DOI, caso a categoria URL não exista no registo.

As funções de **Ánalise de Palvras-Chave** são, em si, muito semelhantes ao conceito das duas funções listar anteriores e, por isso, foram também chamadas **Listar por Ordem Alfabética / por Frequência**. Aqui, é perguntado, mais uma vez, ao utilizador se deseja guardar a informação num ficheiro ou vê-la no terminal.
Tivemos de usar novamente a função *removeAcentos* pois todas as palavras-chaves com acentos estavam a aparecer no final quando era selecionada a opção *Ordem Alfabética*.
Por outro lado, para ordenar pela frequência foi usado: *key=lambda x: x[1]*.

Para fazer todas opções de **Consultar** decidimos que o utilizador pode escolher se quer que os registos apareçam ordenados pelo título (ordem alfabética) ou pela data (crescentemente). Também pode posteriormente escolher se os quer num ficheiro ou se prefere vê-los no terminal. Para aparecer no terminal usamos um *"\n".join(registos)*.
Para cada uma das funções consultar tivemos de criar funções auxiliares. Por exemplo, para consultar os registos de um certo autor foi criada a função *criaComAutor* que filtra todos os registos que possuem pelo menos um autor. Esses registos são depois enviados, continuando com o mesmo exemplo, para as funções desejadas *encontraAut_Tit* ou *encontraAut_Data* dependendo se o utilizador quer ordenar pelo título ou data de publicação, respetivamente. Nestas, usa-se um *key=ordenaTit* / *key=ordena_Data* onde os registos que não possuem título / data eram colocados no final. Retomado o exemplo anterior, foram criadas também funções *gravarConsultaNome_Tit* e *gravarConsultaNome_Data* se o utilizador prefere ver os registos num ficheiro em vez de os ver no terminal.
Ora, somente fazia sentido usar as funções de ordenar se o consultar não fosse nem pelo título nem pela data de publicação. No primeiro caso, eram ordenados somente pela data da publicação, no segundo eram ordenados somente pelo título.
Para além disso, para consultar artigos por uma certa palavra-chave é necessário fazer a buscar com *in* e não *==*, como nas outras funções, porque existem muitas palavras-chaves nos artigos e somente uma corresponde à introduzida.

Finalmente, criamos as **Distribuições**:
* As **Publicações por Ano** foram feitas usando a função *ano* que parte de um dicionário vazio e faz a distribuição de artigos por ano usando um slicing *[:4]*. Para ordenar as datas de forma crescente usamos um *key=OrdenaData*.
* Para as **Publicações por Mês de um Determinado Ano** o utilizador tem de introduzir o ano que quer e todos os artigos são filtrados na função *verificaMesAno* e depois enviados para a função *mes* que cria uma distribuição onde cada mês é substituido pelo seu nome em vez de aparecer o número do mesmo. Caso não fosse encontrado nenhum artigo com o ano introduzido, aparece uma mensagem no terminal que informa o utilizador do mesmo.
* Para as **Publicações de um Autor por Anos** o utilizador tem de introduzir o nome do autor e todos os artigos desse autor são filtrados na função *verificaAutor* e depois enviados para a função *verificaPub_Date* que filtra os artigos recebidos retornando somente os que possuem data de publicação. Se não é encontrado nenhum registo com o nome do autor introduzido, aparece uma mensagem no terminal que informa o utilizador do mesmo. Finalmente, a função *pub_autor_ano* constrói a distribuição para depois ser usada no gráfico.
* Indo agora para as **Palavras-chave mais Frequente por Ano**, neste caso temos uma função *verifica_pc_ano* que filtra todos os artigos com o ano de publicação que o utilizador introduziu. Se não é encontrado nenhum registo com esse ano, aparece, mais uma vez, uma mensagem a informar desse facto. Posteriormente, os artigos são enviados para a função *pal_chave_ano* que cria uma distribuição do top 20 palavras-chave mais usadas nesse ano usando um *sorted* e *slicing* (*[:4]*).
* Finalmente, a distribuição das **Palavras-Chave pela Frequência (Top 20)** é feita usando a função *freq_palchave* e usando também um *sorted* e *slicing*.

## Interface Gráfica

A interface gráfica foi criada num ficheiro com o nome de *appGraf2.py* graças ao programa *FreeSimpleGUI*, como foi feito nas aulas. Escolhemos para a nossa interface gráfica o tema *LightBlue"* e usamos a *ata_medica* como uma lista inicialmente vazia.

O layout principal contem ao todo 10 botões, um deles sendo o botão **SAIR**. Os outros são: **Carregar Ata Médica**, **Inserir Registo**, **Apagar Registo por DOI**, **Atualizar**, **Guardar Ata Médica**, **Aceder ao URL/DOI**, **Consultar**. Este último, por sua vez, abre uma janela de outros botões com todas as opções de consultas que o utilizador pode fazer. O botão **Listar** também abre outros botões correspondentes e **Distribuições** que, tal como os dois últimos, abre outros botões, cada um correspondente à sua distribuição.
Para o window principal usamos um *element_justification = 'center'* que coloca o conteúdo da janela alinhados.
<br>
<br>
Todas as funções funcionam exatamente como explicado anteriormente, com as mesmas restrições e raciocínios, e cada uma delas encontra-se encerrada enquanto a lista ata_medica estiver vazia, aparecendo um popup de alerta com essa informação, informando o utilizador que tem de usar primeiro a opção **Carregar Ata Médica**.

É de realçar que na função de **Inserir Registo**, foram adicionadas certas normas que o utilizador tem de respeitar, como para inserir uma data válida de acordo com a norma ano-mês-dia, por exemplo.

Para além desta particularidade, para a função **Guardar Ata Médica**, o utilizador tem de introduzir um nome do tipo *.json* caso contrário, não é aceitado.

Ainda é de referir que para as funções **Consultar** e **Listar**, se o utilizador não quiser ver a informação desejada num ficheiro, aparece um *popup_scrolled* onde pode ver todos registos selecionados.

Finalmente, quando o utilizador carregar no botão **Sair**, aparece uma mensagem num popup temporário a dizer *Obrigado pela sua preferênca. Volte sempre!* graças à opção *auto_close_duration=1* que faz com que este tenha um tempo de vida de 1 segundo. Isto não acontece se carregar no *WINDOW_CLOSED* por escolha pessoal.
<br>
<br>
# Exemplo de Execução

Este exemplo demonstra como usar o sistema para realizar operações básicas utilizando a interface de linha de comando. Acompanhe as etapas abaixo:

### Passo 1: Carregar um ficheiro JSON
 * Ação: Escolher a opção *1 - Carregar Ata Médica* no menu. 
 * Entrada: Insira o nome do ficheiro, por exemplo, registos.json.
 * Saída esperada: 
    ```
    O seu ficheiro foi carregado com sucesso.
    ```
### Passo 2: Inserir um novo registo
 * Ação: Escolher a opção *2 - Inserir Registo*.
 * Entrada: Preencher os campos solicitados: 
    * Abstract: "Resumo do artigo exemplo."
    * Palavras-chave: "saúde, bem-estar"
    * Número de autores: 1
    * Nome do autor: "João Silva"
    * Afiliação do autor: "Universidade X"
    * ORCID: "0000-0001-2345-6789"
    * DOI: "10.1000/xyz123"
    * Link para o PDF: "http://exemplo.com/artigo.pdf"
    * Data: "2024-01-01"
    * Título: "Estudo sobre Bem-Estar"
    * URL: "http://exemplo.com"
 * Saída esperada: 
    ```
    O registo foi guardado com sucesso.
    ```
### Passo 3: Consultar registos por título
 * Ação: Escolher a opção *7 - Consultar Registo por Título*.
 * Entrada: Insira o título "Estudo sobre Bem-Estar".
 * Saída esperada: 
    ```
    - - - - - Registo nº 1 - - - - -
    Abstract: Resumo do artigo exemplo.
    Palavras-chave: saúde, bem-estar
    Autores:
        Nome: João Silva
        Afiliação: Universidade X
        Orcid: 0000-0001-2345-6789
    DOI: 10.1000/xyz123
    PDF: http://exemplo.com/artigo.pdf
    Data de Publicação: 2024-01-01
    Título: Estudo sobre Bem-Estar
    URL: http://exemplo.com
    ```
### Passo 4: Apagar um registo pelo DOI
 * Ação: Escolher a opção *3 - Apagar Registo pelo DOI*.
 * Entrada: Inserir o DOI "10.1000/xyz123".
 * Saída esperada: 
    ```
    Tem a certeza que deseja apagar esse registo? Não poderá voltar atrás. Responda com 'S' ou 'N':
    ```
    S 

    ```
    O seu registo foi apagado com sucesso.
    ```
### Passo 5: Salvar os dados
 * Ação: Escolher a opção *5 - Guardar Ata Médica*.
 * Entrada: Fornecer o nome do arquivo, por exemplo, novo_registro.json.
 * Saída esperada: 
    ```
    O ficheiro novo_registro.json foi guardado na base de dados.
    ```
### Passo 6: Sair do sistema
 * Ação: Escolher a opção *0 - Sair*.
 * Saída esperada: 
    ```
    Aplicação encerrada. Obrigado pela sua visita, volte sempre!
    ```