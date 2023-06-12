from pilha.Node import Node

#inserir na pilha
#remover na pilha
#observar valor de topo

class Stack():
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,elemento):
        #inseri elemento na pilha
        node = Node(elemento)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        #remove elemento que esta no topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("A pilha ta vazia")

    def peek(self):
        #retorna o topo da pilha para observação
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha ta vazia")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        r = ''
        pointer = self.top
        while pointer:
            r = r + str(pointer.data) + '\n'
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()




