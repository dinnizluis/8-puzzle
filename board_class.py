from anytree import *

class Board(NodeMixin): #Add the node feature

	def __init__(self, conf, parent=None):
		self.conf = conf
		if conf == sorted(conf) and len(conf) != 0:
			self.status = "final"
		else:
			self.status = "not_final"
		self.parent= parent

	def printTree(self):
		for pre, _, node in RenderTree(self):
			treestr = u"%s%s" % (pre, node.conf)
			print(treestr.ljust(8), node.status)

	def printBoard(self):
		#print("{} is the configuration.".format(self.conf))
		#print("{} is the status.".format(self.status))
		print("configuration: ")
		print(self.conf)
		print("status: ")
		print(self.status)

	def copyBoard(self):
		board = Board(self.conf.copy())
		return board

	def swap(self, a, b):
		lst = self.conf.copy()
		lst[a], lst[b] = lst[b], lst[a]
		return lst

	def findZero(self):
		for i in range(len(self.conf)):
			if self.conf[i] == 0:
				return i
		return -1

	def boardIsFinal(self):
		return self.status == "final"

	def haveChild(self):
		zero = self.findZero()
		if zero == 1:
			left = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			mid = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(mid, parent=self)

			right = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(right, parent=self)

		elif zero == 3:
			left = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			mid = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(mid, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(right, parent=self)

		elif zero == 5:
			left = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			mid = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(mid, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(right, parent=self)
		
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
				node_left = Board(mid, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(right, parent=self)

		elif zero == 0:
			left = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(right, parent=self)

		elif zero == 2:
			left = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 6:
			left = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 8:
			left = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count +=1 
			if count == 0:
				node_left = Board(left, parent=self)

			right = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count +=1
			if count == 0:
				node_right = Board(right, parent=self)

		elif zero == 4:
			left = self.swap(zero, zero-1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == left)) != 0:
					count += 1
			if count == 0:
				node_left = Board(left, parent=self)

			mid1 = self.swap(zero, zero+1)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid1)) != 0:
					count += 1
			if count == 0:
				node_mid1 = Board(mid1, parent=self)

			mid2 = self.swap(zero, zero-3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == mid2)) != 0:
					count += 1
			if count == 0:
				node_mid2 = Board(mid2, parent=self)

			right = self.swap(zero, zero+3)
			count = 0
			for i in range(len(self.ancestors)):
				if len(findall(self.ancestors[i], filter_=lambda node: node.conf == right)) != 0:
					count += 1
			if count == 0:
				node_right = Board(right, parent=self)

		else:
			return False


	def findMinCost(self):
		if self.boardIsFinal():
			return 0
		else:
			q = []
			q.append(self)
			cost = 0
			while len(q) != 0:
				print(len(q))
				#wait = input('The tree is currently like this: ')
				#self.printTree()
				#print('\n')
				u = q.pop(0)
				u.haveChild()
				for i in range(len(u.children)):
					if u.children[i].boardIsFinal():
						return len(u.ancestors)+1
					else:
						q.append(u.children[i])


def readFromFile(name):
	file = open(name, 'r')
	for row in file:
		bd = row
		conf = bd.split(',')
		temp = conf[8].split(' ')
		temp = temp[0].split('\n')
		conf[8] = temp[0]
	return [int(i) for i in conf]

board0 = Board(readFromFile('in3'))
print("custo_total: {}".format(board0.findMinCost()))
board0.printTree()
