# Linked List Data Structure
# Double Linked List

# Node class
class Node:

    # Function to initailize the node object
    def __init__(self, data):
        # Give the Node object a data method that is equal to the data
        self.data = data

        # The following methods will be used to point to next and/or previous Nodes
        # Give the Node object a next method that is equal to None
        self.next = None
        # Give the Node object a previous method that is equal to None
        self.previous = None

# Doubly LinkedList class
class LinkedList:

    # Function to initialize the LinkedList object
    def __init__(self):
        # Give the LinkedList a head method equal to None
        self.head = None
        # Give the LinkedList a foot method equal to None
        self.foot = None

    # Function to append a Node object to the LinkedList object
    def append(self, data):
        # If the head node does not exist
        if self.foot == None:
            # Create a node that will be head and foot
            self.head = Node(data)
            self.foot = self.head
            return

        # Set a variable current to the head node
        current = self.head

        # While the current.next is not equal to None (haven't reached the end)
        while current.next != None:
            # Step through to the next Node in the LinkedList
            current = current.next

        # When the next node does not exist we're at the end of the LinkedList
        # Set the current.next pointer equal to the new Node object
        current.next = Node(data)

    # Function to prepend a Node object to the LinkedList object
    def prepend(self, data):
        # Declare a new head Node object
        newHead = Node(data)
        # Set the new head node.next pointer equal to current LinkedList head
        newHead.next = self.head
        # Set the LinkedList head node to the newHead Node object
        self.head = newHead

    def deleteWithValue(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            sefl.head = self.head.next
            return

        current = self.head

        while current.next != None:
            if current.next.data == data:
                current.next = curent.next.next
                return
            current = current.next

    def prepend()
