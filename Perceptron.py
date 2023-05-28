# My First Neural Network - The perceptron by Frans Rosenblatt
# invented in 1958! It's actually an inclusive or gate

import random

learning_rate = 1 # If you learn faster, you are likely to be more inaccurate - quote by me :D

weights = [random.random(), random.random(), random.random()]

def Perceptron(input1, input2, expectedOutput):
    currentOutput = (input1 * weights[0]) + (input2 * weights[1])

    # HeavySide ActivationFunction
    if currentOutput > 0:
        currentOutput = 1
    else:
        currentOutput = 0
    
    error = expectedOutput - currentOutput
    weights[0] += error * input1 * learning_rate
    weights[1] += error * input2 * learning_rate

# The network can train 50 times on our data
for i in range(50):
    Perceptron(1, 1, 1)
    Perceptron(1, 0, 1)
    Perceptron(0, 1, 1)
    Perceptron(0, 0, 0)

# Testing the algorithm
x = int(input())
y = int(input())
output = x*weights[0] + y*weights[1]

if output > 0:
    output = 1
else:
    output = 0

print("The output is:", output)