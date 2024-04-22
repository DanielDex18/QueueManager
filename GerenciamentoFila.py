from time import sleep

class GerenciadorFilas:
    def __init__(self):
        self.caixa_pref = []
        self.caixa_padr = []

    def adicionar_cliente(self, preferencial):
        if preferencial:
            self.caixa_pref.append(len(self.caixa_pref) + 1)
        else:
            self.caixa_padr.append(len(self.caixa_padr) + 1)

    def atender_cliente(self):
        if self.caixa_pref:
            self.caixa_pref.pop(0)
        elif self.caixa_padr:
            self.caixa_padr.pop(0)
        else:
            print("Não há clientes para atender.")

    def mostrar_filas(self):
        print("Fila preferencial:", self.caixa_pref)
        print("Fila padrão:", self.caixa_padr)


gerenciador = GerenciadorFilas()

while True:
    print('====+====+=====+====+===+===+')
    print('\n1-Adicionar na fila preferencial\n2-Adicionar na fila padrão\n3-Atender a fila preferencial\n4-Atender a fila padrão\n0-Sair\n')
    resp = input()

    try:
        opcao = int(resp)
        if opcao == 1:
            gerenciador.adicionar_cliente(preferencial=True)
        elif opcao == 2:
            gerenciador.adicionar_cliente(preferencial=False)
        elif opcao == 3:
            gerenciador.atender_cliente()
        elif opcao == 4:
            gerenciador.atender_cliente()
        elif opcao == 0:
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número correspondente à opção desejada.")

    gerenciador.mostrar_filas()
