#code
from sys import stdin

def dp(n: int):
    if n <= 2:
        return n

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        # arr = list(map(int, stdin.readline().split()))
        # sarr = stdin.readline()
        n = int(input())
        ans = dp(n)
        print(ans)

if __name__ == '__main__':
    main()