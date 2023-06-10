class circular:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = [None] * capacidade
        self.inicio = 0
        self.fim = 0

    def enqueue(self, elemento):
        if self.is_full():
            raise IndexError("A fila está cheia.")

        self.fila[self.fim] = elemento
        self.fim = (self.fim + 1) % self.capacidade

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia.")

        elemento = self.fila[self.inicio]
        self.fila[self.inicio] = None
        self.inicio = (self.inicio + 1) % self.capacidade

        return elemento

    def is_empty(self):
        return self.inicio == self.fim and self.fila[self.inicio] is None

    def is_full(self):
        return self.inicio == self.fim and self.fila[self.inicio] is not None


fila = circular(5)

fila.enqueue(10)
fila.enqueue(20)
fila.enqueue(30)

print(fila.dequeue())
print(fila.dequeue())

fila.enqueue(40)
fila.enqueue(50)

print(fila.is_empty())
print(fila.is_full())

fila.enqueue(60)
print(fila.is_full())
