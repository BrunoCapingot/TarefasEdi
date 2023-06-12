import random
from Estruturas.fila.Queue import Queue
from Estruturas.pilha import Stack
class Numero6:
    def __init__(self):
        self.fila = Queue()
        self.pilha = Stack()

    def sorteiaNumeros(self):

        for x in range(0,1000):
            numero = random.randint(-1000,1000)
            self.fila.push(numero)
            print('Elemento Adicionado fila : ' + str(self.fila.peek()))
            if numero > 0:
                self.pilha.push(self.fila.pop())
            elif numero < 0 and numero is not None:
                print('\nRetirando elemento: ' + str(self.pilha.pop()) + '\n')
