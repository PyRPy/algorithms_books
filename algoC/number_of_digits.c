#include <stdio.h>
/* very interesting */
int main()
{
    int x;
    x = 12345;
    int digit;
    int ret = 0;

    while (x > 0) {
        digit = x % 10;
        ret = ret * 10 + digit;
        printf("x=%d, digit=%d, ret=%d\n", x, digit, ret);
        x /= 10;
    }

    printf("%d", ret);
    
    return 0;
}