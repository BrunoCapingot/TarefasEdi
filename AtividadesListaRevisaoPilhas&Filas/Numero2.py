from Estruturas.pilha import Stack
class Numero2:
    def __init__(self):
        self._pilha_auxiliar = Stack()
        self._pilha_um = Stack()
        self._pilha_um.push(5)
        self._pilha_um.push(44)
        self._pilha_um.push(55)
        self._pilha_um.push(66)
        self._pilha_um.push(77)
        self._pilha_um.push(89)
        self._pilha_um.push(6651)
        self._pilha_um.push(651651)

    def removerItem(self,chave):
        print('Texto com o elemento {} : {}'.format(chave, self._pilha_um))
        while not self._pilha_um.isEmpty():
            c = self._pilha_um.pop()
            if c != chave:
                self._pilha_auxiliar.push(c)


        while not self._pilha_auxiliar.isEmpty():
            c = self._pilha_auxiliar.pop()
            self._pilha_um.push(c)
        print('Texto sem o elemento {} : {}'.format(chave, self._pilha_um))
