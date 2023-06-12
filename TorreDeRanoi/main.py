from Estruturas.pilha import Stack


class Torre:
    def __init__(self, n):
        self._pino_primeiro = Stack()
        self._pino_segundo = Stack()
        self._pino_terceiro = Stack()
        self._total_discos = n
        self._pinos = {'A': self._pino_primeiro, 'B': self._pino_segundo, 'C': self._pino_terceiro}
    def operacao(self):
        self._pino_primeiro.push(0)
        if self._total_discos != 1:
            for x in range(0, self._total_discos - 1):
                pass
        else:
            self._pino_segundo.push(self._pino_primeiro.pop())

    def moveElemento(self, origem, destino):
        disco = self._pinos[origem].pop()
        self._pinos[destino].push(disco)
        #print("Movendo disco {} de {} para {}".format(disco, origem, destino))

    def process(self):
        for disco in range(self._total_discos, 0, -1):
            self._pinos['A'].push(disco)
        self.recursao(self._total_discos, 'A', 'B', 'C')


    def recursao(self, discos, origem, destino, auxiliar):

        if discos != 0:

            self.recursao(discos - 1, origem, auxiliar, destino)
            self.moveElemento(origem, destino)
            self.recursao(discos - 1, auxiliar, destino, origem)
        else:
            print('Não existem mais elementos')




if __name__ == '__main__':
    n = input("Ola, bem vindo a torre de Hanoi em python, aste de origem e a 1.\nInsira o numero de astes a seguir!\nAstes = ")
    Hanoi = Torre(int(n))
    Hanoi.process()
