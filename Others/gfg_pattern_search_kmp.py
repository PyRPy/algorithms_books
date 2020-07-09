# gfg_pattern_search_kmp.py
def KMPSearch(pat, txt):
    M = len(pat) 
    N = len(txt) 
    # create longest prefix suffix lps
    lps = [0] * M 
    j = 0 # index for pat 

    # preprocessing the pat to find lps array 
    computeLPSArray(pat, M, lps) 
    i = 0 # index for txt 
    while i < N:
        if pat[j] == txt[i]:
            i += 1 
            j += 1 
        if j == M:
            print('find pattern at index ' + str(i-j)) 
            j = lps[j-1] 
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1 

def computeLPSArray(pat, M, lps):
    len = 0 
    lps[0] 
    i = 1 
    while i < M:
        if pat[i] == pat[len]:
            len += 1 
            lps[i] = len 
            i += 1 
        else:
            if len != 0:
                len = lps[len-1] 
            else:
                lps[i] = 0 
                i += 1 
# test 
txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMPSearch(pat, txt) 
# https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/?ref=lbp