from anytree import *
import time, timeit, sys

class Board(NodeMixin): #Add the node feature

	def __init__(self, conf, parent=None):
		self.conf = conf
		if conf == sorted(conf) and len(conf) != 0:
			self.status = "final"
		else:
			self.status = "not_final"
		self.parent= parent

	#Mostra toda a árvore de busca construída.
	def printTree(self):
		for pre, _, node in RenderTree(self):
			treestr = u"%s%s" % (pre, node.conf)
			print(treestr.ljust(8), node.status)

	#Mostra tabuleiro atual.
	def printBoard(self):
		print("{} is the configuration.".format(self.conf))
		print("{} is the status.".format(self.status))

	#Cria uma nova referência e copia os dados do board.
	def copyBoard(self):
		board = Board(self.conf.copy())
		return board

	#Troca dois elementos nas posições a e b (um com o outro).
	def swap(self, a, b):
		lst = self.conf.copy()
		lst[a], lst[b] = lst[b], lst[a]
		return lst

	#Retorna em qual posição o 0 (vazio) está.
	def findZero(self):
		for i in range(len(self.conf)):
			if self.conf[i] == 0:
				return i
		return -1

	#Retorna se o board é final.
	def boardIsFinal(self):
		return self.status == "final"

	#Calcula o valor heurístico para o tabuleiro.
	def heuristic_value(self):
		h = 0
		for i in self.conf:
			h = h + self.manhattanDistance(self.conf[i], i)
		return h

	#Método capaz de calcular a distância de Manhattan de elem que está na posição pos.
	#Retorna o valor absoluto da distância.
	def manhattanDistance(self, elem, pos):
		if pos>=0 and pos<=2:
			cord = (0, pos)
		elif pos>=3 and pos<=5:
			cord = (1, pos-3)
		elif pos>=5 and pos<=8:
			cord = (2, pos-6)
		else:
			return -1 #Invalid position

		if elem == 0:
			return cord[0]+cord[1]
		elif elem == 1:
			return abs(cord[0]-0) + abs(cord[1]-1)
		elif elem == 2:
			return abs(cord[0]-0) + abs(cord[1]-2)
		elif elem == 3:
			return abs(cord[0]-1) + abs(cord[1]-0)
		elif elem == 4:
			return abs(cord[0]-1) + abs(cord[1]-1)
		elif elem == 5:
			return abs(cord[0]-1) + abs(cord[1]-2)
		elif elem == 6:
			return abs(cord[0]-2) + abs(cord[1]-0)
		elif elem == 7:
			return abs(cord[0]-2) + abs(cord[1]-1)
		elif elem == 8:
			return abs(cord[0]-2) + abs(cord[1]-2)

	#Método capaz de realizar os movimentos do jogo. De acordo com a posição do quadro vazio os novos estados são gerados na ordem CBDE.
	def haveChild(self):
		zero = self.findZero()
		if zero == 1:
			up = self.swap(zero, zero+3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:#Verifica se node já existe na árvore
					count +=1
			if count == 0:#Se não existir realiza movimento (up)
				node_up = Board(up, parent=self)

			left = self.swap(zero, zero-1)#LEFT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero+1)#RIGHT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 3:
			up = self.swap(zero, zero-3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:
					count +=1
			if count == 0:
				node_up = Board(up, parent=self)

			down = self.swap(zero, zero+3)#DOWN
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == down)) != 0:
					count +=1
			if count == 0:
				node_down = Board(down, parent=self)

			left = self.swap(zero, zero+1)#LEFT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1
			if count == 0:
				node_left = Board(left, parent=self)

		elif zero == 5:
			up = self.swap(zero, zero-3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:
					count +=1
			if count == 0:
				node_up = Board(up, parent=self)

			down = self.swap(zero, zero+3)#DOWN
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == down)) != 0:
					count +=1
			if count == 0:
				node_down = Board(down, parent=self)

			right = self.swap(zero, zero-1)#RIGHT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 7:
			left = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1
			if count == 0:
				node_left = Board(left, parent=self)

			mid = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid)) != 0:
					count +=1
			if count == 0:
				node_mid = Board(mid, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 0:
			up = self.swap(zero, zero+3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:
					count +=1
			if count == 0:
				node_up = Board(up, parent=self)

			left = self.swap(zero, zero+1)#LEFT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1
			if count == 0:
				node_left = Board(left, parent=self)

		elif zero == 2:
			up = self.swap(zero, zero+3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:
					count +=1
			if count == 0:
				node_up = Board(up, parent=self)

			right = self.swap(zero, zero-1)#RIGHT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 6:
			down = self.swap(zero, zero-3)#DOWN
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == down)) != 0:
					count +=1
			if count == 0:
				node_down = Board(down, parent=self)

			right = self.swap(zero, zero+1)#RIGHT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 8:
			down = self.swap(zero, zero-3)#DOWN
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == down)) != 0:
					count +=1
			if count == 0:
				node_down = Board(down, parent=self)

			left = self.swap(zero, zero-1)#LEFT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1
			if count == 0:
				node_left = Board(left, parent=self)

		elif zero == 4:
			up = self.swap(zero, zero-3)#UP
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == up)) != 0:
					count += 1
			if count == 0:
				node_up = Board(up, parent=self)

			down = self.swap(zero, zero+3)#DOWN
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == down)) != 0:
					count += 1
			if count == 0:
				node_down = Board(down, parent=self)

			left = self.swap(zero, zero-1)#LEFT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count += 1
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero+1)#RIGHT
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count += 1
			if count == 0:
				node_right = Board(right, parent=self)

		else:
			return False
	
	#Método capaz de encontrar caminho mínimo do board no parâmetro até um estado final,
	#retorna o custo mínimo e quantidade de nós analisados.
	def findMinCost(self):
		if self.boardIsFinal():
			return 0
		else:
			q = []
			r = (self.heuristic_value(), self)
			q.append(r)
			nodes = 0
			while len(q) != 0:
				u = min(q, key=lambda q: q[0])
				q.remove(u)
				u[1].haveChild()
				for i in range(len(u[1].children)):
					nodes +=1
					if u[1].children[i].boardIsFinal():
						return len(u[1].ancestors)+1, nodes
					else:
						g = len(u[1].ancestors)+1
						h = u[1].children[i].heuristic_value()
						q.append( (h+g, u[1].children[i]) )

#Método capaz de ler um arquivo com a configuração de um tabuleiro e retorná-lo como uma lista.
def readFromFile(name):
	file = open(name, 'r')
	for row in file:
		bd = row
		conf = bd.split(',')
		temp = conf[8].split(' ')
		temp = temp[0].split('\n')
		conf[8] = temp[0]
	return [int(i) for i in conf]

#Método para executar os 9 exemplos disponíveis em uma única execução.
def run(a, b):
	file = open("results.txt", "w")
	file.close()
	for i in range(a, b+1):
		board = Board(readFromFile('testes/in'+str(i)))
		begin = time.time()
		rslt = board.findMinCost()
		end = time.time()
		tempo = end - begin
		file0 = open("results.txt", "a")
		file1 = open("out"+str(i), "w")
		file0.write("custo_total: {0}, nós examinados: {1}, tempo: {2} segundos".format(rslt[0], rslt[1], str(tempo)))
		file0.write("\n")
		file1.write("custo_total: {0}".format(rslt[0]))
		file0.close()
		file1.close()
		print("------------------------------------------------------------------------------------")
		print("In"+str(i))
		print("custo_total: {0}, nós examinados: {1}, tempo: {2} segundos".format(rslt[0], rslt[1], str(tempo)))

#lib para calcular quantidade de memória alocada.
import tracemalloc
tracemalloc.start()

#run(1,9)
param = sys.argv[1:]
in1 = []
for i in range(len(param[0])):
	if param[0][i] >= '0' and param[0][i] <= '8':
		in1.append(int(param[0][i]))
board  = Board(in1)
c, n = board.findMinCost() 
sys.stdout.write("custo_total: "+str(c))
sys.exit(0)

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
#print('[Top 10]')
#for stat in top_stats[:10]:
#	print(stat)
