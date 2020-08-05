from sys import stdin
import math

def dp(arr: list, m: int, n: int):
    dp = [[0]*n for i in range(m)]

    for i in range(m):
        dp[i][n-1] = arr[i][n-1]
    
    for i in range(n-2, -1, -1):
        for j in range(m):
            a1 = 0
            a2 = 0
            a3 = 0

            if j-1 >= 0 and i+1<n:
                a1 = dp[j-1][i+1]
            
            a2 = dp[j][i+1]

            if j+1 < m and i < n:
                a3 = dp[j+1][i+1]
            
            dp[j][i] = max(a1, max(a2, a3)) + arr[j][i]

    # for i in range(m):
    #     for j in range(n):
    #         print(dp[i][j], end=' ')
    #     print()
    # print()
    maxEle = -math.inf
    for i in range(m):
        if maxEle < dp[i][0]:
            maxEle = dp[i][0] 

    return maxEle 

def main():
    t = int(input())

    for i in range(t):
        m, n = map(int, stdin.readline().split())
        subarr = list(map(int, stdin.readline().split()))
        arr = list()
        for j in range(m):
            arr.append(subarr[j*n: (j+1)*n])
        
        ans = dp(arr, m , n)
        print(ans)

if __name__ == '__main__':
    main()