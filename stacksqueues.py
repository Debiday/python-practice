#LIFO
#_________________________________________________________
# Stack
#_________________________________________________________
class Stack(object):

    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]
        #returns the last item in the list

    def size(self):
        return len(self.items)
#_________________________________________________________
# Queue
#_________________________________________________________
class Queue(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)
    #3,2,1,0

    def dequeue(self):
        return self.items.pop()
    #3,2,1

    def size(self):
        return len(self.items)

    

    




    

#_________________________________________________________
# Deque
#_________________________________________________________
class Deque(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.insert(0, item)
    #add in the front of the queue, the rear of the queue because it's oldest?

    def addFront(self, item):
        self.items.append(item)
    #add in at the back, which is the front of the queue?

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
#_________________________________________________________
#
#_________________________________________________________