class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None


def listaenca(lista):
    cabeca = None
    for valor in lista[::-1]:
        no = No(valor)
        no.proximo = cabeca
        cabeca = no
    return cabeca


def listaencadeada(listainver):
    no = listainver
    while no is not None:
        print(no.valor, end=" ")
        no = no.proximo

nums = input("Digite uma lista de números inteiros separados por espaço: ").split()
nums = [int(num) for num in nums]

listainver = listaenca(nums)

listaencadeada(listainver)