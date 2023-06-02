from utilityFunctions import *
import numpy as np  
# Create the layer

class Layer:
    # Main Variabels
    numIncoming : int
    numOutcoming : int
    costGradientWeights : list
    costGradientBiases : list
    weights = []
    biases = []

    # Creating the layer    
    def layer(self, numIncoming, numOutcoming):    
        self.numIncoming = numIncoming
        self.numOutcoming = numOutcoming
        self.weights = []
        self.biases = []

        # Generating a random value for each weight and dividing it by the square root of numImcoming
        for i in range(numIncoming * numOutcoming):
            weight = InitializeRandomWeight(numIncoming)
            self.weights.append(weight)

        for j in range(numOutcoming):
            bias = 0
            self.biases.append(bias)

    # Updating weights and biases (gradient descend)
    def applyGradients(self, learnRate):
        for nodeOut in range(len(self.numOutcoming)):
            self.biases[nodeOut] -= self.costGradientBiases[nodeOut] * learnRate

        for node in range(len(self.numIncoming) * len(self.numOutcoming)):
            self.weights[node] = self.costGradientWeights[node] * learnRate
            
    

    # Calculating the ouputs by looking at the corresponding inputs
    def calculateOutputs(self, inputs: list):
        activations = []
        weightedInput = []

        for outcomingNode in range(self.numOutcoming):
            weightedInput = self.biases[outcomingNode]
            for incomingNode in range(self.numIncoming):
                weightedInput += inputs[incomingNode] * self.weights[incomingNode]
                
            activations.append(self.ActivationFunction(weightedInput, "sigmoid"))
        return activations
    
    def ActivationFunction(self, value, mode):
        if mode == "stepped":
            if value > 0:
                return 1
            else:
                return 0
            
        elif mode == "sigmoid":
            return 1/(1+np.exp(-value))
        
        elif mode == "relu":
            return max(0.0, value)
    
    def nodeCost(self, activation, expectedOutput):
        error = activation - expectedOutput
        return error * error
    