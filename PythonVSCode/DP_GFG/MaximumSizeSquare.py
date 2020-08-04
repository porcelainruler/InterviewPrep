'''
1) Construct a sum matrix S[R][C] for the given M[R][C].
     a)    Copy first row and first columns as it is from M[][] to S[][]
     b)    For other entries, use following expressions to construct S[][]
         If M[i][j] is 1 then
            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
         Else /*If M[i][j] is 0*/
            S[i][j] = 0
2) Find the maximum entry in S[R][C]
3) Using the value and coordinates of maximum entry in S[i], print 
   sub-matrix of M[][]
'''

from sys import stdin
import math

def dp(arr: list, m: int, n: int):
    dp = [[0]*(n) for i in range(m)]

    maxDim = -math.inf
    for i in range(m):
        dp[i][0] = arr[i][0]
        if maxDim < dp[i][0]:
            maxDim = dp[i][0]
    for i in range(n):
        dp[0][i] = arr[0][i]
        if maxDim < dp[0][i]:
            maxDim = dp[0][i]

    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
            else:
                dp[i][j] = 0
            
            if maxDim < dp[i][j]:
                maxDim = dp[i][j]

    return maxDim

def main():
    t = int(input())

    for i in range(t):
        m, n = map(int, stdin.readline().split())
        arr = list()

        subarr = list(map(int, stdin.readline().split()))
        for j in range(len(subarr)//n):
            arr.append(subarr[j*n : (j+1)*n])

        ans = dp(arr, m, n)
        print(ans)

if __name__ == '__main__':
    main()