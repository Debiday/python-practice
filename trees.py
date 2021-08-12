# _________________________________________________________
# functions
# _________________________________________________________
def BinaryTree(r):
    return [r,[], []]

def insertLeft(root, newBranch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else: 
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else: 
        root.insert(2, [newBranch, [], []])
    return root


#access functions
def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]
# _________________________________________________________
# OO Tree
# _________________________________________________________
class BinaryTree(object):
    """
    >>> r =  BinaryTree(3)
    >>> insertLeft(r, 4)
    [3, [4, [], []], []]
    >>> insertLeft(r, 5)
    [3, [5, [4, [], []], []], []]
    >>> insertRight(r, 6)
    [3, [5, [4, [], []], []], [6, [], []]]
    >>> insertRight(r, 7)
    [3, [5, [4, [], []], []], [7, [], [6, [], []]]]
    >>> l = getLeftChild(r)
    >>> print(l)
    [5, [4, [], []], []]
    >>> setRootVal(l, 9)
    """

    def __init__(self, rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode) 
        else: 
            t = BinaryTree(newNode)
            #push the existing left child one level down in the tree
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            #set self.rightchild
            self.rightChild = t

    # access methods (4)
    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

# _________________________________________________________
# three tree traversals
# _________________________________________________________
#preorder function (outside implementation)
def preorder(tree):
    if tree: 
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#preorder method(inside implementation)
def preorder2(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

#postorder
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

#inorder
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# _________________________________________________________
# priority queues with binary heaps
# _________________________________________________________










