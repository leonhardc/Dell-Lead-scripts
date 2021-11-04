livros = {} # lista de livros
livro = {} # dicionario

while True:
    # ENTRADA DE DADOS
    print('--- MENU ---')
    print('1. Cadastrar Livro')
    print('2. Listar livros')
    print('3. Sair')
    op = input('\nEscolha uma opção: ')

    # PROCESSAMENTO DE DADOS
    if op == '1':
        # Cadastrar livros
        print('\n--- Cadastrar Livro ---\n')
        titulo = input('Título do livro: ')
        genero = input('Gênero do livro: ')
        subgenero = input('Subgenero do livro: ')
        editora = input('Editora do livro: ')
        num_copias = input('Numero de cópias em estoque: ')
        valor = input('Valor do Livro (R$): ')

        livro['titulo'] = titulo
        livro['genero'] = genero
        livro['subgenero'] = subgenero
        livro['editora'] = editora
        livro['numero de copias'] = num_copias
        livro['valor'] = valor

        if genero in livros:
            # adiciona livro no genero especificado
            if subgenero in livros[genero]:
                #adiciona livro no subgenero especificado
                livros[genero][subgenero].append(livro)
                print()
            else:
                # cria novo subgenero
                livros[genero][subgenero] = []
                livros[genero][subgenero].append(livro)
                print()
        else:
            # cria um novo genero para o livro
            livros[genero] = {}
            livros[genero][subgenero] = []
            livros[genero][subgenero].append(livro)
            print()


    elif op == '2':
        print('\n --- Listar Livros --- \n')
        # listar livros
        for genero in livros:
            # acessa o genero do livro
            print('--- Genero: {} ---'.format(genero))
            for subgenero in livros[genero]:
                print('\t--- Subgenero: {} ---'.format(subgenero))
                # acessa o subgenero do livro
                cont = 1
                for livro in livros[genero][subgenero]:
                    #acessa a lista de livros
                    print('\t\tLivro {}: \n'.format(cont))
                    for chave, valor in livro.items():
                        print('\t\t\t{} : {}'.format(chave, valor))
                    cont += 1
        # fim do listar livros


    elif op == '3':
        # sair
        break

    else:
        print('Opção Inválida!')
        op = input()
