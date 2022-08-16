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
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()
    
    def deletion(self, location):
        if self.head == None:
            return "Linked List Underflow..!"
        if location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
        elif location == 1:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                node.next = None
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 2:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    def deleteEntireSLL(self):
        if self.head is None:
            print("Linked list already empty..")
        else:
            self.head, self.tail = None, None

singly_linked_list = SinglyLinkedList()
singly_linked_list.insertion(1,0)
singly_linked_list.insertion(2,1)
singly_linked_list.insertion(5,2)
singly_linked_list.insertion(2,2)
singly_linked_list.insertion(2,3)
singly_linked_list.traversing()
singly_linked_list.deletion(3)
singly_linked_list.traversing()
# singly_linked_list.deleteEntireSLL()
# singly_linked_list.traversing()