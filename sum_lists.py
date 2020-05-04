class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = Node(data)

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def sumLists(ll1, ll2):

    ll3 = LinkedList()
    currentll1 = ll1.head
    currentll2 = ll2.head
    carry = 0

    ll3.append((currentll1.data + currentll2.data) % 10)
    carry = int((currentll1.data + currentll2.data) / 10)

    while currentll1.next != None and currentll2.next != None:
        currentll1 = currentll1.next
        currentll2 = currentll2.next
        ll3.append((carry + currentll1.data + currentll2.data) % 10)
        carry = int((currentll1.data + currentll2.data) / 10)

    if carry > 0:
        ll3.append(carry)

    ll3.printList()

if __name__=='__main__':
    ll1 = LinkedList()
    ll1.append(7)
    ll1.append(1)
    ll1.append(6)
    # ll1.printList()

    ll2 = LinkedList()
    ll2.append(5)
    ll2.append(9)
    ll2.append(2)
    # ll2.printList()

    sumLists(ll1, ll2)
