#include <stdio.h>
#include <stdlib.h>

/* Algorithms in C by Robert Sedgewick 1990 */
struct node
    { int key; struct node *next; };

int main()
{
    int i, N, M;
    struct node *t, *x;
    scanf("%d %d", &N, &M);
    t = (struct node*) malloc(sizeof *t);
    t->key = 1;
    x = t;
    for (i = 2; i <= N; i++ )
    {
        t ->next = (struct node * ) malloc(sizeof *t);
        t = t -> next;
        t -> key = i;
    }
    t -> next = x;
    while (t != t -> next ) {
        for (i = 1; i < M; i++ ) t = t -> next;
        printf("%d ", t -> next -> key );
        x = t -> next;
        t -> next = t -> next -> next;
        free(x);
    }
    printf("%d\n", t -> key);

    return 0;
}