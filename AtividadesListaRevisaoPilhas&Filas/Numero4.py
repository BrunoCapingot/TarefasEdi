from Estruturas.fila.Queue import Queue
import random

class Numero4:
    def __init__(self):
        self._fila_um = Queue()
        self.fila_dois = Queue()


        while len(self._fila_um) != 100:
            self._fila_um.push(random.random())
        print('Tamanho fila 1: ' + str(len(self._fila_um)))
        print('Fila 1: ' + str(self._fila_um))


    def invertaFila(self):
        string = ''
        while not self._fila_um.isEmpty():
            string = string + str(self._fila_um.pop())+'->'
        string = string.split('->')
        for x in range(len(string), 0, -1):
            self.fila_dois.push(string[x - 1])
        print('Tamanho fila 2: ' + str(len(self.fila_dois)))
        print('Fila 2: ' + str(self.fila_dois))