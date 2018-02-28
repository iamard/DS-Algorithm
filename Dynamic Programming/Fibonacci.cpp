#include <cstdio>
#include <cstring>
using namespace std;

int lookpup[100] = { -1 };

int fibTopDown(int n) {
    if (lookpup[n] == -1) {
        if (n <= 1)
            lookpup[n] = n;
        else
            lookpup[n] = fibTopDown(n - 1) + fibTopDown(n - 2);
    }

    return lookpup[n];    
}

int fibBottomUp(int n) {
    int table[n + 1];
    table[0] = 0;
    table[1] = 1;
    for (int index = 2; index <= n; index++) {
        table[index] = table[index - 1] + table[index - 2];
    }
    return table[n];
}

int main(int argc, char **argv) {
    memset(lookpup, 0xFF, sizeof(lookpup));

    printf("Fibonacci 40th: %d by top down\n", fibTopDown(40));
    printf("Fibonacci 40th: %d by bottom up\n", fibBottomUp(40));
    return 0;
}