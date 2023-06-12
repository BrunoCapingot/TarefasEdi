from Estruturas.DuplicatedLinkedList.Node import Node


class DuplicatedLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, elemento):
        if self.head:
            pointer = self.head
            while pointer.next:
                pointer = pointer.next
            new_node = Node(elemento)
            new_node.prev = pointer
            pointer.next = new_node
            self.tail = new_node
        else:
            new_node = Node(elemento)
            self.head = new_node
            self.tail = new_node
        self._size += 1

    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __getitem__(self, index):
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range")

    def __setitem__(self, index, elemento):
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
                i += 1
        raise ValueError("{} não está na lista".format(elemento))

    def _getNode(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("list index out of range")
        pointer = self.head
        for _ in range(index):
            pointer = pointer.next
        return pointer

    def insert(self, index, elemento):
        if index == 0:
            new_node = Node(elemento)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
        elif index == self._size:
            self.append(elemento)
        else:
            pointer = self._getNode(index - 1)
            new_node = Node(elemento)
            new_node.next = pointer.next
            if pointer.next:
                pointer.next.prev = new_node
            pointer.next = new_node
            new_node.prev = pointer
        self._size += 1

    def remove(self, elemento):
        pointer = self.head
        while pointer:
            if pointer.data == elemento:
                if pointer.prev:
                    pointer.prev.next = pointer.next
                else:
                    self.head = pointer.next
                if pointer.next:
                    pointer.next.prev = pointer.prev
                else:
                    self.tail = pointer.prev
                self._size -= 1
                return True
            pointer = pointer.next


    def __repr__(self):
        r = ''
        pointer = self.head
        while pointer:
            r += str(pointer.data) + "<->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


lista_duplamente_encadeada = DuplicatedLinkedList()
lista_duplamente_encadeada.insert(0, 666)
lista_duplamente_encadeada.insert(1, 333)
lista_duplamente_encadeada.insert(2, 444)
lista_duplamente_encadeada.insert(3, 555)
lista_duplamente_encadeada.remove(444)
print(lista_duplamente_encadeada)

print(lista_duplamente_encadeada.index(444))
lista_duplamente_encadeada.append(777)
print(lista_duplamente_encadeada)
print(lista_duplamente_encadeada[2])
