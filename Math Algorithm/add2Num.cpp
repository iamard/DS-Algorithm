/* The following questions is from the following book.
 * "Coding Interviews Questions, Analysis& Solutions" */

#include <cstdio>
using namespace std;

int add2Num(int num1, int num2) {
    int sum;
    int carry;
    do {
        sum   = num1 ^ num2;
        carry = (num1 & num2) << 1;
        num1  = sum;
        num2  = carry;
    } while(num2 != 0);

    return num1;
}

int main() {
    printf("199 + 199: %d %d\n", 199 + 199, add2Num(199, 199));
    printf("938 + 100: %d %d\n", 938 + 100, add2Num(938, 100));
    return 0;
}
