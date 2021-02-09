#include <stdio.h>
/* from https://www.cprogramming.com */
int main()
{
    int n = 10;
    int array[] = {1, 4, 3, 6, 0, 10, 8, 2, 5, 7};

    printf("before soring: \n");
    for (int i=0; i < n; i++ ) {
        printf("%d ", array[i]);
    }
    for(int x=0; x<n; x++) {
 
        int index_of_min = x;
 
        for(int y=x; y<n; y++) {
 
            if(array[index_of_min]>array[y]) {
 
                index_of_min = y;
            }
        }
 
        int temp = array[x];
    
        array[x] = array[index_of_min];
    
        array[index_of_min] = temp;
    
    }
    printf("\nafter soring: \n");
    for (int i=0; i < n; i++ ) {
        printf("%d ", array[i]);
    }
    return 0;
}