#include <stdio.h>
#include <string.h>

void search(char pat[], char txt[])
{
    int M = strlen(pat);
    int N = strlen(txt);
    int i = 0;

    while (i <= N - M)
    {
        int j;
        for (j = 0; j < M; j++){
            if (txt[i+j] != pat[j])
                break;
        }

        if (j == M){
            printf("pattern found at index %d \n", i);
            i = i + M;
        } else if (j == 0){
            i = i + 1;
        } else
        {
            i = i + j;
        }
        
    }
}

// test 
int main()
{
    char txt[] = "ABCEABCDABCEABCD"; 
    char pat[] = "ABCD";
    search(pat, txt);
    return 0;
}