
class Node:#create class to contain values

    def __init__(self, val, tot):
        self.value = val
        self.total = tot

    def __hash__(self):#make node hashable in dictionary
        return hash(id(self))

    def __eq__(self, other):
        return (id(self) == id(other))

    def __ne__(self, other):
        return not(id(self) == id(other))
    def __lt__(self, other):
        return (self.total < other.total)
    def __gt__(self, other):
        return (self.total > other.total)
    def __le__(self, other):
        return (self.total <= other.total)
    def __ge__(self, other):
        return (self.total >= other.total)
    def __cmp__(self,other):
        return cmp(self.total, other.total)
    

import os
import operator
from collections import defaultdict
import heapq
infinity = 10**10
print os.getcwd()

behemoth = open("matrix.txt","r")
test = open("test.txt","r")

class Graph:

    def __init__(self):
        print 'initiate object'
        self.tableSize = 0
        self.table = []
        self.tableDict = defaultdict(list)
        
    def bfs_paths(self):#calculate all paths to bottom
        print 'paths'
        #print self.table[0][0],' ', self.table[0][0].value
        visited = []
        heap = []
        self.table[0][0].total = self.table[0][0].value
        heapq.heappush(heap,(self.table[0][0]))#start at head of tree
        visited.append(self.table[0][0])
        #print len(self.tableDict)
        while heap:
            
            (vertex) = heapq.heappop(heap)
            for next in set(self.tableDict[vertex]):#get non visited nodes
                if next == self.table[self.tableSize][self.tableSize]:
                    return vertex.total + next.value
                else:#updating the total for nodes in visited
                    if next not in visited:
                        next.total = next.value + vertex.total
                        visited.append(next)
                        heapq.heappush(heap,(next))#add to queue children
                    else:
                        for n in visited:
                            if n == next:
                                if n.total > next.total:
                                    n.total = next.total

            
    
    def readFile(self, file):
        print 'readFile'
        self.table = [[Node(int(n),infinity) for n in s.split(",")] for s in file.readlines()] #create table of nodes
        #print len(self.table[0])-1
        self.tableSize = len(self.table) - 1

    def createTable(self):
        print 'createTable'
        for i in range(self.tableSize+1):
            for n in range(len(self.table[i])):
                #print 'i: ', i , ' n: ', n
                if i == 0 and n == 0:#top left
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])#connect nodes to children nodes
                elif i == 0 and n == self.tableSize:#top right
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes
                elif i == self.tableSize and n == 0:#bottom left
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                elif i == self.tableSize and n == self.tableSize:#bottom right
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes

                #______________________________________
                elif i in range(1,self.tableSize) and n == self.tableSize :#right col
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                elif i == 0 and n in range(1,self.tableSize):#top row
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])#connect nodes to children nodes
                elif i in range(1,self.tableSize) and n == 0:#left col
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])#connect nodes to children nodes
                elif i == self.tableSize and n in range(1,self.tableSize):#bottom row
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])#connect nodes to children nodes
                else:
                    self.tableDict[self.table[i][n]].append(self.table[i-1][n])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n-1])#connect nodes to children nodes
                    self.tableDict[self.table[i][n]].append(self.table[i][n+1])
                    self.tableDict[self.table[i][n]].append(self.table[i+1][n])

        #for n in self.tableDict:
            #print n.value, ' : '
            #for x in self.tableDict[n]:
                #print (x.value)
            #print '__________'


t = Graph()
t.readFile(test)
t.createTable()
print t.bfs_paths()

x = Graph()
x.readFile(behemoth)
x.createTable()
print x.bfs_paths()
