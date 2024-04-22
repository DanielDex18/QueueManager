# Gerenciador de Filas

## Descrição do Problema
O código implementa um gerenciador de filas para um sistema de atendimento ao cliente. Existem duas filas: preferencial e padrão. Os clientes podem ser adicionados a uma das filas e atendidos conforme sua ordem de chegada.

## Estrutura do Código
O código consiste em uma classe `GerenciadorFilas` que encapsula a lógica de gerenciamento das filas. Há três métodos principais:
- `__init__(self)`: Inicializa as listas vazias para as filas preferencial e padrão.
- `adicionar_cliente(self, preferencial)`: Adiciona um cliente à fila, sendo preferencial se `preferencial` for True e padrão caso contrário.
- `atender_cliente(self)`: Atende um cliente, removendo-o da fila preferencial se houver clientes nessa fila, caso contrário, remove-o da fila padrão.
- `mostrar_filas(self)`: Exibe o estado atual das filas na saída padrão.

O código principal está fora da classe e cria uma instância do `GerenciadorFilas`. Ele contém um loop infinito que solicita a entrada do usuário para realizar operações como adicionar cliente, atender cliente ou sair do programa. O código utiliza tratamento de exceções para lidar com entradas inválidas do usuário.

## Funcionamento
O programa solicita ao usuário que escolha uma opção a cada iteração do loop. As opções incluem adicionar clientes às filas, atender clientes ou sair do programa. Quando um cliente é adicionado, ele é inserido na fila preferencial ou padrão com base na escolha do usuário. Quando um cliente é atendido, o programa remove o primeiro cliente da fila preferencial, se houver, ou da fila padrão, se a fila preferencial estiver vazia. O estado atual das filas é exibido após cada operação.

## Pontos Fortes
- O código é claro e bem estruturado, facilitando a compreensão e manutenção.
- Utiliza orientação a objetos para encapsular a lógica de gerenciamento de filas.
- Implementa tratamento de exceções para lidar com entradas inválidas do usuário.

## Possíveis Melhorias
- Poderia-se adicionar mais funcionalidades, como a capacidade de remover clientes de uma fila específica ou visualizar estatísticas sobre as filas.
- Uma interface gráfica poderia ser adicionada para melhorar a experiência do usuário.
