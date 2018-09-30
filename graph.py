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
        zero = self.getRoot().getBoard().findZero()
        conf = self.getRoot().getBoard().getConf()

        if zero == 0:
            new_nodeL = self.getRoot().swap(zero, zero+1)
            new_nodeR = self.getRoot().swap(zero, zero+3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
            #Here comes the growth of the search tree, but how?
            self.root.children[0].
        elif zero == 2:
            new_nodeL = self.getRoot().swap(zero, zero-1)
            new_nodeR = self.getRoot().swap(zero, zero+3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 6:
            new_nodeL = self.getRoot().swap(zero, zero+1)
            new_nodeR = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 8:
            new_nodeL = self.getRoot().swap(zero, zero-1)
            new_nodeR = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 1:
            new_nodeL = self.getRoot().swap(zero, zero+1)
            new_nodeM = self.getRoot().swap(zero, zero+3)
            new_nodeR = self.getRoot().swap(zero, zero-1)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeM)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 3:
            new_nodeL = self.getRoot().swap(zero, zero+1)
            new_nodeM = self.getRoot().swap(zero, zero+3)
            new_nodeR = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeM)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 5:
            new_nodeL = self.getRoot().swap(zero, zero-1)
            new_nodeM = self.getRoot().swap(zero, zero+3)
            new_nodeR = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeM)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 7:
            new_nodeL = self.getRoot().swap(zero, zero-1)
            new_nodeM = self.getRoot().swap(zero, zero+1)
            new_nodeR = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_nodeL)
            self.getRoot().haveKid(new_nodeM)
            self.getRoot().haveKid(new_nodeR)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        elif zero == 4:
            new_node0 = self.getRoot().swap(zero, zero-1)
            new_node1 = self.getRoot().swap(zero, zero+1)
            new_node2 = self.getRoot().swap(zero, zero+3)
            new_node3 = self.getRoot().swap(zero, zero-3)
            self.getRoot().haveKid(new_node0)
            self.getRoot().haveKid(new_node1)
            self.getRoot().haveKid(new_node2)
            self.getRoot().haveKid(new_node3)
            self.height += 1
            children  = self.getRoot().getChildren()
            board = Board()
            node = Node(board)
            for i in range(len(children)):
                board.setConf(children[i])
                if board.isFinal():
                    return True
        else:
            #Statement of error
            return False
