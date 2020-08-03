from sys import stdin

def dp(arr: list, n: int):
    su = 0
    su = sum(arr)
    dp = [[0]*(su+1) for i in range(n+1)]

    for i in range(su+1):
        dp[i][0] = True

    for i in range(1, su+1):
        for j in range(1, n+1):
            None
            # Do Something

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        
        ans = dp(arr, n)
        print(ans)

if __name__ == '__main__':
    main()