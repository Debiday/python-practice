# Pros
# Constant time insertion and deletion at any position
# In comparison, arrays are O(n)(linear)
# No need to specify size beforehand unlike array (Amortization)

# Cons:
# To access an element, need linear time to go from head to tail
# In comparison, arrays are constant time
#_________________________________________________________
# Singly linked list
#_________________________________________________________
class Node(object):
    
    def __init__(self, value):

        self.value = value
        self.nextnode = None
#running a node
# >>> a = Node(1)
# >>> b = Node(2)
# >>> c = Node(3)
# >>> a.nextnode = b
# >>> b.nextnode = c
# >>> a.nextnode.value //2
#_________________________________________________________
# Doubly linked list
#_________________________________________________________
# Allow greater variety of O(1) constant time update incl. insert/ delete
# Header, Trailer, Sentinals (dummy nodes)

class DoublyLinkedListNode(object):

    def __init__(self, value):

        self.value = value
        self.nextnode = None
        self.prevnode = None

# >>> a = DoublyLinkedListNode(1)
# >>> b = DoublyLinkedListNode(2)
# >>> c = DoublyLinkedListNode(3)
# >>> a.nextnode = b
# >>> b.prevnode = a
# >>> b.nextnode = c
# >>> c.prevnode = b
#_________________________________________________________
# Singly linked list cycle check (Common!)
#_________________________________________________________
def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 != None and marker2.next_node != None:

        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True
        
    return False
#_________________________________________________________
# Linked list reversal
#_________________________________________________________



#_________________________________________________________
# 
#_________________________________________________________
#_________________________________________________________
# 
#_________________________________________________________
#_________________________________________________________
# 
#_________________________________________________________
#_________________________________________________________
# 
#_________________________________________________________