import os
import operator

print os.getcwd()
file = open("p018_triangle.txt", "r")



table = [[int(n) for n in s.split()] for s in file.readlines()]


# Program to print BFS traversal from a given source
# vertex. BFS(int s) traverses vertices reachable
# from s.
from collections import defaultdict
 
# This class represents a directed graph using adjacency
# list representation
class Node:
    
    def __init__(self,value):
        self.children = []
        self.maximum = 0
        self.val= value
        


        
        
    def addChild(self, child):
        self.children.append(child)

    def __gt__(self, compare):
        return self.children == compare.children
    
    def getVal(self):
        return self.val

class Graph:
    # Constructor
    def __init__(self):
 
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.masterNode = 0
 
    
    # function to add an edge to graph
    def addEdge(self,a,b,c):

        self.graph[a].append(b)
        self.graph[a].append(c)
        
        
 
    # Function to print a BFS of graph
    def bfs(self, start):
        
        visited, queue = [], [self.masterNode]
        
        while queue:
            print queue
            vertex = queue.pop(0)
            
            if vertex not in visited:
                print vertex.getVal(), ' is not in visited'
                visited.append(vertex)
                
                queue.extend(self.graph[vertex])
        return visited


    def printGraph(self):
                 print self.graph

    def readTable(self,file):
        self.masterNode = Node(table[0][0])
        print self.masterNode
        self.addEdge(self.masterNode, Node(table[1][0]),Node(table[1][1]))
        for i in range(1,len(table)-1):
            for n in range(len(table[i])):
                self.addEdge(Node(table[i][n]),Node(table[i+1][0+n]),Node(table[i+1][1+n]))

                
                        
    

# Driver code
# Create a graph given in the above diagram
g = Graph()
g.readTable(table)



print g.bfs('75')


