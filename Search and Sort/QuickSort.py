def partition(array, low, high):
    index = low - 1
    pivot = array[high]

    for curPos in range(low, high):
        if (array[curPos] <= pivot):
            index = index + 1
            array[index], array[curPos] = array[curPos], array[index]
    array[index + 1], array[high] = array[high], array[index + 1]
    return index + 1

def quickSort(array, low, high):
    if (low < high):
        curPos = partition(array, low ,high)
        quickSort(array, low, curPos - 1)
        quickSort(array, curPos + 1, high)

if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5]
    quickSort(array, 0, len(array) - 1)
    print(array)
