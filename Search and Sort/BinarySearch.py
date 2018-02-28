def binarySearch(array, left, right, target):
    while(left <= right):
        middle = left + int((right - left) / 2)
        if (array[middle] == target):
            return middle
        elif (array[middle] < target):
            left = middle + 1
        else:
            right = middle - 1

    return -1;

if __name__ == "__main__":
    array  = [ 2, 3, 4, 10, 40 ]
    target = 10
    
    result = binarySearch(array, 0, len(array) - 1, target)
    print(result)
