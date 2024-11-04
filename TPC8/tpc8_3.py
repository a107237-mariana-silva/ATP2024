# Funções Auxiliares:

def existePost(redeSocial,id):
    cond = False
    for post in redeSocial:
        if post['id'] == id:
            cond = True
    return cond

def existeAutor(redeSocial,autor):
    cond = False
    for post in redeSocial:
        if post['autor'] == autor:
            cond = True
    return cond

def existeAutorCom(redeSocial, autor):
    cond = False
    for post in redeSocial:
        for comentarios in post['comentarios']:
            if comentarios['autor'] == autor:
                cond = True
    return cond

# Acrescenta um novo post à rede social:

def ids(redeSocial):
    if len(redeSocial) != 0:
        ultimo = redeSocial[-1]['id']
        num = int(ultimo[1:]) + 1
        id = "p" + str(num)
        return id
    else:
        id = "p1"
        return id

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    id = ids(redeSocial)
    post = {'id':id,'conteudo': conteudo,'autor': autor,'dataCriacao': dataCriacao,'comentarios': comentarios}
    redeSocial.append(post)
    return ("O post foi adicionado com sucesso.")

# Acresecntar um comentário a um post:

def insCom(redeSocial,id):
    if existePost(redeSocial,id):
        for post in redeSocial:
            if post['id'] == id:
                comentarios = post['comentarios']
                com = input("Introduza o seu comentário:")
                autor = input("Introduza o seu nome:")
                seccao = {'comentario':com,'autor':autor}
                comentarios.append(seccao)
        return ("O seu comentário foi adicionado com sucesso.")
    else:
        return ("Pedimos desculpa, mas esse poste não existe")

# Remove um post da rede:

def remPost(redeSocial, id):
    if existePost(redeSocial,id):
        for post in redeSocial:
            if post['id'] == id: 
                redeSocial.remove(post)
        return ("O posto foi removido com sucesso.")
    else:
        print("Pedimos desculpa, mas esse id não existe.")

# Indica quantos posts estão registados:

def quantosPost(redeSocial):
    res = 0
    for post in redeSocial:
        res = res + 1
    return (f"Número de posts: {res}.")

# Devolve a lista de posts de um determinado autor:

def postsAutor(redeSocial, autor):
    lista = []
    if existeAutor(redeSocial, autor):
        for post in redeSocial:
            if post['autor'] == autor:
                id = post['id']
                if id not in lista:
                    lista.append(id)
        return lista
    else:
        return ("Pedimos desculpa, mas esse autor não publicou nenhum post.")

# Devolve a lista de autores de posts ordenada alfabeticamente:

def autores(redeSocial):
    autores = []
    for post in redeSocial:
        aut = post['autor']
        if aut not in autores:
            autores.append(aut)
    return sorted(autores)

# Devolve uma distribuição de posts por autor:

def postsPorAutor(redeSocial):
    distrib = {}
    for post in redeSocial:
        if post['autor'] in distrib:
            distrib[post['autor']] = distrib[post['autor']] + 1
        else:
            distrib[post['autor']] = 1
    return distrib

# Recebe um autor e devolve a lista de posts comentados por esse autor:

def comentadoPor(redeSocial, autor):
    lista = []
    if existeAutorCom(redeSocial, autor):
        for post in redeSocial:
            for comentarios in post['comentarios']:
                if comentarios['autor'] == autor:
                    id = post['id']
                    if id not in lista:
                        lista.append(id)
        return lista
    else:
        return ("Pedimos desculpa, mas esse autor não comentou nenhum post.")

# Menu:

def menu():
    print(""" - - - - - MENU - - - - -
1 - Inserir um Post
2 - Acrescentar um Comentário a um Post
3 - Remover um Post
4 - Ver a minha Rede Social
5 - Número de Posts
6 - Lista de Posts de um Autor
7 - Autores
8 - Número de Posts por Autor
9 - Comentários por Autor
0 - Sair""")

# Sair:

def sair():
    return ("""A aplicação vai encerrar.
Agradecemos pela sua preferência. Volte sempre!""")


# Aplicação:

print("Bem vindo! Em que posso ajudar?")
cond = True
myRedeSocial = []
while cond:
    menu()
    opcao = str(input("Introduza a sua opção:"))
    if opcao == '1':
        conteudo = input("Introduza o conteudo do post:")
        autor = input("Introduza o seu nome:")
        data = input("Introduza a data de hoje (0000-00-00): ")
        comentarios = []
        print(insPost(myRedeSocial,conteudo,autor,data,comentarios))
    elif opcao == '2':
        if len(myRedeSocial) != 0:
            id = input("Inroduza o id do post que deseja comentar:")
            print(insCom(myRedeSocial,id))
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '3':
        if len(myRedeSocial) != 0:
            id = input("Inroduza o id do post que deseja remover:")
            print(remPost(myRedeSocial,id))
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '4':
        print(myRedeSocial)
    elif opcao == '5':
        if len(myRedeSocial) != 0:
            print(quantosPost(myRedeSocial))
        else:
            print("Não existe nenhum post.")
    elif opcao == '6':
        if len(myRedeSocial) != 0:
            autor = input("Introduza o nome do autor:")
            print(postsAutor(myRedeSocial,autor))
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '7':
        if len(myRedeSocial) != 0:
            print(autores(myRedeSocial)) 
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '8':
        if len(myRedeSocial) != 0:
            print(postsPorAutor(myRedeSocial))
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '9':
        if len(myRedeSocial) != 0:
            autor = input("Introduza o nome do autor do comentário:")
            print(comentadoPor(myRedeSocial,autor))
        else:
            print("Pedimos desculpa, mas a sua Rede Social está vazia.")
    elif opcao == '0':
        print(sair())
        cond = False
    else:
        print("Opcão incorreta. Por favor, introduza um número entre 0 e 9.")