from Estruturas.fila.Queue import Queue


class Aviao:
    def __init__(self, nome, indenticacao):
        self.nome = nome
        self.indenticacao = indenticacao

    def getName(self): return self.nome

    def getIndenticacao(self): return self.indenticacao


class Numero3:
    def __init__(self):
        self.filaParaDecolar = Queue()
        self.filaAuxiliar = Queue()

    def aguardandoDecolagem(self):
        print("Aguardadndo decolagem o total de: " + str(len(self.filaParaDecolar)))

    def autorizarDecolagem(self):
        if not self.filaParaDecolar.isEmpty():
            aviao = self.filaParaDecolar.pop()
            print('Decolagem autorizada para: ' + str(aviao))
        else:
            print('Nenhum aviao para decolar')

    def adicionarAviaoFila(self,nome,id):
        elemento = [nome,id]
        self.filaParaDecolar.push(elemento)

    def listarFilaDecolagem(self):
        if not self.filaParaDecolar.isEmpty():
            while not self.filaParaDecolar.isEmpty():
                c = self.filaParaDecolar.pop()
                print('Decolagem para:')
                print('Nome: '+c[0])
                print('Identificacao: '+str(c[1]))
                print('Pronto para decolar')
                print('---------ProximoAviao---------')
                self.filaAuxiliar.push(c)
        else:
            print('Não a aviões disponiveis para decolagem')
        while not self.filaAuxiliar.isEmpty():
            c = self.filaAuxiliar.pop()
            self.filaParaDecolar.push(c)

    def listagemCaracteristicasPrimeiro(self):
            c = self.filaParaDecolar.peek()
            print('\n---------PrimeiroAviao---------')
            print('Decolagem para:')
            print('Nome: ' + c[0])
            print('Identificacao: ' + str(c[1]))
            print('Pronto para decolar')


