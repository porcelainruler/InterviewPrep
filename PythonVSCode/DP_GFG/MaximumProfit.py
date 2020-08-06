from sys import stdin
import math

# Solution - O(n*k)
def dp(price, n, k):  
  
    # Table to store results of subproblems  
    # profit[t][i] stores maximum profit  
    # using atmost t transactions up to  
    # day i (including day i)  
    profit = [[0 for i in range(n + 1)]  
                 for j in range(k + 1)]  
  
    # Fill the table in bottom-up fashion  
    for i in range(1, k + 1):  
        prevDiff = float('-inf') 
          
        for j in range(1, n):  
            prevDiff = max(prevDiff, 
                           profit[i - 1][j - 1] - 
                           price[j - 1])  
            profit[i][j] = max(profit[i][j - 1],  
                               price[j] + prevDiff)  
  
    return profit[k][n - 1]

# Solution - O(n*n*k)
def dpMore(arr: list, n: int, k: int):
    dp = [[0]*(n) for i in range(k)]

    minEle = arr[0]

    for i in range(1, n):
        dp[0][i] = max(dp[0][i-1], arr[i] - minEle)
        if minEle > arr[i]:
            minEle = arr[i]

    for i in range(1, k):
        for j in range(n):

            maxPro = -math.inf
            for l in range(j):
                maxPro = max(maxPro, dp[i-1][l] + arr[j] - arr[l])
            
            dp[i][j] = max(dp[i][j-1], maxPro)

    for i in range(k):
        for j in range(n):
            print(dp[i][j], end=' ')
        print()
    print()

    return dp[k-1][n-1]

def main():
    t = int(input())

    for i in range(t):
        k = int(input())
        n = int(input())
        arr = list(map(int, stdin.readline().split()))

        ans = dp(arr, n, k)
        print(ans)

if __name__ == '__main__':
    main()