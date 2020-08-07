from sys import stdin

def dp(a: str, b: str, c: str, m: int, n: int):
    dp = [[False]*(n+1) for i in range(m+1)]

    if (m + n) != len(c):
        return False

    for i in range(m+1):
        for j in range(n+1):
            if i==0 and j==0:
                dp[i][j] = True

            elif i == 0 and b[j-1] == c[i+j-1]:
                dp[i][j] = dp[i][j-1]
            
            elif j == 0 and a[i-1] == c[i+j-1]:
                dp[i][j] = dp[i-1][j]
            
            elif a[i-1] != c[i+j-1] and b[j-1] ==c[i+j-1]:
                dp[i][j] = dp[i][j-1]

            elif a[i-1] == c[i+j-1] and b[j-1] !=c[i+j-1]:
                dp[i][j] = dp[i-1][j]

            elif a[i-1] == c[i+j-1] and b[j-1] ==c[i+j-1]:
                dp[i][j] = dp[i][j-1] | dp[i-1][j]

            else:
                dp[i][j] = False 
    
    #for i in range(m+1):
    #    for j in range(n+1):
    #        print(dp[i][j], end = ' ')
    #    print()

    return dp[m][n]

def main():
    t = int(input())

    for i in range(t):
        a, b, c = map(str, stdin.readline().split())
        
        ans = dp(a, b, c, len(a), len(b))
        # print(len(a), len(b), len(c))
        if ans:
            print(1)
        else:
            print(0)

if __name__ == '__main__':
    main()