from turtle import pos
from node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.numElements = 0
        self.exist = False

    def isEmpty(self):
        if self.head == self.tail == None:
            return True
        else:
            return False

    def insertEmptyList(self,element):
        node = Node(element)
        self.head = self.tail = node
        self.numElements += 1

    def append(self,element):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                node = Node(element)
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
                self.numElements += 1
        else:
            raise IndexError ("\nElement is null!\n")

    def insertHead(self,element):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                node = Node(element)
                node.next = self.head
                self.head.previous = node
                self.head = node
                self.numElements += 1
        else:
            raise IndexError ("\nElement is null!\n")

    def insert(self,element,position):
        if element != None:
            if self.isEmpty():
                self.insertEmptyList(element)
            else:
                if position == self.numElements:
                    self.append(element)
                elif position == 1:
                    self.insertHead(element)
                elif position == 0:
                    print("\nPosition does not exist!\n")
                else:
                    node = Node(element)
                    nodeAux = self.head
                    for index in range(position-2):
                        nodeAux = nodeAux.next
                    
                    node.previous = nodeAux
                    node.next = nodeAux.next

                    nodeAux.next.previous = node
                    nodeAux.next = node
                    self.numElements += 1
        else:
            raise IndexError ("\nElement is null!\n")
                
    def removeTail(self):
        if self.isEmpty():
            print("\nEmpty List!\n")
        elif self.head == self.tail:
            print("There is only one [1] element!")
            self.head = self.tail = None
            self.numElements = 0
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            self.numElements -= 1

    def removeHead(self):
        if self.isEmpty():
            print("\nEmpty List!\n")
        elif self.head == self.tail:
            print("There is only one [1] element!")
            self.head = self.tail = None
            self.numElements = 0
        else:
            self.head = self.head.next
            self.head.previous = None
            self.numElements -= 1

    def removePosition(self,position):
        if position != None:
            if self.isEmpty():
                print("\nEmpty List!\n")
            elif position == self.numElements:
                self.removeTail()  
            elif position > self.numElements:
                print(f"\nThe position {position} does not exist in the list!\n")
            elif position == 1:
                self.removeHead()
            else:
                positionAux = self.head
                for index in range(self.numElements-2):
                    if index == position - 2:
                        positionAux.next = positionAux.next.next
                        positionAux.next.previous = positionAux
                        self.numElements -= 1
                    else:
                        positionAux = positionAux.next

    def removeElement(self,element):
        self.exist = False
        if element != None:
            if self.isEmpty():
                print("\nEmpty List!\n")
            elif self.tail.data == element:
                self.removeTail()
            elif self.head.data == element:
                self.removeHead()
            else:
                nodeAux = self.head.next
                for index in range(self.numElements-2):
                    if nodeAux.data == element:
                        nodeAux.previous.next = nodeAux.next
                        nodeAux.next.previous = nodeAux.previous
                        self.numElements -= 1
                        self.exist = True
                    else:
                        nodeAux = nodeAux.next
                if self.exist == False:
                    print(f"\nElement {element} does not exist in the list!\n")
        else:
            raise IndexError ("\nElement is null!\n")    

    def searchElement(self,element):
        if element != None:
            if self.isEmpty():
                print("\nEmpty List!\n")
            elif self.head.data == self.tail.data == element:
                self.printData(self.head.data,1)
            elif self.tail.data == element:
                self.printData(self.tail.data,self.numElements)
            elif self.head.data == element:
                self.printData(self.head.data,1)
            else:
                nodeAux = self.head.next
                for index in range(self.numElements-2):
                    if nodeAux.data == element:
                        self.printData(nodeAux.data,index + 2)
                        self.exist = True
                    else:
                        nodeAux = nodeAux.next
                if self.exist == False:
                    print(f"\nElement {element} does not exist in the list!\n")
        else:
            raise IndexError ("\nElement is null!\n")     

    def searchPosition(self,position):
        if position != None:
            if self.isEmpty():
                print("\nEmpty List!\n")
            elif position == self.numElements:
                self.printData(self.tail.data,position)
            elif position > self.numElements:
                print(f"\nThe position {position} does not exist in the list!\n")
            else:
                positionAux = self.head
                for index in range(self.numElements - 1):
                    if index + 1 == position:
                        self.printData(positionAux.data,position)
                    positionAux = positionAux.next
        else:
            raise IndexError ("\nElement is null!\n")    

    def printData(self,element,position):
        print(f"Element exist in position: {position}")
        print(f"Element is: {element}")
    
    def printList(self,node):
        if self.isEmpty():
            print("\nEmpty List!\n")
        else:
            while (node is not None):
                print(f"Element is: {node.data}")
                node = node.next
    
    def printListInverse(self,node):
        if self.isEmpty():
            print("\nEmpty List!\n")
        else:
            while (node is not None):
                print(f"Element is: {node.data}")
                node = node.previous

    def printHead(self):
        print(f"Head is: {self.head.data}")

    def printTail(self):
        print(f"Tail is: {self.tail.data}")

    def printNumberElementsList(self):
        print("\nThe number of elements is: " + str(self.numElements) + "\n\n")