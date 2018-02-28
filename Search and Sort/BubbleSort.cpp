#include <cstdio>
#include <algorithm>
using namespace std;

void bubbleSort(int array[], int length) {
    for (int i = 0; i < length; i++) {
        for (int j = 0; j < length - i - 1; j++) {
            if (array[j] > array[j + 1])
                swap(array[j], array[j + 1]);
        }
    }
}

int printArray(int array[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
}

int main(int argc, char **argv) {
    int array[] = { 64, 34, 25, 12, 22, 11, 90 };
    int length = sizeof(array)/sizeof(int);

    bubbleSort(array, length);
    printArray(array, length);

    return 0;
}