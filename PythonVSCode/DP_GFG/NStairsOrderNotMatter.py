#code
from sys import stdin

def fastest(n: int):
    return n//2 + 1;

def dp(n: int):
    dp = [0]*(n+1)
    dp[0] = 1

    for i in range(1, n+1):
        dp[i] += dp[i-1]
    
    for i in range(2, n+1):
        dp[i] += dp[i-2]

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        # arr = list(map(int, stdin.readline().split()))
        # sarr = stdin.readline()
        n = int(input())
        # ans = dp(n)
        ans = fastest(n)
        print(ans)

if __name__ == '__main__':
    main()