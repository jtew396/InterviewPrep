# Cracking the Coding Interview Queue Example

class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def add(self, data):
        t = self.Node(data)
        if self.last != None:
            self.last.next = t
        self.last = t
        if self.first == None:
            self.first = self.last

    def remove(self):
        if self.first == None:
            return
        data = self.first.data
        self.first = self.first.next
        if self.first == None:
            self.last = None
        return data

    def peek(self):
        if self.first == None:
            return
        return self.first.data

    def isEmpty(self):
        if self.first == None:
            return True
        else:
            return False

queue1 = MyQueue()
queue1.add(1)
queue1.add(2)
queue1.add(3)
print(queue1.peek())
queue1.remove()
print(queue1.peek())
