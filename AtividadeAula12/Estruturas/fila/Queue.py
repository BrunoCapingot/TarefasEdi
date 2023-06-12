from Estruturas.fila.Node import Node

class Queue():
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self, elemento):
        # Inserir elemento na fila
        node = Node(elemento)
        if self.last is None:
            self.last = node
        else:
            self.last.next = node
            self.last = node

        if self.first is None:
            self.first = node
        self._size += 1

    def pop(self):
        # Remover elemento que está na frente da fila
        if self._size > 0:
            elemento = self.first.data
            self.first = self.first.next
            self._size -= 1
            return elemento
        else:
            return None

    def peek(self):
        # Retorna o elemento da frente da fila para observação, sem remover
        if self._size > 0:
            elemento = self.first.data
            return elemento
        raise IndexError("The queue is empty")

    def isEmpty(self):
        # Verifica se a fila está vazia
        return self._size == 0

    def __len__(self):
        # Retorna o tamanho da fila
        return self._size

    def __repr__(self):
        if self._size > 0:
            r = ''
            pointer = self.first
            while pointer:
                r += str(pointer.data) + "->"
                pointer = pointer.next
            return r
        return "None"

    def __str__(self):
        return self.__repr__()
