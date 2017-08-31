/* The following questions is from the following book.
 * "Coding Interviews Questions, Analysis& Solutions" */

#include <stdexcept>
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

int div2Num(int num1, int num2) {
    if (num2 == 0)
        throw invalid_argument("num2 is zero!\n");

    bool minus = false;
    if ((num1 < 0 && num2 > 0) || (num1 > 0 && num2 < 0)) {
        minus = true;
    }
    if (num1 < 0)
        num1 = add2Num(~num1, 1);
    if (num2 < 0)
        num2 = add2Num(~num2, 1);

    int result = 0;
    for (int i = 0; i < 32; i++) {
        result <<= 1;
        if ((num1 >> (31 - i)) >= num2) {
            num1 = sub2Num(num1, num2 << (31 - i));
            result = add2Num(result, 1);
        }
    }
    
    if (minus)
        result = add2Num(~result, 1);
    return result;
}

int main() {
    printf("-199 / 3: %d %d\n", -199 / 3, div2Num(-199, 3));
    printf("938  / 5: %d %d\n", 938  / 5, div2Num( 938, 5));
    return 0;
}
