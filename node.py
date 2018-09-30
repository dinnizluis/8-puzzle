from board import *

class Node:
    def __init__(self, board):
        self.children = []
        self.board = board
        self.height = 1

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

    def swap(self, a, b):
        lst = self.getBoard().getConf().copy()
        lst[b], lst[a] = lst[a], lst[b]
        return lst

    def haveKid(self):
        zero = self.getBoard().findZero()
        board = Board()
        if zero == 0:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero+1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else:
                    self.children[i].haveKid()
        elif zero == 2:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero-1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else:
                    self.children[i].haveKid()
        elif zero == 6:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero+1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero-3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else:
                    self.children[i].haveKid()
        elif zero == 8:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero-1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero-3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else:
                    self.children[i].haveKid()
        elif zero == 1:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero+1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+3))
            new_nodeM = Node(board)
            board.setConf(self.swap(zero, zero-1))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeM)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else: #If not final call the method again until it finds a leaf
                    self.children[i].haveKid()
        elif zero == 3:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero+1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+3))
            new_nodeM = Node(board)
            board.setConf(self.swap(zero, zero-3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeM)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else: #If not final call the method again until it finds a leaf
                    self.children[i].haveKid()
        elif zero == 5:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero-1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+3))
            new_nodeM = Node(board)
            board.setConf(self.swap(zero, zero-3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeM)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else: #If not final call the method again until it finds a leaf
                    self.children[i].haveKid()
        elif zero == 7:
            #Create new nodes according to the father
            board.setConf(self.swap(zero, zero-1))
            new_nodeL = Node(board)
            board.setConf(self.swap(zero, zero+1))
            new_nodeM = Node(board)
            board.setConf(self.swap(zero, zero-3))
            new_nodeR = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_nodeL)
            self.children.append(new_nodeM)
            self.children.append(new_nodeR)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else: #If not final call the method again until it finds a leaf
                    self.children[i].haveKid()
        elif zero == 4:
            #Create new nodes according to the father
            board.setConf(swap(zero, zero-1))
            new_node0 = Node(board)
            board.setConf(swap(zero, zero+1))
            new_node1 = Node(board)
            board.setConf(swap(zero, zero+3))
            new_node2 = Node(board)
            board.setConf(swap(zero, zero-3))
            new_node3 = Node(board)
            #Add new nodes to the list of children
            self.children.append(new_node0)
            self.children.append(new_node1)
            self.children.append(new_node2)
            self.children.append(new_node3)
            #Increment height
            self.height += 1
            #Test if one of the new nodes is final
            for i in range(len(self.children)):
                if self.children[i].getBoard().isFinal():
                    return True
                else:
                    self.children[i].haveKid()
        else:
            #Statement of error
            return False
