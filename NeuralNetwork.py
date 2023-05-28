from random import random

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
    layers : list

    # Sets up the network
    def NeuralNetwork(layerSizes : list):
        pass

    # Caluclates the outputs from the inputs
    def CalculateOuputs(inputs : list):
        pass

    # Find the highest input using the function above
    def Classify(inputs):
        pass

    
# Test program
if __name__ == "__main__":
    network = Layer()
    network.layer(2, 3)
    print(network.calculateOutputs([1, 2]))
     