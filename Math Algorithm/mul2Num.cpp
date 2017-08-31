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

int mul2Num(int num1, int num2) {
    bool minus = false;
    if ((num1 < 0 && num2 > 0) || (num1 > 0 && num2 < 0))
        minus = true;

    if (num1 < 0) {
        num1 = add2Num(~num1, 1);
    }
    if (num2 < 0) {
        num2 = add2Num(~num2, 1);
    }

    int result = 0;
    while(num1 > 0) {
        if (num1 & 0x1) {
            result = add2Num(result, num2);
        }
        num2 <<= 1;
        num1 >>= 1;
    }

    if (minus) {
        result = add2Num(~result, 1);
    }
    return result;
}


int main() {
    printf("-1 * 30: %3d %3d\n", -1 * 30, mul2Num(-1, 30));
    printf("-5 *  7: %3d %3d\n", -5 * -5, mul2Num(-5, -7));
    return 0;
}