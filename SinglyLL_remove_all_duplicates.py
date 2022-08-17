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

    def removeDuplicate(self):
        print("\nAfter removing all duplicates: ")
        tempNode = self.head
        unique = []
        unique.append(tempNode.data)
        while tempNode:
            flag = 0
            if tempNode.next == self.tail and tempNode.next.data in unique:
                tempNode.next = None
                break
            if tempNode.next.data not in unique:
                unique.append(tempNode.next.data)
            else:
                nextNode = tempNode.next.next
                tempNode.next = nextNode
                flag = 1
            if flag != 1:
                tempNode = tempNode.next
            if tempNode.next is None:
                break

sll = SinglyLinkedList()
for _ in range(0, 10):
    sll.insertion(randint(0,25))
print(sll.printSLL())
sll.removeDuplicate()
print(sll.printSLL())