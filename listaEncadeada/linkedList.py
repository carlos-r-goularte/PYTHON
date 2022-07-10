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
