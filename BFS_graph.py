# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 23:47:32 2019

@author: Swathi
"""
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def bfs(self,s):
        visited=[False]*(len(self.graph))
        queue=[]
        queue.append(s)
        visited[s]=True
        while queue:
            s=queue.pop(0)
            print(s,end=" ")
            for i in self.graph[s]:
                if visited[i]==False:
                    visited[i]=True
                    queue.append(i)
    def printGraph(self):
        for u,v in self.graph.items():
            print("For each {} vertex the edge list {}".format(u,v))
g=Graph()
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)
g.bfs(2)
g.printGraph()
                
        
        