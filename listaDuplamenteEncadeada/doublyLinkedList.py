from asyncio.windows_events import NULL
from node import Node

class DoublyLinkedList:

    def __init__(self):
        self.head = self.tail = None
        self.numElements = 0

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

    def remove(self,position):
        pass

    def search(self,element):
        pass
    
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

dList = DoublyLinkedList()

# Test Insert Head
#dList.insertHead(10)
#dList.insertHead(20)
#dList.insertHead(50)

# Test Append
dList.append(1)
dList.append(3)
dList.append(4)
dList.append(6)
dList.insert(2,2)
dList.insert(5,5)
dList.insertHead(0)


dList.printList(dList.head)
dList.printHead()
dList.printTail()
dList.printNumberElementsList()



dList.removeHead()

dList.printList(dList.head)
dList.printHead()
dList.printTail()
dList.printNumberElementsList()



dList.removeTail()

dList.printList(dList.head)
dList.printHead()
dList.printTail()
dList.printNumberElementsList()