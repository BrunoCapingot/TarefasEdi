from Estruturas.fila.Queue import Queue
from Estruturas.pilha import Stack

class Numero7:
    def __init__(self):
        self.pilha = Stack()
        self.fila = None

    def inverteFila(self,fila):
        self.fila = fila
        print('Original: ' + str(self.fila))
        for x in range(0,len(self.fila)):
            dado = self.fila.pop()
            self.pilha.push(dado)
        print('Pilha: ' + str(self.pilha))
        while not self.pilha.isEmpty():
            dado = self.pilha.pop()
            self.fila.push(dado)
        print('Fila: ' + str(self.fila))

