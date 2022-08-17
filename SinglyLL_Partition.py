# Write a code to partition linked list around a value X, such that all nodes less than X come before all nodes greater than or equals to X

from random import randint
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion(self, dataValue, x):
        newNode = Node(dataValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = None
        else:
            if x > dataValue:
                newNode.next = self.head
                self.head = newNode
            else:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
    
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
    sll.insertion(randint(0,50), 25)
print(sll.printSLL())