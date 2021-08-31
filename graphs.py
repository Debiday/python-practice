# _________________________________________________________
# adjacency matrix
# _________________________________________________________
#not an efficient way to store sparse data
#good when number of edges is large |V²|
#connectivity: every vertex is connected to another
# _________________________________________________________
# adjacency list
# _________________________________________________________
#more space efficient eay to imp a sparsely connected graph (compact)
class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):

        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph: 

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
        #grab all values and make it into an iterable object

    def __contains__(self, n):
        return n in self.vertList

# g = Graph()

# for i in range(6):
#     g.addVertex(i)

# g.addEdge(0,1,2)

# for vertex in g:
#     print(vertex)
#     print(vertex.getConnections())
#     print('\n')

# _________________________________________________________
# word ladder problem
# _________________________________________________________
#using buckets and dictionaries
def buildGraph(wordFile):
    d = {}
    g = Graph()

    wfile = open(wordFile, 'r')
    #creating buckets of words that differ by one letter
    for line in wfile:
        print(line)
        word = line[:-1]
        print(word)
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    #add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    
    return g

# _________________________________________________________
# breadth first search: finding the shortest solution to word ladder
# _________________________________________________________
#queue
# _________________________________________________________
# implementation of graph, recap
# _________________________________________________________
#stack
from enum import Enum
from collections import OrderedDict

class State(Enum):
    unvisited =  1
    visited = 2
    visiting = 3

class Node:

    def __init__(self, num):

        self.num = num
        self.visit_state = State.unvisited
        self.adjacent = OrderedDict() #key = node, value = weight

    def __str__(self):
        return str(self.num)

class Graph:

    def __init__(self):
        self.nodes = OrderedDict()

    def add_node(self, num):

        node = Node(num)
        self.nodes[num] = node
        return node

    def add_edge(self, source, dest, weight=0):

        if source not in self.nodes:
            self.add_node(source)
        if dest not in self.nodes:
            self.add_node(dest)

        self.nodes[source].adjacent[self.nodes[dest]] = weight
# _________________________________________________________
# implementation of dfs
# _________________________________________________________
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            visited.add(vertex)

            stack.extend(graph[vertex] - visited)

    return visited 
# _________________________________________________________
# implementation of bfs
# _________________________________________________________
#same results as dfs but provides shortet path first
#uses queue
def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue: 
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)

    return visited


#check: return all possible paths