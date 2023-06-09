import numpy as np
from random import random
from utilityFunctions import *
from layer import *
from node import *

# Create the network itself
class NeuralNetwork:
    layers = []
    currentWeights = []
    currentBiases = []

    # Sets up the network
    def neuralNetwork(self, layerSizes : list, mode):
        for i in range(len(layerSizes)-1):
            layer = Layer()
            layer.layer(layerSizes[i], layerSizes[i+1], mode)
            self.layers.append(layer)

    def learn(self, trainigData, learnRate):
        h = 0.0001
        originalCost = self.loss(trainigData)

        # For each layer in the network...
        for layer in self.layers:
            
            # Updating the weights
            for node in range(layer.numIncoming * layer.numOutcoming):
                layer.weights[node] += h
                deltaCost = self.loss(trainigData) - originalCost
                layer.weights[node] -= h
                layer.costGradientWeights[node] = deltaCost / h

                self.currentWeights = layer.weights

            # Updating the biases
            for biasIndex in range(len(layer.biases)):
                layer.biases[biasIndex] += h
                deltaCost = self.loss(trainigData) - originalCost
                layer.biases[biasIndex] -= h
                layer.costGradientBiases[biasIndex] = deltaCost / h

                self.currentBiases = layer.biases

        self.applyAllGradients(learnRate)

    def learnWithBackPropagation(self, trainingBatch, learnRate):
        for dataPoint in trainingBatch:
            self.updateAllGradients(dataPoint)
        
        self.applyAllGradients(learnRate / len(trainingBatch))
        self.clearAllGradients()
        
    def applyAllGradients(self, learnRate):
        for layer in self.layers:
            layer.applyGradients(learnRate)

    def clearAllGradients(self):
        for layer in self.layers:
            for x in range(len(layer.costGradientWeights)):
                layer.costGradientWeights[x] = 0
            for y in range(len(layer.costGradientBiases)):
                layer.costGradientBiases[y] = 0


    # FASTER GD
    def updateAllGradients(self, dataPoint):
        self.calculateOuputs(dataPoint.input)

        outputLayer = self.layers[len(self.layers) - 1]
        nodeValues = outputLayer.calculateOutputLayerNodeValues(dataPoint.expectedOutput)
        outputLayer.updateGradients(nodeValues)

        for hiddenLayerIndex in range(len(self.layers) - 2):
            hiddenLayer = self.layers[len(self.layers) - 2]
            nodeValues = hiddenLayer.calculateHiddenLayerNodeValues(self.layers[hiddenLayerIndex + 1], nodeValues)
            hiddenLayer.updateGradients(nodeValues)

    # Caluclates the outputs by feeding the inputs through the entire network
    def calculateOuputs(self, inputs : list):
        for layer in self.layers:
            inputs = layer.calculateOutputs(inputs)
            
        return inputs

    # Find the highest input using the function above
    def classify(self, inputs):
        outputs = self.calculateOutputs(inputs)
        return IndexOfMaxValue(outputs)

    def loss_for_one(self, dataPoint):
        outputs = self.calculateOuputs(dataPoint.input)
        outputLayer = self.layers[-1]
        cost = 0

        for node in range(len(outputs)):
            cost += outputLayer.nodeCost(outputs[node], dataPoint.expectedOutput[node])
        
        return cost

    def loss(self, data):
        totalCost = 0
        for dataPoint in data:
            totalCost += self.loss_for_one(dataPoint)
        return totalCost / len(data) # Because we need an average
    
    def get_model(self):
        weights = []
        biases = []
        for layer in self.layers:
            weights.append(layer.weights)
            biases.append(layer.biases)
        return weights, biases
    
    
# Test program
if __name__ == "__main__":
    # Set up the network
    network = NeuralNetwork()
    network.neuralNetwork([2, 2, 1], "relu")

    # These are all of our inputs
    node1 = Node([0, 0], [0])
    node2 = Node([0, 1], [1])
    node3 = Node([1, 0], [1])
    node4 = Node([1, 1], [0])
    
    # We train on a depth of 50 (this means 50 iterations)
    loss = network.loss([node1, node2, node3, node4])
    while loss > 0.05:
        network.learnWithBackPropagation([node1, node2, node3, node4], 0.1)

        loss = network.loss([node1, node2, node3, node4])
        print(loss)

    weights, biases = network.get_model()
    print("weights:" + str(weights))
    print("biases:" + str(biases))

    saveData("OR_DataSet.txt", weights, biases)

    x = int(input())
    y = int(input())
    output = network.calculateOuputs([x, y])
    print("The output is:", output[0])