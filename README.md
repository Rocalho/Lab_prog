# Sistema de biblioteca
Este código é um sistema simples para o gerenciamento de biblioteca com funcionalidades basicas para gerir livros, membros e empréstimos.
## **Classes**
### Livro
Representa um Livro com características como título, autor, ano de publicação, genero e ISBN. Além disso possui uma funcionalidade que mostra as informações do livro.
### Estoque
Gerencia os livros com funcionalidades como adicionar livro, remover livro, buscar livro e mostrar os livros que estão no estoque.
### Membro
Representa um membro da biblioteca com características como nome, ID do membro, data de nascimento e endereço. Além disso possui uma funcionalidade que mostra as informações do membro.
### Cadastro
Gerencia os membros com funcionalidades como adicionar membro, remover membro, buscar membro e mostrar os membros que estão cadastrados.
### Empréstimo
Gerencia os empréstimos de livros aos membros com funcionalidades como, emprestar livro, devolver livro, ver quantos livros estão em posse de um membro (um maxímo de 3 livros por membro) e ver qual membro está com determinado livro.
## **Modo de Uso**
Para o uso do sistema, crie variáveis para Livro, Estoque, Membro, Cadastro e Empréstimo e utilize as funcionalidades para gerenciar a biblioteca.
## **Justificativa**
### Paradigma
O paradigma orientado a objetos foi escolhido pela facilidade em organizar e compreender o código.
### Linguagem de programação
Python foi escolhido por sua simplicidade e legibilidade.
### Arquitetura geral do sistema
A arquitetura geral do sistema é dividida em classes com módulos para gerenciar livros e membros e um menu interativo para facilitar a interação do usuário. 
