import numpy as np
import math


def convertRoadData():
    inputs = ()
    outputs = ()
    fin = open("rando-log-roads.txt", "r")
    for aline in fin:
        name,firstVertex,openSpots,chosenSpot= aline.strip().split("|")
        tmp = []
        tmpo = []
        for i in openSpots:
            tmp.append(int(i))
        inputs = inputs + (tmp,)
        tmpo.append(int(chosenSpot))
        outputs = outputs + (tmpo,)
    return inputs,outputs
class NeuralNetwork(object):
    def __init__(self,isize,osize):
         # X IS THE NUM OF INPUTS
         #seeding for random number generations
        self.inputSize = isize
        self.outputSize = osize
        self.hiddenSize = 3
        #weights
        #weights
        self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
        self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

    def forward(self, X):
        #forward propagation through our network
        self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
        o = self.sigmoid(self.z3) # final activation function
        return o 

    def sigmoid(self, s):
        # activation function 
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, X, y, o):
        # backward propgate through the network
        self.o_error = y - o # error in output
        self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

        self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

    def train (self, X, y):
        o = self.forward(X)
        self.backward(X, y, o)

#NN = NeuralNetwork()
#for i in range(1000):
    #print( "Input: \n" + str(X)) 
    #print( "Actual Output: \n" + str(y))
    #print( "Predicted Output: \n" + str(NN.forward(X)) )
    #print( "Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
    #print( "\n")
 #   NN.train(X,y)

#Q = np.array([0,0,1])
#print("Input: " + str(Q))
#print(str(NN.forward(Q)))
#result = int(round(NN.forward(Q)[0], 2) * 100)
#print("Predicted output: " + str(result))

   

def convertSettlementData():
    inputs = ()
    outputs = ()
    fin = open("rando-log-settlements.txt", "r")
    for aline in fin:
        name,firstHalf,move = aline.strip().split("|")
        tmp = []
        tmpo = []
        for i in firstHalf:
            tmp.append(int(i))
        inputs = inputs + (tmp,)
        tmpo.append(int(move))
        outputs = outputs + (tmpo,)
    return inputs,outputs


def chooseSettlement(board):
    inputs,outputs = convertSettlementData()
    X = np.array(inputs,  dtype=float)
    y = np.array(outputs, dtype=float)

    #normalize our units.
    X = X/np.amax(X, axis=0)
    y = y/100 #max choice we have is 3

    NN = NeuralNetwork(54,1)
    
    #NN = NeuralNetwork()
    for i in range(1000):
        NN.train(X,y)

    Q = np.array(board)

    print("Input: " + str(Q))
    print(str(NN.forward(Q)))
    result = int(round(NN.forward(Q)[0], 2) * 100)
    print("Predicted output: " + str(result))
    exit()
    return result

def chooseRoads(possibleSpots):
    inputs,outputs = convertRoadData()
    X = np.array(inputs,  dtype=float)
    y = np.array(outputs, dtype=float)

    #normalize our units.
    X = X/np.amax(X, axis=0)
    y = y/100 #max choice we have is 3

    NN = NeuralNetwork(3,1)
    
    for i in range(1000):
        NN.train(X,y)
    Q = np.array(possibleSpots)
    result = int(round(NN.forward(Q)[0], 2) * 100)
    return result
