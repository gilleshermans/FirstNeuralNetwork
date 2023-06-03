import random
import math

def IndexOfMaxValue(values : list):
    sortedList = sorted(values)
    max = sortedList[-1]
    return values.index(max)

def InitializeRandomWeight(numIncoming):
    randomValue = random.uniform(-1.0, 1.0)
    return randomValue / math.sqrt(numIncoming)

def saveData(file : str, weights, biases):
    f = open(file, 'w')
    for weight in weights:
        f.write(str(weight) + "\n")
    for bias in biases:
        f.write(str(bias) + "\n")
    f.close()

def getData(file : str):
    f = open(file)
    lines = f.readlines()
    data = []
    for line in lines:
        for char in line:
            if char == "\n":
                line.replace(char, "")
        line = float(line)
        data.append(line)
    print(data)
    


if __name__ == "__main__":
    getData("OR_DataSet.txt")
