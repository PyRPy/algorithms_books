// insertion sort
/* The Algorithm Design Manual - Steven S. Skiena */
// https://www3.cs.stonybrook.edu/~algorith/book/programs/sorting.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int findmatch(char *p, char *t)
{
    int i, j;                               /* index counters */
    int m, n;                               /* string lengths */

    m = strlen(p);
    n = strlen(t);

    for (i = 0; i<=(n-m); i=i+1) {
        j = 0;
        while ((j < m) && (t[i+j] == p[j]))
                j = j + 1;
        if (j == m) return(i);
    }

    return(-1);
}

main()
{

    char letters[] = "abba";
    char text[] = "aababba";

    int result;
    result = findmatch(letters, text);

    printf("The result is %dth :", result + 1, "element in the text.");

    return 0;
}