#include <cstdio>
#include <algorithm>
using namespace std;

int selectionSort(int array[], int length) {
    for (int i = 0; i < length; i++) {
        int candidate = i;
        for (int j = i + 1; j < length; j++) {
            if (array[candidate] > array[j])
                candidate = j;
        }
        swap(array[i], array[candidate]);
    }
}

int printArray(int array[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
}

int main(int argc, char **argv) {
    int array[] = { 64, 25, 12, 22, 11 };
    int length = sizeof(array) / sizeof(int);

    selectionSort(array, length);

    printArray(array, length);

    return 0;
}