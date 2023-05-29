import numpy as np  
# Create the layer

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
        activations = []
        weightedInput = []
        for outcomingNode in range(self.numOutcoming):
            weightedInput = self.biases[outcomingNode]
            for incomingNode in range(self.numIncoming):
                weightedInput += inputs[incomingNode] * self.weights[incomingNode] ####

            activations.append(self.ActivationFunction(weightedInput, "stepped"))
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