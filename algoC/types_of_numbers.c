/* Algorithms in C by Robert Sedgewick 1998 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef int Number;
Number randNum() {
    return rand();
}

int main(int argc, char *argv[])
{
    int i, N = atoi( argv[1]);
    float m1 = 0.0;
    float m2 = 0.0;
    Number x;
    for (i = 0; i < N; i++ ){
        x = randNum();
        m1 += ((float) x ) / N;
        m2 += ((float) x * x) / N;
    }

    printf("     Average: %f\n", m1);
    printf("Std. Deviation: %f\n", sqrt(m2 - m1 * m1));

    return 0;
}

/* types_of_numbers 1000000 */

