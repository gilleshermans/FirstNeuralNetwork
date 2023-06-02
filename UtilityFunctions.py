import random
import math

def IndexOfMaxValue(values : list):
    sortedList = sorted(values)
    max = sortedList[-1]
    return values.index(max)

def InitializeRandomWeight(numIncoming):
    randomValue = random.uniform(-1.0, 1.0)
    return randomValue / math.sqrt(numIncoming)


if __name__ == "__main__":
    newList = [5, 2, 8, 9, 0]
    print(IndexOfMaxValue(newList))
