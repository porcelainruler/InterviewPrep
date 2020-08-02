from sys import stdin

def dp(W, wt, val, n): 
    dp = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                dp[i][w] = 0
            elif wt[i-1] <= w: 
                # Just simple dp[i][w-wt[i-1]] in place of dp[i-1][w-wt[i-1]] So as to incl for Repition
                dp[i][w] = max(val[i-1] + dp[i][w-wt[i-1]],  dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 
  
    return dp[n][W]

def main():
    t = int(input())

    for i in range(t):
        n, w = map(int, stdin.readline().split())
        price = list(map(int, stdin.readline().split()))
        weight = list(map(int, stdin.readline().split()))

        mapper = dict()

        ans = dp(w, weight, price, n)
        print(ans)


if __name__ == "__main__":
    main()