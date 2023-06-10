class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]


fila = Queue()

print("Digite só números inteiros e finalize o prograna com um nuemro negativo:")

while True:
    numero = int(input())
    if numero < 0:
        break
    fila.enqueue(numero)

print("\nElementos da fila na ordem de inserçãoo:")

while not fila.is_empty():
    elemento = fila.dequeue()
    print(elemento)