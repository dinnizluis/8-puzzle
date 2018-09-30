from node import *

class Graph:
    #Constructor
    def __init__(self, node):
        self.root = node
        self.height = 1

    #Getters
    def getRoot(self):
        return self.root

    def getHeight(self):
        return self.height

    def buildGraph(self):
        self.root.haveKid()
