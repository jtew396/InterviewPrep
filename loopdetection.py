class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
            self.head = Node(data)
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = Node(data)

def LoopDetection(loop):

    Turtle =

if __name__=='__main__':
