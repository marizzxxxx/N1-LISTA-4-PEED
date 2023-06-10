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

def pa(frase):
    
    frase = frase.lower().replace(" ", "")
    tamanho = len(frase)
    for i in range(tamanho // 2):
        if frase[i] != frase[tamanho - 1 - i]:
            return False
    return True


frase = input("Digite a frase: ")

if pa(frase):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")