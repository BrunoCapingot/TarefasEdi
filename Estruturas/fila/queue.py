from fila.Node import Node

#inserir na pilha
#remover na pilha
#observar valor de topo

class Queue():
    def __init__(self):
        self.frist = None
        self.last = None
        self._size = 0
    def push(self,elemento):
        #inseri elemento na pilha
        node = Node(elemento)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.frist is None:
            self.frist = node
        self._size = self._size + 1
    def pop(self):
        #remove elemento que esta no topo da pilha
        if self._size > 0:
            elemento = self.frist.data
            self.frist = self.frist.next
            self._size = self._size - 1
            return elemento
        raise IndexError("The queue is empty")
    def peek(self):
        #retorna o topo da pilha para observação, sem remover
        if self._size > 0:
            elemento = self.frist.data
            return elemento
        raise IndexError("The queue is empty")
    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ''
            pointer = self.frist
            while pointer:
                r = r + str(pointer.data) + "->"
                pointer = pointer.next
            return r
        return "None"
    def __str__(self):
        return self.__repr__()




