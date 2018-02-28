#include <cstdio>
#include <cstring>
using namespace std;

void mergeArray(int array[], int left, int middle, int right) {
    int sorted[right - left + 1];

    int cur = 0;
    int s1  = left;
    int s2  = middle + 1;
    while(s1 <= middle && s2 <= right) {
        if (array[s1] <= array[s2]) {
            sorted[cur++] = array[s1++];
        } else {
            sorted[cur++] = array[s2++];
        }
    }

    while(s1 <= middle) {
        sorted[cur++] = array[s1++];
    }

    while(s2 <= right) {
        sorted[cur++] = array[s2++];
    }

    memcpy(&array[left], sorted, sizeof(int) * (right - left + 1));
}

void mergeSort(int array[], int left, int right) {
    if (left < right) {
        int middle = left + (right - left) / 2;
        mergeSort(array, left, middle);
        mergeSort(array, middle + 1, right);
        mergeArray(array, left, middle, right);
    }
}

int printArray(int array[], int length) {
    for (int i = 0; i < length; i++) {
        printf("%d ", array[i]);
    }
}

int main(int argc, char **argv) {
    int array[] = { 12, 11, 13, 5, 6, 7 };
    int length = sizeof(array) / sizeof(int);
    mergeSort(array, 0, length - 1);
    printArray(array, length);
}
