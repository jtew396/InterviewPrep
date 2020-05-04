# Tree Data Structure
# HackerRank
#
# Binary Search Tree

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, value):
        if value <= self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.data)
        if self.right != None:
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.data)
        if self.left != None:
            self.left.printPreOrder()
        if self.right != None:
            self.right.printPreOrder()

    def printPostOrder(self):
        if self.left != None:
            self.left.printPostOrder()
        if self.right != None:
            self.right.printPostOrder()
        print(self.data)

if __name__=='__main__':

    tree1 = Node(10)
    tree1.insert(5)
    tree1.insert(8)
    tree1.insert(15)
    tree1.printInOrder()
