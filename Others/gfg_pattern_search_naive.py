# gfg_pattern_search_naive.py
def search(pat, txt):
    M = len(pat) 
    N = len(txt) 

    # slide pat[] one by one 
    for i in range(N - M + 1):
        j = 0 
        while j < M:
            if txt[i + j] != pat[j]:
                break 
            j += 1 
        if j == M:
            print('pattern found at index: ', i) 
# test 
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search(pat, txt) 

# https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
# code addapted from C++/Java, changed to python style here for consistency