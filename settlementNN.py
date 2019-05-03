import numpy as np
import math


def convertRoadData():
    '''
    Returns 2 lists:
        Inputs: Binary array of roads owned
        Outputs: Roads chosen
    '''
    inputs = ()
    outputs = ()
    fin = open("logging/rando-log-roads.txt", "r")
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
    '''
    Based on this article: https://dev.to/shamdasani/build-a-flexible-neural-network-with-backpropagation-in-pythons
    '''
    def __init__(self,isize,osize):
         # X IS THE NUM OF INPUTS
         #seeding for random number generations
        self.inputSize = isize
        self.outputSize = osize
        self.hiddenSize = 3
        #weights
        #weights
        self.weight_set_1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
        self.weight_set_2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

    def forward(self, X):
        #forward propagation through our network
        self.z = np.dot(X, self.weight_set_1) # dot product of X (input) and first set of 3x2 weights
        self.z2 = self.sigmoid(self.z) # activation function
        self.z3 = np.dot(self.z2, self.weight_set_2) # dot product of hidden layer (z2) and second set of 3x1 weights
        output = self.sigmoid(self.z3) # final activation function
        return output 

    def sigmoid(self, s):
        # activation function 
        return 1/(1+np.exp(-s))

    def sigmoidPrime(self, s):
        #derivative of sigmoid
        return s * (1 - s)

    def backward(self, inputs, outputs, output):
        # backward propgate through the network
        self.output_error = outputs - output # error in output
        self.output_delta = self.output_error*self.sigmoidPrime(output) # applying derivative of sigmoid to error

        self.z2_error = self.output_delta.dot(self.weight_set_2.T) # z2 error: how much our hidden layer weights contributed to output error
        self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

        self.weight_set_1 += inputs.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
        self.weight_set_2 += self.z2.T.dot(self.output_delta) # adjusting second set (hidden --> output) weights

    def train (self, inputs, outputs):
        output = self.forward(inputs)
        self.backward(inputs, outputs, output) 

def convertSettlementData():
    '''
    Returns 2 lists:
        Inputs:  binary tuple of settlements owned. 
        Outputs: tuples of the settlements chosen
    '''
    inputs = ()
    outputs = ()
    fin = open("logging/rando-log-settlements.txt", "r")
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
    inputs = np.array(inputs,  dtype=float)
    outputs = np.array(outputs, dtype=float)

    #normalize our units.
    inputs  = inputs/np.amax(inputs)
    outputs = outputs/100 #mainputs choice we have is 3

    NN = NeuralNetwork(54,1)

    for i in range(1000):
        NN.train(inputs,outputs)

    Q = np.array(board)

    #print("Input: " + str(Q))
    #print(str(NN.forward(Q)))
    result = int(round(NN.forward(Q)[0], 2) * 100)
    #print("Predicted output: " + str(result))
    return result

def chooseRoads(possibleSpots):
    '''
    The 3 digit binary array is processed by the neural network and returns either a 1,2, or 3.
    '''
    inputs,outputs = convertRoadData()
    inputs  = np.array(inputs,  dtype=float)
    outputs = np.array(outputs, dtype=float)

    #normalize our units.
    inputs  = inputs/np.amax(inputs, axis=0)
    outputs = outputs/100 #max choice we have is 3

    NN = NeuralNetwork(3,1)
    
    for i in range(1000):
        NN.train(inputs,outputs)

    Q = np.array(possibleSpots)
    result = int(round(NN.forward(Q)[0], 2) * 100)
    return result
