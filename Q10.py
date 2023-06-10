class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None


class ListaEncadeadaDupla:
    def __init__(self):
        self.cabeca = None
        self.calda = None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
            self.calda = novo_no
        else:
            novo_no.proximo = self.cabeca
            self.cabeca.anterior = novo_no
            self.cabeca = novo_no

    def inserir_final(self, valor):
        novo_no = No(valor)
        if self.calda is None:
            self.cabeca = novo_no
            self.calda = novo_no
        else:
            novo_no.anterior = self.calda
            self.calda.proximo = novo_no
            self.calda = novo_no

    def remover_inicio(self):
        if self.cabeca is None:
            return None

        no_removido = self.cabeca
        if self.cabeca == self.calda:
            self.cabeca = None
            self.calda = None
        else:
            self.cabeca = self.cabeca.proximo
            self.cabeca.anterior = None
        return no_removido.valor

    def remover_final(self):
        if self.calda is None:
            return None

        no_removido = self.calda
        if self.cabeca == self.calda:
            self.cabeca = None
            self.calda = None
        else:
            self.calda = self.calda.anterior
            self.calda.proximo = None
        return no_removido.valor

    def exibir_lista(self):
        if self.cabeca is None:
            print("A lista está vazia.")
            return

        no_atual = self.cabeca
        while no_atual is not None:
            print(no_atual.valor, end=" ")
            no_atual = no_atual.proximo
        print()

lista = ListaEncadeadaDupla()

lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)

lista.exibir_lista()

lista.inserir_final(40)
lista.inserir_final(50)

lista.exibir_lista()

valor_removido = lista.remover_inicio()
print("Valor removido do início:", valor_removido)

lista.exibir_lista()

valor_removido = lista.remover_final()
print("Valor removido do final:", valor_removido)

lista.exibir_lista()