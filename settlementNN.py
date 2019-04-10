import numpy as np

class NeuralNetwork():
    def __init__(self,x):
        # X IS THE NUM OF INPUTS
        #seeding for random number generations
        np.random.seed(1)
        #converting weights to a 114 by 1 matrix with values from -1 to 1 and mean of 0
        self.synaptic_weights = 2 * np.random.random((x,1)) - 1

    def sigmoid(self,x):
        #applying sigmoid function
        return 1/ (1 + np.exp(-x))
    def sigmoid_derivative(self,x):
        return x * (1 - x)
    def train(self, training_inputs, training_outputs, training_iterations):
        #trains the model to make accurate preidictions while always adjusting weights
        for iteration in range(training_iterations):
            #siphon the training data via the neuron
            output = self.think(training_inputs)

            #computing error rate for back-propogation
            error = training_outputs - output

            #performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))

            self.synaptic_weights += adjustments
    def think(self, inputs):
        #passing the inputs via neuron to get Outputs
        #converting values to floats
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output


def convertSettlementsData():
    inputs = []
    outputs = [[]]
    fin = open("log-settlements.txt", "r")
    for aline in fin:
        firstHalf,move = aline.strip().split("|")
        tmp = []
        for i in firstHalf:
            tmp.append(int(i))
        inputs.append(tmp)
        num = round(int(move)/55,4) #because i want to keep this within 1, i divide by 55 possible moves.
        outputs[0].append(num)
    return inputs,outputs
    #initializes the neuron class

def chooseSettlement(board):
    neural_network = NeuralNetwork(114)

    #print("Beginning Randomly Generated Weights: ")
    #print(neural_network.synaptic_weights)

    #THIS TRAINING DATA IS FROM log-settlements.txt
    inputs,outputs = convertSettlementsData()
    training_inputs = np.array(inputs)
    training_outputs = np.array(outputs).T

    #training taking place
    neural_network.train(training_inputs, training_outputs, 15000)

    #print("Ending weights after training: ")
    #print(neural_network.synaptic_weights)

    #print("CONSIDER NEW SITUATION")
    tmp = list(map(str,board))
    theMove = neural_network.think(np.array(tmp))
    theMove = int(theMove * 55)

    #print("The neural network says you should do", theMove)
    return theMove
