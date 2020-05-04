# Linked List Data Structure
# Geeks for Geeks

# Disadvantage - slow to get Nth element O(n)
# Advantage - insert and delete can be quick

# Node class
class Node:

    # Function to initalize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList Class
class LinkedList:

    # Function to initalize the LinkedList object
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

if __name__=='__main__':


    # Start with the empty LinkedList
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second
    second.next = third

    llist.printList()
