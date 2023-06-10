class iagenda:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.ant = None
        self.prox = None


class anums:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def vazio(self):
        return self.primeiro is None

    def ipessoa(self, nome, telefone):
        novaEntrada = iagenda(nome, telefone)

        if self.vazio():
            self.primeiro = novaEntrada
            self.ultimo = novaEntrada
        else:
            novaEntrada.ant = self.ultimo
            self.ultimo.prox = novaEntrada
            self.ultimo = novaEntrada

    def rpessoa(self, nome):
        if self.vazio():
            print("A agenda está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.nome == nome:
                if atual == self.primeiro:
                    self.primeiro = atual.prox
                    if self.primeiro is not None:
                        self.primeiro.ant = None
                elif atual == self.ultimo:
                    self.ultimo = atual.ant
                    if self.ultimo is not None:
                        self.ultimo.prox = None
                else:
                    atual.ant.prox = atual.prox
                    atual.prox.ant = atual.ant
                print("Pessoa removida com sucesso.")
                return
            atual = atual.prox

        print("Pessoa não encontrada na agenda.")

    def bpessoa(self, nome):
        if self.vazio():
            print("A agenda está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            if atual.nome == nome:
                print("Pessoa encontrada:")
                print("Nome:", atual.nome)
                print("Telefone:", atual.telefone)
                return
            atual = atual.prox

        print("Pessoa não encontrada na agenda.")

    def eagenda(self):
        if self.vazio():
            print("A agenda está vazia.")
            return

        atual = self.primeiro
        while atual is not None:
            print("Nome:", atual.nome)
            print("Telefone:", atual.telefone)
            atual = atual.prox
            if atual is not None:
                print()

agenda = anums()

agenda.ipessoa("João", "123456789")
agenda.ipessoa("Maria", "987654321")
agenda.ipessoa("Pedro", "567891234")

print("Agenda telefônica:")
agenda.eagenda()

agenda.bpessoa("Maria")

agenda.rpessoa("João")

print("\nAgenda telefônica após a remoção:")
agenda.eagenda()