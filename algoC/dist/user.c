#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include "Point.h"
/* Algorithms in C by Robert Sedgewick 1998 */
// generate random numbres
float randFloat()
  { return 1.0*rand()/RAND_MAX; }

int main()
{ 
    // create two points
    point p1;
    point p2;

    // give values to each point
    p1.x = randFloat() * 100.0;
    p1.y = randFloat() * 100.0;

    p2.x = randFloat() * 100.0;
    p2.y = randFloat() * 100.0;

    // print out distance as result
    printf("distance is %f ", distance(p1, p2));

    return 0;
}

// command in windows terminal : gcc user.c calc.c -o dist