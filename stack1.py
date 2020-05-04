# Cracking the Coding Interview Stack Example

class MyStack:
    def __init__(self):
        self.top = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def pop(self):
        if self.top == None:
            return

        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, data):
        t = self.Node(data)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top == None:
            return
        return self.top.data

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False

stack1 = MyStack()
stack1.isEmpty()
stack1.push(1)
print(stack1.peek())
stack1.push(2)
print(stack1.peek())
