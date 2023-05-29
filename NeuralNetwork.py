from random import random
from UtilityFunctions import *

class Layer:
    # Main Variabels
    numIncoming : int
    numOutcoming : int
    weights = []
    biases = []

    # Creating the layer    
    def layer(self, numIncoming, numOutcoming):    
        self.numIncoming = numIncoming
        self.numOutcoming = numOutcoming
        self.weights = []
        self.biases = []

        # I dont know what the values should be yet
        for i in range(numIncoming * numOutcoming):
            weight = 1
            self.weights.append(weight)
        for j in range(numOutcoming):
            bias = 0
            self.biases.append(bias)

    # Calculating the ouput
    def calculateOutputs(self, inputs: list):
        weightedInputs = []
        weightedInput = []
        for outcomingNode in range(self.numOutcoming):
            weightedInput = self.biases[outcomingNode]
            for incomingNode in range(self.numIncoming):
                weightedInput += inputs[incomingNode] * self.weights[incomingNode] ####

            weightedInputs.append(weightedInput)
        return weightedInputs

class NeuralNetwork:
    layers = []

    # Sets up the network
    def NeuralNetwork(self, layerSizes : list):
        for i in range(len(layerSizes)-1):
            layer = Layer()
            layer.layer(layerSizes[i], layerSizes[i+1])
            self.layers.append(layer)

    # Caluclates the outputs from the inputs
    def calculateOuputs(self, inputs : list):
        for layer in self.layers:
            inputs = layer.calculateOutputs(inputs)
            
        return inputs
    


    # Find the highest input using the function above
    def Classify(self, inputs):
        outputs = self.calculateOutputs(inputs)
        return IndexOfMaxValue(outputs)

    
# Test program
# I know that this code is very badly coded
# but it's just a test, please forgive me :)

if __name__ == "__main__":
    # Set up the network
    network = NeuralNetwork()
    network.NeuralNetwork([2, 1])

    for i in range(50):
        # Calculate current ouput
        output = network.calculateOuputs([0, 0])
        if output[0] > 0:
            output = 1
        else:
            output = 0
        error = 0 - output
        network.layers[0].weights[0] += error * 0
        network.layers[0].weights[1] += error * 0

        output = network.calculateOuputs([0, 1])
        if output[0] > 0:
            output = 1
        else:
            output = 0
        error = 1 - output
        network.layers[0].weights[0] += error * 0
        network.layers[0].weights[1] += error * 1
        output = network.calculateOuputs([1, 0])
        if output[0] > 0:
            output = 1
        else:
            output = 0
        error = 1 - output
        network.layers[0].weights[0] += error * 1
        network.layers[0].weights[1] += error * 0

        output = network.calculateOuputs([1, 1])
        if output[0] > 0:
            output = 1
        else:
            output = 0
        error = 1 - output
        network.layers[0].weights[0] += error * 1
        network.layers[0].weights[1] += error * 1

    x = int(input())
    y = int(input())
    output = network.calculateOuputs([x, y])

    if output[0] > 0:
        output = 1
    else:
        output = 0

    print("The output is:", output)