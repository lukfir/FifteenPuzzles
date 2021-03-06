import numpy as np
from Node import Node
import sys, time
from queue import Queue

class Bfs(object):
    """description of class"""

    def __init__(self, startNode, endNode, settings):
        self.__start = startNode
        self.__end = endNode
        self.__visited = {}
        self.__queue = Queue()
        self.solutionNode = None
        self.__settings = settings
        self.counterNodes = 0
        

    def solve(self):

        moves = np.array(['G', 'D', 'L', 'P'])

        self.__queue.put(self.__start)

        if(self.__settings[0]!='R'):
            moves = self.__settings
        
        while not self.__queue.empty() and not self.solutionNode:
            lastNode = self.__queue.get()

            if lastNode == self.__end and not self.solutionNode: 
                self.solutionNode = lastNode
                break
                
            if lastNode.hash in self.__visited: continue
            children = lastNode.getChildren()
            if(self.__settings[0]=='R'):
                np.random.shuffle(moves)

            for move in moves:
                if move in children:
                    newNode = Node(children[move], lastNode, move)
                    if newNode.hash in self.__visited: continue
                    self.__queue.put(newNode)

            self.__visited[lastNode.hash] = None
            self.counterNodes += 1
       
