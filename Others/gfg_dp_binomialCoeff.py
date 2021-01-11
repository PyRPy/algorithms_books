# gfg_binomialCoeff
# https://www.geeksforgeeks.org/binomial-coefficient-dp-9/
def binomialCoeff(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    # recursive call
    return binomialCoeff(n-1, k-1) + binomialCoeff(n-1, k)

# test
n = 5
k = 2

print("the value of C(%d, %d) is %d" % (n, k, binomialCoeff(n, k)))

# use 2D array for DP
def binomialCoeff2(n, k):
    C = [[0 for x in range(k+1)] for x in range(n+1)]
    # bottom up manner
    for i in range(n+1):
        for j in range(min(i, k) + 1):
            # base case
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j-1] + C[i-1][j]
    return C[n][k]

print("values of C[" + str(n) + "][" + str(k) + "] is "
      + str(binomialCoeff2(n, k)))

# use pascal triangle and less memory
def binomialCoeff3(n, k):
    C = [0 for i in range(k+1)]
    C[0] = 1
    for i in  range(1, n+1):
        j = min(i, k)
        while j > 0:
            C[j] = C[j] + C[j-1]
            j -= 1
    return C[k]

print("the value of C(%d, %d) is %d" % (n, k, binomialCoeff3(n, k)))

# with help of look-up table
# naive recurisve + look-up table

def binomialCoeffUtil(n, k, dp):
    # return
    if dp[n][k] != -1:
        return dp[n][k]
    # store
    if k == 0:
        dp[n][k] = 1
        return dp[n][k]
    if k == n:
        dp[n][k] = 1
        return dp[n][k]

    # save value in lookup table before return
    dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
                binomialCoeffUtil(n - 1, k, dp))

    return dp[n][k]

def binomialCoeff4(n, k):
    # make a temp lookup table
    dp = [[-1 for y in range(k+1)] for x in range(n+1)]
    return binomialCoeffUtil(n, k, dp)


print("values of C[" + str(n) + "][" + str(k) + "] is "
      + str(binomialCoeff4(n, k)))
    
