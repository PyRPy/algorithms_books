#include <stdio.h>
#include <stdlib.h>
/* https://www.youtube.com/watch?v=5KRGH2IoF7Q */

int main()
{
    void *p;
    int cnt = 0;
    while ((p = malloc(100 * 1024 * 1024))) {
        cnt++;
    }

    printf("it is allocated %d00MB space\n", cnt);

    return 0;
}