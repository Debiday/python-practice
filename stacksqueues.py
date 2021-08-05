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

    def peek(self):
        return self.items[-1]

    

    




    

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
# Stack practice
#_________________________________________________________
class Stack2(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

#_________________________________________________________
# Queue practice
#_________________________________________________________
class Queue2(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

#_________________________________________________________
# Deque practice
#_________________________________________________________
class Deque2(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#_________________________________________________________
# Balanced parenthesis check
#_________________________________________________________
def balance_check(s):

    if len(s) % 2 != 0:
        return False

    opening = set('({[')
    matches = set([('(',')'),('[',']'),('{', '}')])  

    stack = []

    for paren in s:
        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
                #no matching paren

            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False
            
    return len(stack) == 0
#or
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        while ("()" in s) or ("{}" in s) or ("[]" in s):
            for i in range(len(s)):
                if ("[]") in s:
                    s = s.replace("[]","")
                elif ("()") in s:
                    s = s.replace("()","")
                    print('t')
                elif ("{}") in s:
                    s = s.replace("{}","")
        return s==""
#_________________________________________________________
# Queue two stacks
#_________________________________________________________
class Queue2Stacks(object):

    def __init__(self):
        self.input = []
        self.output = []

    def enqueue(self, element):
        self.input.append(element)

    def dequeue(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()
#_________________________________________________________
# Write a task manager with a queue
#_________________________________________________________
# task_queue = Queue()

# while True:

#     if task_queue.isEmpty():
#         next_task = None
#     else:
#         next_task = task_queue.peek()

#     print("Next task", next_task)

#     command = input("A)dd task, D)o first tast, or Q)uit? ")

#     if command == "A":
#         task = input("Task: ")
#         task_queue.enqueue(task)

#     elif command == "D":
#         print("Completed:", task_queue.dequeue())
    
#     elif command == "Q":
#         break

#     else:
#         print("Invalid Command, try again.")