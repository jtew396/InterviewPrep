class MyQueue:
    def __init__(self):
        self.stackNewest = MyStack()    # Has the newest elements on top
        self.stackOldest = MyStack()    # Has the oldest elements on top

    def add(self, data):
        # Push onto stackNewest, which always has the newest elements on top
        self.stackNewest.push(data)

    # Move elements from stackNewest onto stackOldest.
    # This is usually done so that we can do operations on stackOldest.
    def shiftStacks(self):
        if stackOldest.isEmpty():
            while not stackNewest.isEmpty():
                stackOldest.push(stackNewest.pop())

    def peek(self):
        shiftStacks()
        return stackOldest.peek()

    def remove(self):
        shiftStacks()
        return stackOldest.pop()




class MyStack:
    def __init__(self):
        self.top = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def push(self, data):
        t = self.Node(data)
        t.next = self.top
        self.top = t

    def pop(self):
        if self.top == None:
            return
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top == None:
            return
        return self.top.data

    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
