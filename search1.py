# Cracking the Coding Interview - Search

# Depth-First Search (DFS)
def search(root):
    if root == None:
        return
    print(root)
    root.visited = True
    for i in root.adjacent:
        if i.visited == false:
            search(i)


# Breadth-First Search (BFS) - Remember to use a Queue Data Structure
def search(root):
    queue = Queue()                 # Declare a Queue object
    root.marked = True              # Set the root node marked parameter equal to True
    queue.enqueue(root)             # Add to the end of the queue

    while not queue.isEmpty():      # While the Queue is not empty
        r = queue.dequeue()         # Remove from the front of the queue
        print(r)                    # Print the returned dequeued node
        for i in r.adjacent:        # for every node in the adjacent nodes
            if i.marked == False:   # if they are marked as False
                i.marked = True     # set them to True
                queue.enqueue(i)    # Add them to the Queue

# Bidirectional Search Uses 2 Breadth-First Searches
# This is used for to find the shortest path ebetween a source and destination node
