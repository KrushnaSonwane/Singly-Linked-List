from random import randint
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion(self, dataValue):
        newNode = Node(dataValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = None
        else:
            newNode.next = self.head
            self.head = newNode
    
    def printSLL(self):
        result = ''
        if self.head is None:
            return result
        else:
            tempNode = self.head
            while tempNode:
                result += str(tempNode.data)
                tempNode = tempNode.next
                if tempNode is None:
                    break
                result += ' -> '
        return result

sll = SinglyLinkedList()
for _ in range(0, 10):
    sll.insertion(randint(0,50))
print(sll.printSLL())