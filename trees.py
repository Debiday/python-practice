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
# keep the tree balanced by creating a complete tree,
# each level has all of its nodes
# 2*parent position to get left child and 2*p + 1 for right  

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

#methods for insertion
def percUp(self, i):
    while i // 2 > 0:
        if self.heapList[i] < self.heapList[i // 2]:
            tmp = self.heapList[i //2]
            self.heapList[i // 2] = self.heapList[i]
            self.heapList[i] = tmp
        i = i // 2
    
def insert(self, k):
    self.heapList.append(k)
    self.currentSize = self.currentSize + 1
    self.percUp(self.currentSize)

# percDown and minChild
def percDown(self, i):
    while(i * 2) <= self.currentSize:
        mc = self.minChild(i)
        if self.heapList[i] > self.heapList[mc]:
            tmp = self.heapList[i]
            self.heapList[i] = self.heapList[mc]
            self.heapList[mc] = tmp
        i = mc

def minChild(self, i):
    if i * 2 + 1 > self.currentSize:
        return i * 2
    else: 
        if self.heapList[i*2] < self.heapList[i*2+1]:
            return i * 2
        else:
            return i * 2 + 1

def delMin(self):
    retval = self.heapList[1]
    self.heapList[1] = self.heapList[self.currentSize]
    self.currentSize = self.currentSize - 1
    self.heapList.pop()
    self.percDown(1)
    return retval

#code to build the heap
def buildHeap(self, alist):
    i = len(alist) // 2
    self.currentSize = len(alist)
    self.heapList = [0] + alist[:]
    while (i > 0):
        self.percDown(i)
        i = i - 1

# _________________________________________________________
# binary search trees (implementation)
# _________________________________________________________
# bst property: to the left, everything less in the box to the left
# only refers to the direct parent

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size
    
    #allows you to use the built in search method on the BST
    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

# _________________________________________________________
# tree node recap (how it works and basic functions)
# _________________________________________________________
class TreeNode: 

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    











