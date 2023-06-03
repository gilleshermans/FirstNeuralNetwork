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
    def neuralNetwork(self, layerSizes : list):
        for i in range(len(layerSizes)-1):
            layer = Layer()
            layer.layer(layerSizes[i], layerSizes[i+1])
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


    def applyAllGradients(self, learnRate):
        for layer in self.layers:
            layer.applyGradients(learnRate)

    # Caluclates the outputs by feeding the inputs through the entire network
    def calculateOuputs(self, inputs : list):
        for layer in self.layers:
            inputs = layer.calculateOutputs(inputs)
            
        return inputs

    # Find the highest input using the function above
    def Classify(self, inputs):
        outputs = self.calculateOutputs(inputs)
        return IndexOfMaxValue(outputs)

    def loss_for_one(self, dataPoint):
        outputs = self.calculateOuputs(dataPoint.input)
        outputLayer = self.layers[-1]
        cost = 0

        for node in range(len(outputs)):
            cost += outputLayer.nodeCost(outputs[node], dataPoint.expectedOutput) # should be dataPoints.expectedOutputs[nodeout]
        
        return cost

    def loss(self, data):
        totalCost = 0
        for dataPoint in data:
            totalCost += self.loss_for_one(dataPoint)
        return totalCost / len(data) # Because we need an average
    
    
# Test program
if __name__ == "__main__":
    # Set up the network
    network = NeuralNetwork()
    network.neuralNetwork([2, 1, 1])

    # These are all of our inputs
    node1 = Node([0, 0], 0)
    node2 = Node([0, 1], 1)
    node3 = Node([1, 0], 1)
    node4 = Node([1, 1], 1)
    
    # We train on a depth of 50 (this means 50 iterations)
    loss = network.loss([node1, node2, node3, node4])
    while loss > 0.1:
        network.learn([node1, node2, node3, node4], 0.1)

        loss = network.loss([node1, node2, node3, node4])
        print(loss)

    
    saveData("OR_DataSet.txt", network.currentWeights, network.currentBiases)

    x = int(input())
    y = int(input())
    output = network.calculateOuputs([x, y])
    

    print("The output is:", output[0])