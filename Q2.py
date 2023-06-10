class Fila:
    def __init__(self):
        self.fila = []

    def enqueue(self, elemento):
        self.fila.append(elemento)

    def dequeue(self):
        if not self.is_empty():
            return self.fila.pop(0)
        else:
            raise IndexError("A fila está vazia.")

    def size(self):
        return len(self.fila)

    def is_empty(self):
        return len(self.fila) == 0

    def show(self):
        if not self.is_empty():
            print("Fila:", self.fila)
        else:
            print("A fila está vazia.")


fila = Fila()

while True:
    print("1. Adicionar número")
    print("2. Remover número")
    print("3. Tamanho")
    print("4. Mostrar")
    print("5. Sair")

    opcao = int(input("escolha uma das opçoes: "))

    if opcao == 1:
        numero = int(input("Digite o número: "))
        fila.enqueue(numero)
        print("Número adicionado.")

    elif opcao == 2:
        try:
            numero_removido = fila.dequeue()
            print("Número removido:", numero_removido)
        except IndexError as e:
            print(e)

    elif opcao == 3:
        tamanho = fila.size()
        print("O tamanho eh:", tamanho)

    elif opcao == 4:
        fila.show()

    elif opcao == 5:
        print("Tchau.")
        break

    else:
        print("Opção inválida. Tente novamente.")