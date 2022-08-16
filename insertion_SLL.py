class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertion(self, data, location):
        newNode = Node(data)
        if self.head is None:               #if node does not exist
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:               #inserting at the beginning of SLL
                newNode.next = self.head
                self.head = newNode
            elif location == 1:             #inserting at the end of SLL
                self.tail.next = newNode
                self.tail = newNode
                newNode.next = None
            else:                           #inserting at Kth location
                tempNode = self.head
                index = 0
                while index < location-2:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traversing(self):
        if self.head is None:
            return "Sorry"
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
    # def reversedLinkedList(self):
    

singly_linked_list = SinglyLinkedList()
singly_linked_list.insertion(1,0)
singly_linked_list.insertion(2,1)
singly_linked_list.insertion(3,2)
singly_linked_list.traversing()