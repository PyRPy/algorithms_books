#include <stdio.h>
#include <stdlib.h>

/* Algorithms in C by Robert Sedgewick 1998 */
int heads() {
    return rand() < RAND_MAX/2;
}

int main()
{ 
    int i, j, cnt;
    int N = 1000;
    int M = 300;
    int *f = malloc((N+1)*sizeof(int));
    for ( j = 0; j <= N; j++ ) f[j] = 0;
    for ( i = 0; i < M; i++, f[cnt]++ ) {
        for (cnt = 0, j = 0; j <= N; j++ ) {
            if (heads()) cnt++;
        }
    }

    for (j = 0; j <= N; j++ ) {
        // printf("%2d ", j);
        printf("%2d ", f[j]);
        for ( i = 0; i < f[j]; i+=10 ) {
        printf("*");
        }
        printf("\n");
    }


    return 0;
}

// somwhow not working !