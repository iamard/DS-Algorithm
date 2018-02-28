def mergeArray(array, left, middle, right):
    sorted = [0] * (right - left + 1)

    cur = 0
    s1  = left
    s2  = middle + 1
    while (s1 <= middle) and (s2 <= right):
        if (array[s1] <= array[s2]):
            sorted[cur] = array[s1]
            s1 = s1 + 1
        else:
            sorted[cur] = array[s2]
            s2 = s2 + 1
        cur = cur + 1

    while s1 <= middle:
        sorted[cur] = array[s1]
        s1 = s1 + 1
        cur = cur + 1

    while s2 <= right:
        sorted[cur] = array[s2]
        s2 = s2 + 1
        cur = cur + 1

    for cur in range(left, right + 1):
        array[cur] = sorted[cur - left]

def mergeSort(array, left, right):
    if (left < right):
        middle = left + int((right - left) / 2)
        mergeSort(array, left, middle)
        mergeSort(array, middle + 1, right)
        mergeArray(array, left, middle, right)

if __name__ == "__main__":
    array = [ 12, 11, 13, 5, 6, 7 ]
    mergeSort(array, 0, len(array) - 1)
    print(array)