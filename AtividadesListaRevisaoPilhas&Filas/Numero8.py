import random
from Estruturas.pilha import Stack
class Numero8:
    def __init__(self):
        self.pilha = TestaPilha()
        for x in range(0,1000):
            numero = random.randint(-100,100)
            if numero > 0:
                self.pilha.inserirEmP(numero)
            elif numero < 0:
                self.pilha.inserirEmN(numero)
            else:
                self.pilha.retirarUmEmAmbos()


class TestaPilha:
    def __init__(self):
        self.p = Stack()
        self.n = Stack()


    def inserirEmP(self,elemento):
        self.p.push(elemento)

    def inserirEmN(self,elemento):
        self.n.push(elemento)

    def retirarUmEmAmbos(self):
        n = self.n.pop()
        p = self.p.pop()
        print('Retirando n: ' + str(n))
        print('Retirando p: ' + str(p))