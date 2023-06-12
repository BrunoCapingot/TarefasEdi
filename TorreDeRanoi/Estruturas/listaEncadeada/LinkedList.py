from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def append(self, elemento):
        if self.head:
            # Cria um ponteiro com o mesmo valor apontado na memoria que o self.head
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            pointer.next = Node(
                elemento)  # Guarda novo elemento no novo no e guarda no pointer.next para apontar para o novo elemento
        else:
            # Para primeira inserção
            self.head = Node(elemento)
        self._size = self._size + 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elemento):
        # lista[5] = 9
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elemento
        else:
            raise IndexError("list index out of range")

    def index(self, elemento):
        pointer = self.head
        i = 0
        while pointer:
            if pointer.data == elemento:
                return i
            else:
                pointer = pointer.next
                i = i + 1
        raise ValueError("{} nao esta na lista".format(elemento))

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        return pointer

    def insert(self, index, elemento):
        node = Node(elemento)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, elemento):

        if self.head == None:
            raise ValueError("{} is not in list".format(elemento))

        elif self.head.data == elemento:
            self.head = self.head.next
            self._size = self._size + 1
            return True
        else:
            anterior = self.head
            pointer = self.head.next
            while pointer:
                if pointer.data == elemento:
                    anterior.next = pointer.next
                    pointer.next = None
                anterior = pointer
                pointer = pointer.next
            self._size = self._size - 1
            return True
        raise ValueError("{} is not in list".format(elemento))

    def __repr__(self):
        r = ''
        pointer = self.head
        while pointer:
            r = r+str(pointer.data) + "->"
            pointer = pointer.next
        return r
    def __str__(self):
        return self.__repr__()


lista = LinkedList()
lista.insert(0,666)
lista.insert(1,333)
lista.insert(2,444)
lista.insert(3,555)
lista.remove(666)
print(lista)

#.index
#append
#lista[]
