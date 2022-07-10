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

    def append(self,element):
        if element:
            if self.isEmpty():
                node = Node(element)
                self.head = self.tail = node
                self.numElements += 1
                
            else:
                node = Node(element)
                self.tail.next = node
                node.previous = self.tail
                self.tail = node
                self.numElements += 1
        else:
            raise IndexError ("\nElement is null!\n")

    def insertHead(self,element):
        pass

    def insert(self,element,position):
        pass

    def removeTail(self,element):
        pass

    def removeHead(self,element):
        pass

    def remove(self,element,position):
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

            
    def printNumberElementsList(self):
        print("\nThe number of elements is: " + str(self.numElements))

dList = DoublyLinkedList()

# Teste Append
#dList.append(10)
#dList.append(15)
#dList.append(20)

# Teste Print List
#dList.printList(dList.head)
#dList.printListInverse(dList.tail)


#dList.printNumberElementsList()
