from board import *

class Node:
    def __init__(self, board):
        self.children = []
        self.board = board

    #Setters
    def setChildren(self, lst):
        self.children = lst.copy()

    def setBoard(self, board):
        self.board = board.copy()

    #Getters
    def getChildren(self):
        return self.children

    def getBoard(self):
        return self.board

    def haveKid(self, node):
        self.children.append(node)

    def swap(self, a, b):
        lst = self.getBoard().getConf().copy()
        lst[b], lst[a] = lst[a], lst[b]
        return lst
