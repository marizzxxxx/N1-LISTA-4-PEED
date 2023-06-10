class No:
    def __init__(self, dado):
        self.dado = dado
        self.ant = None
        self.prox = None

class ListaED:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def vazio(self):
        return self.primeiro is None

    def inserir(self, dado):
        novoNo = No(dado)

        if self.vazio():
            self.primeiro = novoNo
            self.ultimo = novoNo
        elif dado < self.primeiro.dado:
            novoNo.prox = self.primeiro
            self.primeiro.ant = novoNo
            self.primeiro = novoNo
        elif dado > self.ultimo.dado:
            novoNo.ant = self.ultimo
            self.ultimo.prox = novoNo
            self.ultimo = novoNo
        else:
            atual = self.primeiro
            while atual is not None and dado > atual.dado:
                atual = atual.prox

            novoNo.ant = atual.ant
            novoNo.prox = atual
            atual.ant.prox = novoNo
            atual.ant = novoNo

    def exibir(self):
        if self.vazio():
            print("A lista está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.prox
        print()

def lnomes():
    lista = ListaED()

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == "sair":
            break
        lista.inserir(nome)

    return lista

lnomes = lnomes()
print("Lista de nomes em ordem alfabética:")
lnomes.exibir()