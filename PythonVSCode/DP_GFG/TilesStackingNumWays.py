# Tile Dim. - 1x4 : To Fill nx4
from sys import stdin

def dp(n: int):
    if n<4:
        return 1
        
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, n+1):
        dp[i] += dp[i-1] + dp[i-4]
    

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        ans = dp(n)
        print(ans)

if __name__ == '__main__':
    main()