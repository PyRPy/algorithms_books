// insertion sort
/* The Algorithm Design Manual - Steven S. Skiena */
// https://www3.cs.stonybrook.edu/~algorith/book/programs/sorting.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define NELEM	10		/* size of test arrays */

insertion_sort(int s[], int n)
{
    int i, j;
    for (i=1; i < n; i++) {
        j = i;
        while ((j > 0) && (s[j] < s[j-1])) {
            swap(&s[j], &s[j-1]);
            j = j -1;
        }
    }
}

swap(int *a, int *b)
{
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

random_permutation(int a[], int n)
{
    int i;
    for (i=n; i>1; i--) swap(&a[i-1], &a[random_int(0, i-1)]);
}

random_int(low,high)
int low,high;                                /*lower/upper bounds on numb*/
{
    int rand();
    int i,j,r;                               /*random number*/

    i = RAND_MAX / (high-low+1);
    i *= (high-low+1);
    while ((j = rand()) >=i) continue;
    r = (j % (high-low+1)) + low;
    /*printf("rand=%d RAND_MAX=%d \n",r,RAND_MAX);*/
    /*printf("rand=%d low=%d high=%d \n",r,low,high);*/
    if ((r < low) || (r > high))
            printf("Error: random integer %d out of range [%d,%d]\n",
                    r,low,high);

    return(r);
}

main()
{
    int s[NELEM+2];
    int n;
    int i,j;

    for (i=0; i<NELEM; i++) s[i] = NELEM - i;
    random_permutation(s, NELEM);
    for (i=0; i<NELEM; i++) printf("%d ", s[i]);

    // sorting
    insertion_sort(s, NELEM);

    printf("\n\nInsertion sort: \n");
    for (i=0; i<NELEM; i++) printf("%d ", s[i]);

    return 0;
}