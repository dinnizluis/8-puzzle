from graph import *

#''' Initial test of the board class
file = open('in2', 'r')
board = Board()
#board.readFromFile(file)
#root = Node(board)
graph = Graph(Node(board.readFromFile(file)))
graph.buildGraph()
children = graph.getRoot().getChildren()
graph.root.children[1].printNode()
print(graph.root.children[1].getBoard().isFinal())
#'''
'''board1, board2 = Board(), Board()

conf1, conf2 = [1,2,3,0,4,5,6,7,8], [1,2,3,4,0,5,6,7,8]

board1.setConf(conf1)
board2.setConf(conf2)

print(board1.getConf())
print(board2.getConf())

print(board1.sameBoard(board2))'''
