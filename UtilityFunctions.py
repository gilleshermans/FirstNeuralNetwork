def IndexOfMaxValue(values : list):
    sortedList = sorted(values)
    max = sortedList[-1]
    return values.index(max)


if __name__ == "__main__":
    newList = [5, 2, 8, 9, 0]
    print(IndexOfMaxValue(newList))
