from random import randint
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # to insert new node at the beginning of Singly Linked List
    def insertion(self, dataValue):
        newNode = Node(dataValue)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = None
        else:
            newNode.next = self.head
            self.head = newNode
    
    # to print all node with visualization
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

    # to find a length of Singly Linked List
    def findLength(self):
        index = 0
        tempNode = self.head
        while tempNode:
            index += 1
            tempNode = tempNode.next
        return index

    # to return K^th last node from Singly Linked List
    def returnKthLatsNode(self, k):
        if k > self.findLength():
            return "Kth node does not exist.."
        else:
            tempNode = self.head
            index = 0
            while tempNode:
                index += 1
                if k-1 == self.findLength() - index:
                    return tempNode.data
                tempNode = tempNode.next

sll = SinglyLinkedList()
for _ in range(0, 10):
    sll.insertion(randint(0,25)) # To genarate random integer from the range of 0 to 25
print(sll.printSLL())
print(sll.returnKthLatsNode(10))