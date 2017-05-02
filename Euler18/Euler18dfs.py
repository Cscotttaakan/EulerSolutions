
class Node:

    def __init__(self, val):
        self.value = val

    def __hash__(self):
        return hash(id(self))

    def __eq__(self, other):
        return (id(self) == id(other))

    def __ne__(self, other):
        return not(id(self) == id(other))

import os
import operator
from collections import defaultdict
print os.getcwd()
file = open("p018_triangle.txt", "r")
test = open("p018_triangle_test.txt","r")

class Graph:

    def __init__(self):
        print 'initiate object'
        self.table = []
        self.tableDict = defaultdict(list)
        
    def dfs_paths(self):#calculate dfs search bottom
        print 'paths'
        queue = [(self.table[0][0], [self.table[0][0]])]#start at head of tree
        print len(self.table)
        while queue:
            
            (vertex, path) = queue.pop(0)

            for next in set(self.tableDict[vertex]) - set(path):#remove visited
                if next in self.table[len(self.table)-1]:#stop when reach bottom
                    yield path + [next]
                else:
                    print 'Path'
                    for a in path:
                        print a.value
                    queue.insert(0,(next, path + [next]))#changed queue to stack


    def readFile(self, file):#create node table
        print 'readFile'
        self.table = [[Node(int(n)) for n in s.split()] for s in file.readlines()]
        

    def createTable(self):#link nodes
        print 'createTable'
        for i in range(len(self.table)-1):
            for n in range(len(self.table[i])):
                for x in range(2):
                    self.tableDict[self.table[i][n]].append(self.table[i+1][x+n])

    def calculateMax(self):#calculate max of all paths
        self.max = 0
        a = self.dfs_paths()
        for b in a:
            if self.calculateSetTotal(b) > self.max:
                self.max = self.calculateSetTotal(b)

        return self.max

    def calculateSetTotal(self, set):#calculate total of path
        self.total = 0
        for a in set:
            self.total += a.value

        return self.total
    
#for n in a:
#    print sum(n)

g = Graph()
g.readFile(file)
g.createTable()
print g.calculateMax()

n = Graph()
n.readFile(test)
n.createTable()
print n.calculateMax()

