from sys import stdin
import sys
import math

def dp(n: int, k: int, mapper: dict):
    if k == 1 or k==0:
        return k

    if n == 1:
        return k

    #key = str(n) + '-' + str(k)
    #if mapper.get(key) is not None:
    #    return mapper.get(key)

    minEle = math.inf
    
    for i in range(1, k+1):
        eBreak = dp(n-1, i-1, mapper)
        eSafe = dp(n, k-i, mapper)

        val = max(eBreak, eSafe)

        if minEle > val:
            minEle = val  
    
    #if mapper.get(key) is not None:
    #    mapper[key] = minEle + 1

    return minEle + 1


def dpBU(n, k):
    dp = [[0]*(k+1) for i in range(n+1)]

    for i in range(1, n+1):
        dp[i][0] = 0
        dp[i][1] = 1
    
    for i in range(1, k+1):
        dp[1][i] = i

    for i in range(2, n+1):
        for j in range(2, k+1):
            dp[i][j] = math.inf
            for l in range(1, j+1):
                res = max(dp[i-1][l-1], dp[i][j-l]) + 1
                if res < dp[i][j]:
                    dp[i][j] = res
    
    return dp[n][k]

def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, stdin.readline().split())
        mapper = dict()
        #ans = dp(n, k, mapper)
        ans = dpBU(n, k)
        print(ans)

if __name__ == '__main__':
    main()