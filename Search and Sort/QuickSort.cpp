#include <cstdio>
#include <algorithm>
using namespace std;

int partition(int array[], int left, int right) {
    int index = left - 1;
    int pivot = array[right];

    for (int curPos = left; curPos < right; curPos++) {
        if (array[curPos] <= pivot) {
            index = index + 1;
            swap(array[curPos], array[index]);
        }
    }
    swap(array[index + 1], array[right]);
    return index + 1;
}

void quickSort(int array[], int left, int right) {
    if (left < right) {
        int curPos = partition(array, left, right);
        quickSort(array, left, curPos - 1);
        quickSort(array, curPos + 1, right);
    }
}

int printArray(int array[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
}

int main(int argc, char **argv) {
    int array[] = { 10, 7, 8, 9, 1, 5 };
    int length = sizeof(array) / sizeof(int);

    quickSort(array, 0, length - 1);
    printArray(array, length);
}
