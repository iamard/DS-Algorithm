#include <cstdio>
using namespace std;

int binarySearch(int array[], int left, int right, int target) {
    while(left <= right) {
        int middle = left + (right - left) / 2;
        if (array[middle] == target)
            return middle;
        else if (array[middle] < target)
            left = middle + 1;
        else
            right = middle - 1;
    }

    return -1;
}

int main(int argc, char **argv) {
    int array[] = { 2, 3, 4, 10, 40 };
    int length = sizeof(array) / sizeof(int);
    int target = 10;
    int result = binarySearch(array, 0, length - 1, target);
    printf("%d\n", result);

    return 0;
}