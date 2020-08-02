from sys import stdin

def dp(sarr1: str, sarr2: str, m: int, n: int):
    dp = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                dp[i][j] = 0
            elif sarr1[i-1] == sarr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    return dp[m][n]

def main():
    t = int(input())

    for i in range(t):
        m, n = map(int, stdin.readline().split())
        sarr1 = list(map(str, stdin.readline().split()))[0]
        sarr2 = list(map(str, stdin.readline().split()))[0]

        ans = dp(sarr1, sarr2, len(sarr1), len(sarr2))
        print(ans)

if __name__ == '__main__':
    main()