#include <stdio.h>
#include <stdlib.h>
/* Computer Programming in C for Beginners - Avelino J. Gonzalez */
void swap(int [], int, int);
void printout(int []);

int main()
{
    int a[] = {4, 1, 9, 5, 7, 3, 8, 0, 6, 2};
    int i, j, small;

    printout(a);
    printf("\n\n");

    for (i=0; i<10; i++) {
        small = i;
        for (j=i+1; j<10; j++) {
            if(a[j] < a[small])
                small = j;
        }
        swap(a, i, small);
        printout(a); /* print out for comparison */
        printf("\n");
    }
    printout(a);
    printf("\n\n");

    return 0;
}

void swap(int a[], int x, int y)
{
    int temp = 0;
    temp = a[x];
    a[x] = a[y];
    a[y] = temp;
}

void printout(int a[])
{
    int n;
    for (n=0; n<10; n++)
        printf(" %d ", a[n]);
}