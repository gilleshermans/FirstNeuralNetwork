import numpy as np
from random import random
from utilityFunctions import *
from layer import *
from node import *

# Create the network itself
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
    
    def loss_for_one(self, dataPoint):
        outputs = self.calculateOuputs(dataPoint.input)
        outputLayer = self.layers[-1]
        cost = 0

        for node in range(len(outputs)):
            cost += outputLayer.nodeCost(outputs[node], dataPoint.expectedOutput) # expectedOutput should be dataPoints.expectedOutput[nodeout]
        
        return cost

    def loss(self, data):
        totalCost = 0
        for dataPoint in data:
            totalCost += self.loss_for_one(dataPoint)
        return totalCost / len(data) # Because we need an average
    

    
# Test program
# I know that this code is very badly coded
# but it's just a test, please forgive me :)

if __name__ == "__main__":
    # Set up the network
    network = NeuralNetwork()
    network.NeuralNetwork([2, 1])

    # These are all of our inputs
    node1 = Node([0, 0], 0)
    node2 = Node([0, 1], 1)
    node3 = Node([1, 0], 1)
    node4 = Node([1, 1], 1)
    
    # We train on a depth of 50 (this means 50 iterations)
    for i in range(1):
        # Calculate current ouput
        output = network.calculateOuputs(node1.input)

        error = 0 - output[0]
        network.layers[0].weights[0] += error * 0
        network.layers[0].weights[1] += error * 0

        output = network.calculateOuputs(node2.input)

        error = 1 - output[0]
        network.layers[0].weights[0] += error * 0
        network.layers[0].weights[1] += error * 1
        
        output = network.calculateOuputs(node3.input)

        error = 1 - output[0]
        network.layers[0].weights[0] += error * 1
        network.layers[0].weights[1] += error * 0

        output = network.calculateOuputs(node4.input)

        error = 1 - output[0]
        network.layers[0].weights[0] += error * 1
        network.layers[0].weights[1] += error * 1

        loss = network.loss([node1, node2, node3, node4])
        print(loss)

    x = int(input())
    y = int(input())
    output = network.calculateOuputs([x, y])

    print("The output is:", output)