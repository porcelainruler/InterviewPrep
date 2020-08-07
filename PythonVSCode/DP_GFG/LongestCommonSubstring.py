'''

The longest common suffix has following optimal substructure property.

If last characters match, then we reduce both lengths by 1
LCSuff(X, Y, m, n) = LCSuff(X, Y, m-1, n-1) + 1 if X[m-1] = Y[n-1]
If last characters do not match, then result is 0, i.e.,
LCSuff(X, Y, m, n) = 0 if (X[m-1] != Y[n-1])

Now we consider suffixes of different substrings ending at different indexes.
The maximum length Longest Common Suffix is the longest common substring.
LCSubStr(X, Y, m, n) = Max(LCSuff(X, Y, i, j)) where 1 <= i <= m and 1 <= j <= n

'''

from sys import stdin
import math

def dp(a: str, b: str, m: int, n: int):
    dp = [[0]*(n+1) for i in range(m+1)]

    maxLen = 0

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                maxLen = max(maxLen, dp[i][j])
            else:
                dp[i][j] = 0

    return maxLen

def main():
    t = int(input())

    for i in range(t):
        m, n = map(int, stdin.readline().split())
        a = input()
        b = input()
        
        ans = dp(a, b, m, n)
        print(ans)

if __name__ == '__main__':
    main()