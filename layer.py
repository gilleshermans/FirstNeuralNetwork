from utilityFunctions import *
import numpy as np  
# Create the layer

class Layer:
    # Main Variabels
    numIncoming : int
    numOutcoming : int
    costGradientWeights = []
    costGradientBiases = []
    weights = []
    biases = []
    mode = ""

    # Creating the layer    
    def layer(self, numIncoming, numOutcoming, mode):    
        self.numIncoming = numIncoming
        self.numOutcoming = numOutcoming
        self.weights = []
        self.biases = []
        self.mode = mode

        # Generating a random value for each weight and dividing it by the square root of numImcoming
        for i in range(numIncoming * numOutcoming):
            weight = InitializeRandomWeight(numIncoming)
            self.weights.append(weight)

            self.costGradientWeights.append(0)

        for j in range(numOutcoming):
            bias = 0
            self.biases.append(bias)

            self.costGradientBiases.append(0)
        

    # Updating weights and biases (gradient descend)
    def applyGradients(self, learnRate):
        for nodeOut in range(self.numOutcoming):
            self.biases[nodeOut] -= self.costGradientBiases[nodeOut] * learnRate

        for node in range(self.numIncoming * self.numOutcoming):
            self.weights[node] -= self.costGradientWeights[node] * learnRate
            
    # Calculating the ouputs by looking at the corresponding inputs
    def calculateOutputs(self, inputs: list):
        self.activations = []
        self.inputs = inputs

        for outcomingNode in range(self.numOutcoming):
            self.weightedInput = self.biases[outcomingNode]
            for incomingNode in range(self.numIncoming):
                self.weightedInput += self.inputs[incomingNode] * self.weights[incomingNode]
                
            self.activations.append(self.activation(self.weightedInput, self.mode))

        return self.activations
    
    def activation(self, value, mode):
        if mode == "stepped":
            if value > 0:
                return 1
            else:
                return 0
            
        elif mode == "sigmoid":
            return 1/(1+np.exp(-value))
        
        elif mode == "relu":
            if value >= 0:
                return value
            
            return 0.0
        
    def calculateOutputLayerNodeValues(self, expectedOutputs):
        self.nodeValues = []
        for i in range(len(expectedOutputs)):
            costDerivative = self.nodeCostDerivative(self.activations[i], expectedOutputs[i])
            activationDerivative = self.activationDerivative(self.activations[i], self.mode) ###########
            self.nodeValues.append(activationDerivative * costDerivative)

        return self.nodeValues
    
    def calculateHiddenLayerNodeValues(self, oldLayer, oldNodeValues):
        newNodeValues = []
        for newNodeIndex in range(len(self.numOutcoming)):
            newNodeValue = 0
            for oldNodeIndex in range(len(oldNodeValues)):
                weightedInputDerivative = oldLayer.weights[oldNodeIndex + newNodeIndex]
                newNodeValue += weightedInputDerivative * oldNodeValues[oldNodeIndex]
            newNodeValue *= self.activationDerivative(self.weightedInputs[newNodeIndex], self.mode)
            newNodeValues.append(newNodeValue)

        return newNodeValues

    def updateGradients(self, nodeValues):
        for nodeIn in range(self.numIncoming):
            for nodeOut in range(self.numOutcoming):
                derivativeCostToWeight = self.inputs[nodeIn] * self.nodeValues[nodeOut]
                self.costGradientWeights[nodeIn] += derivativeCostToWeight 
                self.costGradientWeights[nodeIn + nodeOut - 1] += derivativeCostToWeight 
        
            derivativeCostToBias = nodeValues[nodeOut]
            self.costGradientBiases[nodeOut] += derivativeCostToBias

    def activationDerivative(self, value, mode):
        if mode == "sigmoid":
            activation = self.activation(value, "sigmoid")
            return activation * (1 - activation)
        if mode == "relu":
            if value < 0:
                return 0
            else:
                return 1


    def nodeCost(self, activation, expectedOutput):
        error = activation - expectedOutput
        return error * error
    
    def nodeCostDerivative(self, activation, expectedOutput):
        return 2 * (activation - expectedOutput)