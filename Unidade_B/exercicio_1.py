############## ATENÇÃO #################
"""LISTA DISPONÍVEL SOMENTE ATÉ 10/10"""
"""https://forms.gle/YHpnHFVoDz483jY48"""
#**************************************#
"""


Exercício 1.1: Sistema de Biblioteca

Contexto:
Você foi contratado para criar um simples sistema de gerenciamento para uma pequena biblioteca. Os requisitos iniciais são criar um programa que permita ao usuário gerenciar livros e membros da biblioteca.

Requisitos:

A biblioteca deve ser capaz de armazenar informações sobre os livros, como título, autor e status (emprestado ou disponível).
A biblioteca deve também ser capaz de armazenar informações sobre os membros, como nome e os livros que eles emprestaram.
Implemente funcionalidades para adicionar livros, emprestar livros a membros e retornar livros.

Instruções:

Crie uma classe chamada Livro que tenha os seguintes atributos: titulo, autor e status. Por padrão, todos os livros devem ter o status "disponível".

Crie uma classe chamada Membro que tenha os seguintes atributos: nome e livros_emprestados (uma lista).

Crie uma classe chamada Biblioteca que tenha os seguintes atributos: livros (um dicionário com o título do livro como chave e a instância do livro como valor) e membros (um dicionário com o nome do membro como chave e a instância do membro como valor).

Na classe Biblioteca, crie os seguintes métodos:

adicionar_livro(self, livro): Adiciona um livro ao dicionário de livros.
registrar_membro(self, membro): Adiciona um membro ao dicionário de membros.
emprestar_livro(self, titulo_livro, nome_membro): Empresta um livro para um membro se o livro estiver disponível.
retornar_livro(self, titulo_livro, nome_membro): Retorna um livro que estava emprestado.


Desafio:

Adicione funcionalidades para remover livros ou membros.
Implemente uma busca para encontrar um livro ou membro por nome.
Dicas:

Use dicionários para armazenar livros e membros na classe Biblioteca para fácil acesso.
Ao emprestar um livro, atualize o status do livro e a lista de livros emprestados do membro.
Ao retornar um livro, faça o processo inverso do empréstimo.



Exercício 1.2: Gerenciador de Pedidos de Restaurante

Contexto:
Você está ajudando um pequeno restaurante a digitalizar seus processos. Eles querem um programa simples que gerencie os pedidos de seus clientes. Cada pedido pode ter vários itens, e cada item tem um preço associado.

Objetivo:
Crie um programa que permite ao usuário adicionar pedidos, adicionar itens aos pedidos e calcular o total de um pedido.

Requisitos:

O programa deve ter um dicionário de itens_menu onde as chaves são nomes de itens e os valores são os preços. Por exemplo: {"hamburger": 5.50, "batata frita": 2.00, "refrigerante": 1.50}.
Os pedidos podem ser armazenados em um dicionário chamado pedidos, onde as chaves são números de pedido e os valores são outro dicionário contendo os itens pedidos e suas quantidades.
O programa deve permitir que o usuário:
Adicione um novo pedido.
Adicione itens a um pedido existente.
Calcule e exiba o total de um pedido.
Instruções:

Inicialize o dicionário itens_menu com pelo menos 5 itens e seus preços.
Permita que o usuário adicione novos pedidos. Um pedido deve ser outro dicionário com itens e quantidades. Por exemplo: {1: {"hamburger": 2, "refrigerante": 1}} representa um pedido com 2 hambúrgueres e 1 refrigerante.
Permita que o usuário adicione itens a um pedido existente, especificando o número do pedido, o item e a quantidade.
Implemente uma função chamada calcular_total_pedido que aceita um número de pedido e retorna o total desse pedido, multiplicando preços e quantidades e somando todos os itens.
Desafio:

Implemente uma funcionalidade que permite ao usuário remover itens de um pedido ou alterar a quantidade de um item em um pedido.
Permita que o usuário visualize todos os pedidos atuais e seus totais.
Dicas:

Lembre-se de verificar se um item adicionado pelo usuário realmente existe no menu.
Ao calcular o total, lembre-se de multiplicar o preço do item pela quantidade e, em seguida, somar os totais para todos os itens.



Exercício 1.3: Sistema de Gerenciamento de Zoológico

Contexto:
Você foi encarregado de desenvolver um sistema para gerenciar os animais de um zoológico. O zoológico tem vários tipos de animais, e eles precisam de uma forma organizada de acompanhar informações básicas sobre esses animais, como espécie, dieta, idade e habitat.

Requisitos:

Crie uma classe Animal que tenha os seguintes atributos:

nome (nome do animal)
especie (por exemplo, "Leão", "Pinguim", "Cobra")
idade
dieta (por exemplo, "Carnívoro", "Herbívoro", "Onívoro")
A classe Animal também deve ter um método descricao que retorna uma string formatada, descrevendo o animal (por exemplo, "Leo é um Leão de 5 anos que é Carnívoro").

Crie uma classe Zoologico que tenha os seguintes atributos:

animais (uma lista para armazenar instâncias da classe Animal)
A classe Zoologico deve ter os seguintes métodos:

adicionar_animal(self, animal): para adicionar um novo animal ao zoológico.
remover_animal(self, nome): para remover um animal do zoológico usando seu nome.
listar_animais(self): para listar todos os animais no zoológico e suas informações.
Desafio:

Adicione um atributo habitat à classe Animal (por exemplo, "Savana", "Tundra", "Floresta Tropical"). Modifique o método descricao para incluir essa informação.
Na classe Zoologico, adicione um método buscar_por_especie(self, especie) que retorna uma lista de animais dessa espécie específica.
Implemente a possibilidade de listar todos os animais em um habitat específico.
Dicas:

Ao adicionar ou remover animais da lista em Zoologico, lembre-se de usar os métodos da lista, como append ou remove.
Ao listar os animais, use um loop para iterar sobre todos os animais e chamar o método descricao de cada animal.


Exercício 1.4: Plataforma de Jogos de Azar Online

Contexto:
Você está desenvolvendo um software para gerenciar uma plataforma de jogos de azar online. Cada jogo tem um nome, uma categoria (por exemplo, "Pôquer", "Caça-Níqueis", "Roleta"), uma taxa de entrada e uma identificação única. Você gostaria de imprimir facilmente os detalhes dos jogos de uma maneira legível.

Objetivo:
Crie classes para representar um jogo e um catálogo de jogos. Use a função __str__() para personalizar a saída quando um jogo é impresso.

Requisitos:

Crie uma classe chamada Jogo com os seguintes atributos:

nome
categoria
taxa_entrada
id
Implemente o método __str__(self) para a classe Jogo. Quando você imprimir um objeto da classe Jogo, deve retornar uma string no formato: "Nome: [nome], Categoria: [categoria], Taxa de Entrada: [taxa_entrada], ID: [id]".

Crie uma classe chamada Plataforma com o seguinte atributo:

jogos: uma lista para armazenar objetos da classe Jogo.
Adicione os seguintes métodos à classe Plataforma:

adicionar_jogo(self, jogo): adiciona um jogo à lista.
remover_jogo(self, id): remove um jogo usando sua ID.
listar_jogos(self): imprime todos os jogos na plataforma usando um loop e aproveitando a função __str__() da classe Jogo.
Desafio:

Implemente o método __str__(self) para a classe Plataforma também. Ao imprimir um objeto da classe Plataforma, deve mostrar quantos jogos existem na plataforma.


Exercício 1.5: Sistema de Gerenciamento de Estudantes

Contexto:
Você está construindo um software para gerenciar estudantes em uma escola. Cada estudante tem um nome, idade, nota e um ID único. A escola deseja realizar várias operações com esses estudantes, como adicionar uma nota a um estudante, calcular a média da turma e encontrar o estudante com a maior nota.

Objetivo:
Crie uma classe para representar um estudante e uma classe para representar uma turma de estudantes. Use métodos dentro dessas classes para executar as operações necessárias.

Requisitos:

Crie uma classe chamada Estudante com os seguintes atributos:

nome
idade
nota
id
Crie uma classe chamada Turma com o seguinte atributo:

estudantes: uma lista para armazenar objetos da classe Estudante.
Adicione os seguintes métodos à classe Turma:

adicionar_estudante(self, estudante): adiciona um estudante à turma.
remover_estudante(self, id): remove um estudante usando sua ID.
media_da_turma(self): calcula e retorna a média das notas dos estudantes.
melhor_estudante(self): retorna o estudante com a maior nota.
Desafio:
Adicione os seguintes métodos à classe Estudante:

alterar_nota(self, nova_nota): modifica a nota do estudante.
informacoes(self): imprime informações básicas sobre o estudante.

"""