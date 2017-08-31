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

int sub2Num(int num1, int num2) {
    num2 = add2Num(~num2, 1);
    return add2Num(num1, num2);
}

int main() {
    printf("199 - 108: %d %d\n", 199 - 108, sub2Num(199, 108));
    printf("938 - 167: %d %d\n", 938 - 167, sub2Num(938, 167));
    return 0;
}