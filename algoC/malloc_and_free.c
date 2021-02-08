#include <stdio.h>
#include <stdlib.h>
/* https://www.youtube.com/watch?v=5KRGH2IoF7Q */

int main()
{
    void *p;
    int cnt = 0;
    p = malloc(100 * 1024 * 1024);
    p++;
    free(p);

    return 0;
}