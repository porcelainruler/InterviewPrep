from sys import stdin

def dp(sarr: str, n: int):
    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1):
        if sarr[i] == sarr[i+1]:
            dp[i][i+1] = 1

    for length in range(3, n+1):
        for i in range(n - length + 1):
            j = i + length - 1
            if sarr[i] == sarr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 0

    # for i in range(n):
    #     for j in range(n):
    #         print(dp[i][j], end = ' ')
    #     print()
    # print()

    ans = 0
    for su in dp:
        ans += sum(su) -1

    return ans

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        sarr = list(map(str, stdin.readline().split()))[0]

        ans = dp(sarr, len(sarr))
        print(ans)

if __name__ == '__main__':
    main()