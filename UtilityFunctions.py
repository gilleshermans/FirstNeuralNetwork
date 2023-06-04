import random
import math

def IndexOfMaxValue(values : list):
    sortedList = sorted(values)
    max = sortedList[-1]
    return values.index(max)

def InitializeRandomWeight(numIncoming, numOutcoming):
    randomValue = random.uniform(numIncoming, numOutcoming)
    return randomValue * math.sqrt(2/(numIncoming + numOutcoming))

def saveData(file : str, weights, biases):
    f = open(file, 'w')
    f.write(str(weights))
    f.write("\n")
    f.write(str(biases))
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
