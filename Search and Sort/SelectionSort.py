def selectionSort(array):
    for i in range(len(array)):
        candidate = i
        for j in range(i + 1, len(array)):
            if (array[candidate] > array[j]):
                candidate = j
        array[i], array[candidate] = array[candidate], array[i]

if __name__ == "__main__":
    array = [ 64, 25, 12, 22, 11 ]
    selectionSort(array)
    print(array)
