from sys import stdin

def dp(sarr: str, n: int):
    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = 0
    
    for length in range(2, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if sarr[i] == sarr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

    # for i in range(n):
    #     for j in range(n):
    #         print(dp[i][j], end = ' ')
    #     print()
    # print()

    return dp[0][n-1]

def main():
    t = int(input())

    for i in range(t):
        sarr = list(map(str, stdin.readline().split()))[0]

        ans = dp(sarr, len(sarr))
        print(ans)

'''
3
abcd
aba
geeks
'''

if __name__ == '__main__':
    main()