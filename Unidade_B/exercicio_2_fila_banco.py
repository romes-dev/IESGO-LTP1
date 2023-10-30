"""
Questão: Gerenciamento de Fila de Banco com Prioridade

Você foi designado para criar um programa em Python que simula a gestão de uma fila de banco do tipo FIFO (First-In, First-Out) com a capacidade de lidar com clientes prioritários de acordo com a lei. Sua tarefa é criar um programa que permita adicionar clientes à fila, atender o próximo cliente e visualizar a fila.

A fila funciona da seguinte maneira:

Quando um cliente chega ao banco, ele pode ou não ter prioridade por lei. Os clientes com prioridade por lei devem ser atendidos imediatamente e, portanto, pulam para a frente da fila.
Os clientes que não têm prioridade por lei são adicionados ao final da fila.
O atendimento é realizado no estilo FIFO, ou seja, o próximo cliente na fila é atendido.
Os clientes podem escolher sair do banco a qualquer momento.
Aqui está um resumo das funcionalidades que o programa deve ter:

Adicionar cliente à fila:

Solicita ao usuário o nome do cliente.
Pergunta se o cliente tem prioridade por lei (S para Sim, N para Não).
Se o cliente tiver prioridade, ele é adicionado à frente da fila. Caso contrário, é adicionado ao final da fila.
Atender próximo cliente:

Remove o próximo cliente da fila e informa que ele está sendo atendido.
Visualizar fila:

Exibe a fila atual, mostrando os nomes dos clientes na ordem em que estão na fila.
Sair do programa:

Encerra o programa.
Lembre-se de que você precisa criar uma classe Cliente para representar as pessoas na fila. A lista fila deve conter objetos dessa classe para acompanhar os clientes e suas prioridades.

Ao criar o programa, certifique-se de tratar erros e situações em que a fila está vazia.

Siga as diretrizes acima para criar um programa Python que simule a gestão de uma fila de banco com clientes prioritários. Certifique-se de que o programa funcione corretamente e permita que os usuários interajam com a fila, adicionando clientes, atendendo-os e visualizando a fila.
"""