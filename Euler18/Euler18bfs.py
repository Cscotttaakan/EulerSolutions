
class Node:#create class to contain values

    def __init__(self, val):
        self.value = val

    def __hash__(self):#make node hashable in dictionary
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
behemoth = open("p067_triangle.txt","r")

class Graph:

    def __init__(self):
        print 'initiate object'
        self.table = []
        self.tableDict = defaultdict(list)
        
    def bfs_paths(self):#calculate all paths to bottom
        print 'paths'
        queue = [(self.table[0][0], self.table[0][0].value)]#start at head of tree
        while queue:
            
            (vertex, path) = queue.pop(queue.index(self.searchQueue(queue)))
            for next in set(self.tableDict[vertex]):#get non visited nodes
                if next in self.table[len(self.table)-1]:#check if next is part of the last row
                    return path + next.value#store in bfs_paths object
                else:
                    queue.append((next, path + next.value))#add to queue children


    def searchQueue(self, q):
        print 'search path'
        temp, tempPath = q[0]
        minimum = temp.value
        for node,path in q:
            if path < tempPath:
                minimum = node.value
                temp = node
                tempPath = path
        return (temp,tempPath)
            
    
    def readFile(self, file):
        print 'readFile'
        self.table = [[Node(int(n)) for n in s.split()] for s in file.readlines()] #create table of nodes
        

    def createTable(self):
        print 'createTable'
        for i in range(len(self.table)-1):
            for n in range(len(self.table[i])):
                for x in range(2):
                    self.tableDict[self.table[i][n]].append(self.table[i+1][x+n])#connect nodes to children nodes

    def calculateMax(self):#calculate max value
        self.max = 1000
        a = self.bfs_paths()
        print a
        if self.calculateSetTotal(a) < self.max:
            self.max = self.calculateSetTotal(a)

        return self.max

    def calculateSetTotal(self, set):#calculate total of path
        self.total = 0
        self.total += set

        return self.total
    
#for n in a:
#    print sum(n)

#g = Graph()
#g.readFile(file)
#g.createTable()
#print g.calculateMax()

#n = Graph()
#n.readFile(test)
#n.createTable()
#print n.calculateMax()

t = Graph()
t.readFile(behemoth)
t.createTable()
print t.calculateMax()
