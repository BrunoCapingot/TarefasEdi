from Estruturas.fila.Queue import Queue
from Numero1 import Numero1
from Numero2 import Numero2
from Numero3 import Numero3
from Numero4 import Numero4
from Numero5 import Numero5
from Numero6 import Numero6
from Numero7 import Numero7
from Numero8 import Numero8


def menu(name):
    if name == 'tarefa 1':
        tarefa = Numero1()
        tarefa.setFrase("arara arara ")
        #arara
        #lalalalalal
        #kbkbkbkbkbk
        tarefa.condifionaPalindromo()
        tarefa.palindromo()
        tarefa.getDataSet()

    elif name == 'tarefa 2':
        tarefa = Numero2()
        tarefa.removerItem(5)
        tarefa.removerItem(44)
        tarefa.removerItem(55)
        tarefa.removerItem(66)
        tarefa.removerItem(77)
        tarefa.removerItem(89)
        tarefa.removerItem(6651)
        tarefa.removerItem(651651)

    elif name == 'tarefa 3':
        tarefa = Numero3()
        while True:
            print("\n=== Controle de Pista de Decolagem ===")
            print("1. Listar número de aviões aguardando")
            print("2. Autorizar decolagem do primeiro avião")
            print("3. Adicionar avião à fila de espera")
            print("4. Listar aviões na fila de espera")
            print("5. Listar características do primeiro avião")
            print("0. Sair")

            cmd = int(input('Comando: '))
            if cmd == 1:
                tarefa.aguardandoDecolagem()
            elif cmd == 2:
                tarefa.autorizarDecolagem()
            elif cmd == 3:
                tarefa.adicionarAviaoFila('BCC',6669875)
            elif cmd == 4:
                tarefa.listarFilaDecolagem()
            elif cmd == 5:
                tarefa.listagemCaracteristicasPrimeiro()

    elif name == 'tarefa 4':
        tarefa = Numero4()
        tarefa.invertaFila()

    elif name == 'tarefa 5':
        fila1 = Queue()
        fila1.push(65)
        fila1.push(44)
        fila1.push(65)
        fila1.push(984)
        fila1.push(222)
        fila1.push(852)
        fila1.push(426)
        fila1.push(871)
        tarefa = Numero5()
        tarefa.inserirMilNumbers()
        tarefa.comparaElementosComExistente(fila1)
        #tarefa.pesquisaInFila(222)

    elif name == 'tarefa 6':
        tarefa = Numero6()
        tarefa.sorteiaNumeros()

    elif name == 'tarefa 7':
        tarefa = Numero7()
        fila = Queue()
        fila.push(556)
        fila.push(656)
        fila.push(65)
        fila.push(899)
        tarefa.inverteFila(fila)

    elif name == 'tarefa 8':
        tarefa = Numero8()


if __name__ == '__main__':
    menu('tarefa 8')

