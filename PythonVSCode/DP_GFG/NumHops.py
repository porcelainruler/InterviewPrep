from sys import stdin

def dp(n: int):
    dp = [0]*(n+1)
    dp[0] = 1
    if n==0:
        return dp[0]
    dp[1] = 1
    if n==1:
        return dp[1]
    dp[2] = 2
    if n==2:
        return dp[2]

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

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