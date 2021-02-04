#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand(time(0));
    int number = rand() % 100 + 1;
    int count = 0;
    int a = 0;
    printf("there is a number between 1 and 100: ");

    do {
        printf("guess this number: ");
        scanf("%d", &a);
        count ++;
        if (a > number) {
            printf("too large \n");
        } else if (a < number) {
            printf("too small \n");
        }
    } while (a != number);
    printf("great, you guessed %d times to find the right number. \n", count);

    return 0;
}