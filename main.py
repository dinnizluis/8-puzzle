from graph import *

#''' Initial test of the board class
file = open('in1', 'r')
board = Board()
board.readFromFile(file)
root = Node(board)
graph = Graph(root)
graph.buildGraph()
children = graph.getRoot().getChildren()
print(graph.root.children[1])
#'''
