from pilha.Stack import Stack
from pilha.Node import Node

class Input():

    def __init__(self):
        dataPilha = Stack()

        while input() != -1:
            notacao = input('Selecione dentro as notaçãoes para Infixa, Pos-Fixa e Pre-fixa ou -1 para sair')
            dataPilha.push(notacao)
        print(dataPilha)




