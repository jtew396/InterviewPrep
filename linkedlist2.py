# Linked List Data Structure
# HackerRank
#
#

# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:

    # Function to initialize the LinkedList class
    def __init__(self):
        self.head = None

    # Function to append a Node object to the LinkedList object
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = Node(data)

    # Function to prepend a Node object to the LinkedList object
    def prepend(self, data):
        newHead = Node(data)
        newHead.next = self.head
        self.head = newHead

    # Function to delete a Node object from the LinkedList object
    def deleteWithValue(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=='__main__':

    llist = LinkedList()
    llist.append(1)
    llist.append(2)
    llist.append(3)
    llist.printList()
    llist.prepend(0)
    llist.printList()
    llist.deleteWithValue(0)
    llist.printList()
