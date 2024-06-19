from datetime import date, timedelta
from time import sleep


class Livros:
    def __init__(self, titulo, autor, ano, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.isbn = isbn
        self.emprestado = False

    def informacoes(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de publicação: {self.ano}')
        print(f'Gênero: {self.genero}')
        print(f'ISBN: {self.isbn}')
        if self.emprestado:
            print('Emprestado: Sim')
        else:
            print('Emprestado: Não')
        print('-='*20)


class Estoque:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro: {livro.titulo} foi adicionado.')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'Livro {livro.titulo}. Foi removido.')
                return
        print(f'ISBN digitado não é válido.')

    def buscar_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                return livro
        print('ISBN inválido, livro não foi encontrado.')

    def mostrar_estoque(self):
        if not self.livros:
            print('Não há livros cadastrados.')
        else:
            for livro in self.livros:
                livro.informacoes()
            print('-='*20)


class Membro:
    def __init__(self, nome, id_membro, data_nascimento, endereco):
        self.nome = nome
        self.id_membro = id_membro
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.livros_emprestados = []

    def informacao_membro(self):
        print(f'Nome: {self.nome}')
        print(f'ID do membro: {self.id_membro}')
        print(f'Data nascimento: {self.data_nascimento}')
        print(f'Endereço: {self.endereco}')
        if len(self.livros_emprestados) > 0:
            print(f'Livros emprestados: {[livro.titulo for livro in self.livros_emprestados]}')
        else:
            print('Nenhum livro emprestado')


class Cadastro:
    def __init__(self):
        self.membros = []

    def adicionar_membro(self, membro):
        self.membros.append(membro)
        print(f'Membro {membro.nome} Adicionado.')

    def remover_membro(self, id_membro):
        for membro in self.membros:
            if membro.id_membro == id_membro:
                self.membros.remove(membro)
                print(f'Membro {membro.nome} removido.')
                return
        print('ID inválido')

    def buscar_membro(self, id_membro):
        for membro in self.membros:
            if membro.id_membro == id_membro:
                return membro
        print('ID inválido')

    def listar_membros(self):
        if not self.membros:
            print('Nenhum membro cadastrado.')
        else:
            for membro in self.membros:
                membro.informacao_membro()
                print('-'*20)


class Emprestimo:
    def __init__(self, estoque_livro, cadastro_membro):
        self.estoque_livro = estoque_livro
        self.cadastro_membro = cadastro_membro
        self.emprestimos = []

    def emprestar_livro(self, id_membro, isbn):
        membro = self.cadastro_membro.buscar_membro(id_membro)
        if not membro:
            print(f"ID {id_membro} não encontrado.")
            return
        livro = self.estoque_livro.buscar_livro(isbn)
        if not livro:
            print(f'ISBN {isbn} não encontrado')
            return
        if livro.emprestado:
            print(f'O livro {livro.titulo} está emprestado a outro membro')
        elif len(membro.livros_emprestados) >= 3:
            print(f'Membro {membro.nome} já tem 3 livros emprestados')
        else:
            data_emprestimo = date.today()
            data_devolucao = data_emprestimo + timedelta(days=14)

            membro.livros_emprestados.append(livro)
            livro.emprestado = True
            self.emprestimos.append((membro, livro, data_emprestimo, data_devolucao))
            print(f'Livro {livro.titulo} emprestado ao membro {membro.nome}.')

    def devolver_livro(self, id_membro, isbn):
        membro = self.cadastro_membro.buscar_membro(id_membro)
        if not membro:
            print(f'ID {id_membro} não encontrado.')
            return
        livro = self.estoque_livro.buscar_livro(isbn)
        if not livro:
            print(f'ISBN {isbn} não encontrado.')
            return
        if livro not in membro.livros_emprestados:
            print(f'O membro {membro.nome} não pegou o livro {livro.titulo} emprestado.')

        membro.livros_emprestados.remove(livro)
        livro.emprestado = False

        self.emprestimos = [e for e in self.emprestimos if e[1].isbn or e[0].id_membro != id_membro]
        print(f'Livro {livro.titulo} devolvido pelo membro {membro.nome}.')

    def listar_emprestimos_membro(self, id_membro):
        membro = self.cadastro_membro.buscar_membro(id_membro)
        if not membro:
            print(f'ID {id_membro} não encontrado.')
            return

        print(f'Livros que estão com o membro {membro.nome}:')
        for livro in membro.livros_emprestados:
            print(f' -{livro.titulo} (ISBN {livro.isbn})')

    def listar_membros_por_livro(self, isbn):
        livro = self.estoque_livro.buscar_livro(isbn)
        if not livro:
            print(f'ISBN {isbn} não encontrado.')
            return

        print(f'Membro que está com o livro "{livro.titulo}":')
        for e in self.emprestimos:
            if e[1].isbn == isbn:
                print(f' -{e[0].nome} (ID: {e[0].id_membro})')


cadastro_livro = Estoque()
cadastro_membro = Cadastro()
emprestimo = Emprestimo(cadastro_livro, cadastro_membro)


while True:
    print()
    print('-='*20)
    print('SISTEMA DA BIBLIOTECA\n'
          '1- Adicionar livro\n'
          '2- Remover livro\n'
          '3- Listar livros\n'
          '4- Adicionar membro\n'
          '5- Remover membro\n'
          '6- Listar membros\n'
          '7- Emprestar livro\n'
          '8- Devolver livro\n'
          '9- Listar empréstimo por membro\n'
          '10- Listar membro em posse do livro\n'
          '0- SAIR')
    print('-='*20)
    print()
    opcao = int(input('Escolha uma opção: '))
    if opcao == 1:
        titulo1 = str(input('Titulo: '))
        autor1 = str(input('Autor: '))
        ano1 = str(input('Ano de publicação: '))
        genero1 = str(input('Gênero: '))
        isbn1 = str(input('ISBN: '))
        livro1 = Livros(titulo1, autor1, ano1, genero1, isbn1)
        cadastro_livro.adicionar_livro(livro1)

    elif opcao == 2:
        isbn1 = str(input('ISBN do livro a ser removido: '))
        cadastro_livro.remover_livro(isbn1)

    elif opcao == 3:
        cadastro_livro.mostrar_estoque()

    elif opcao == 4:
        nome1 = str(input('Nome: '))
        id_membro1 = str(input('ID do membro: '))
        data_nascimento1 = str(input('Data de nascimento: '))
        endereco1 = str(input('Endereço: '))
        membro1 = Membro(nome1, id_membro1, data_nascimento1, endereco1)
        cadastro_membro.adicionar_membro(membro1)

    elif opcao == 5:
        id_membro1 = str(input('ID do membro: '))
        cadastro_membro.remover_membro(id_membro1)

    elif opcao == 6:
        cadastro_membro.listar_membros()

    elif opcao == 7:
        id_membro1 = str(input('ID do membro: '))
        isbn1 = str(input('ISBN: '))
        emprestimo.emprestar_livro(id_membro1, isbn1)

    elif opcao == 8:
        id_membro1 = str(input('ID do membro: '))
        isbn1 = str(input('ISBN: '))
        emprestimo.devolver_livro(id_membro1, isbn1)

    elif opcao == 9:
        id_membro1 = str(input('ID do membro: '))
        emprestimo.listar_emprestimos_membro(id_membro1)

    elif opcao == 10:
        isbn1 = str(input('ISBN: '))
        emprestimo.listar_membros_por_livro(isbn1)

    elif opcao == 0:
        print('Saindo do sistema...')
        break

    else:
        print('Opção inválida, tente novamente.')

    sleep(2)
