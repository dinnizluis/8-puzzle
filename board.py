class Board:
    #Constructor
    #Sobrescrever construtor para também receber parâmetro
    def __init__(self):
        self.conf = []
        self.status = 'not_final'

    #Setters
    def setConf(self, list):
        self.conf = list.copy()

    def setStatus(self, str):
        self.status = str

    #Getters
    def getConf(self):
        return self.conf

    def getStatus(self):
        return self.status

    def copy(self):
        return self


    #Read a board configuration from a file object (the content of the object is expected to be in a specific format),
    #set the board configuration to it,
    #and @returns the configuration
    def readFromFile(self, file):
        #Get only the string with the configuration
        for row in file:
            bd = row
        conf = bd.split(',')
        temp = conf[8].split(' ')
        temp = temp[0].split('\n')
        conf[8] = temp[0]

        #Convert the list of char to int
        for i in range(len(conf)):
            conf[i] = int(conf[i])
        self.conf = conf
        return conf

    #Finds the 0 on the list
    #and @returns the index of 0
    def findZero(self):
        for i in range(len(self.conf)):
            if(self.conf[i] == 0):
                return i
        return -1

    #Checks if the current configuration is final Statement
    #and @returns True if it is and False if it isn't
    def isFinal(self):
        for i in range(1, 9):
            if self.conf[i-1] > self.conf[i]:
                return False
        self.status = 'final'
        return True

    #Checks if the given board has the same consiguration as the object
    #and @returns a boolean value
    def sameBoard(self, board):
        if len(board.getConf()) != len(self.conf):
            return False
        else:
            for i in range(len(self.conf)):
                if board.getConf()[i] != self.getConf()[i]:
                    return False
        return True
