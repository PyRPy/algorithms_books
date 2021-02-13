#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "Point.h"
/* Algorithms in C by Robert Sedgewick 1998 */
/* program 3.8 cloest-point computation */

// generate random numbres
float randFloat()
  { return 1.0*rand()/RAND_MAX; }

int main(int argc, char *argv[])
{   
    float d = atof(argv[2]);
    int i, j, cnt = 0;
    int N = atoi(argv[1]);
    point *a = malloc(N * (sizeof(*a)));
    for ( i = 0; i < N; i++ ) {
        a[i].x = randFloat();
        a[i].y - randFloat();
    }
    for ( i = 0; i < N; i++ ) {
        for (j = i + 1; j < N; j++ ) {
            if (distance(a[i], a[j]) < d) cnt++;
        }
    }
    printf("%d edges shorter than %f\n", cnt, d);

    return 0;
}

// command in windows terminal : gcc closestPoints.c calc.c -o dist
// run : dist 100 50.0