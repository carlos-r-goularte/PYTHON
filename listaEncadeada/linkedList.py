from ast import Index
from ctypes import pointer
from node import Node

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def append(self,element):
        if self.head:
            #inserir quando a lista já possuir elementos
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(element)
        else:
            #inserir quando a lista está vazia
            self.head = Node(element)
        self.size += 1

    def __len__(self):
        return self.size

    def set(self,index,element):
        pass

    def get(self, index):
        pass

    def __getitem__(self,index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index our of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("List index out of range")

    def __setitem__(self,index,element):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("List index our of range")
        if pointer:
            pointer.data = element
        else:
            raise IndexError("List index out of range")
    