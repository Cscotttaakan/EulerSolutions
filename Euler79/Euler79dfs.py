import os
import operator
from collections import defaultdict
print os.getcwd()
file = open("keylog_test.txt", "r")
file2 = open("keylog.txt", "r")
class Graph:

    def __init__(self):
        print 'initiate object'
        self.table = []
        self.tableDict = defaultdict(list)
        
    def dfs_paths(self):#get paths
        queue = []
        visited = []
        for n in self.tableDict: #iterate through options in dictionary
            queue.append(n)
            visited.append(n)
            while(queue):

                next = queue.pop(0)
                if next in self.tableDict:
                    for a in self.tableDict[next]:
                        queue.insert(0,a)#use stack method
                visited.append(next)
                visited = self.removeDup(visited)
                queue = self.removeDup(queue)
            yield visited
            visited = []
        


    def readFile(self, file):#create node table
        print 'readFile'
        self.table = [[int(n) for n in s.split()] for s in file.readlines()]
        
    def createTable(self):#link nodes
        print 'createTable'
        tempTable = defaultdict(list)
        for i in range(len(self.table)):#create i x 3 table, but has duplicates
                    tempTable[self.table[i][0]].append(self.table[i][1])
                    tempTable[self.table[i][0]].append(self.table[i][2])
                    tempTable[self.table[i][1]].append(self.table[i][2])

        self.tableDict = dict((k,self.removeDup(v)) for k,v in tempTable.items()) #remove duplicates
        for x in self.tableDict:#remove connected nodes
            for n in self.tableDict[x]:
                self.cleanNodes(n,x)
        
                                    
    def cleanNodes(self, key,parent):#if a node contains children in the list, remove those in list
        if key in self.tableDict:
            for z in self.tableDict[key]:
                if z in self.tableDict[parent]:#checking children of vertices to see if they are contained
                    self.tableDict[parent].remove(z)
                    self.cleanNodes(z,parent) #recursive

    def removeDup(self, list):#remove duplications in list
        s = []
        for i in list:
            if i not in s:
                s.append(i)
        return s

    def returnKey(self):#return path with length of total unique numbers, not less
        self.a = self.dfs_paths()
        for b in self.a:
            if len(b) > len(self.tableDict):
                return b
            
    
#for n in a:
#    print sum(n)

g = Graph()
g.readFile(file)
g.createTable()
print 'Shortest Key: ',g.returnKey()

x = Graph()
x.readFile(file2)
x.createTable()
print 'Shortest Key: ',x.returnKey()

