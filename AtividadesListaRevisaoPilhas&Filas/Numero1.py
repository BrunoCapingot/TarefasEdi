from Estruturas.pilha import Stack
from Estruturas.fila.Queue import Queue


class Numero1:
    def __init__(self):
        self._pilha_um = Stack()
        self._pilha_dois = Stack()
        self._pilha_suporte = Stack()
        self._fila_um = Queue()

    def setFrase(self, strings):
        string = strings.replace(" ", "")
        string = string.replace(".", "")
        for c in string:
            self._pilha_suporte.push(c)
            self._pilha_um.push(c)
            self._fila_um.push(c)
        texto = ''
        while not self._pilha_suporte.isEmpty():
            c = self._pilha_suporte.pop()
            texto = texto + c
        print('textoInvertido: ' + texto)
    def condifionaPalindromo(self):
        x = ''
        y = ''
        while True:
            if x is None and y is None:
                break
            x = self._pilha_um.pop()
            y = self._fila_um.pop()
            if x == y:
                self._pilha_dois.push(True)
            else:
                self._pilha_dois.push(False)

    def palindromo(self):
        while not self._pilha_dois.isEmpty():
            c = self._pilha_dois.pop()
            if c == False:
                print('A frase não é um palíndromo')
                return
        print('A frase é um palíndromo')

    def getDataSet(self):
        return self._pilha_um
