import random

from Estruturas.fila.Queue import Queue

class Numero5:
    def __init__(self):
        self.fila1 = Queue()
        self.fila2 = Queue()
        self.pilhaImpilha = Queue()
        self.pilhaDesimpilha = Queue()

    def inserirMilNumbers(self):
        for x in range(0,1000):
            numero = random.randint(1,50)
            self.fila1.push(numero)
        #print('Fila f: ' + str(self.fila1))

    def comparaElementosComExistente(self, filaExistente):

        while not filaExistente.isEmpty():
            dadoVisitante = filaExistente.pop()
            while not self.fila1.isEmpty():
                dadoCasa = self.fila1.pop()
                if dadoVisitante == dadoCasa:
                    self.fila2.push(dadoCasa)
                self.pilhaImpilha.push(dadoCasa)
            while not self.pilhaImpilha.isEmpty():
                self.fila1.push(self.pilhaImpilha.pop())
        print('Elementos de pesquisa: ' + str(self.fila1))
        print('Elementos encontrados: ' + str(self.fila2))

    def pesquisaInFila(self,element):
        while not self.fila1.isEmpty():
            elemento = self.fila1.pop()
            if elemento == element:
                self.fila2.push(elemento)
            self.pilhaDesimpilha.push(elemento)

        while not self.pilhaDesimpilha.isEmpty():
            elemento = self.pilhaDesimpilha.pop()
            self.fila1.push(elemento)
        #print('Fila p: ' + str(self.fila2))
        return True


