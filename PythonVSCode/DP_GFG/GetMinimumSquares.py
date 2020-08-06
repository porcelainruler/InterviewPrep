from sys import stdin
import math

def dp(n: int):
    arr = list()
    i=1
    while i*i <= n:
        arr.append(i*i)
        i += 1

    dp = [0]*(n+1)

    dp[0:4] = [0, 1, 2, 3]

    for i in range(4, n+1):
        dp[i] = i
        for j in range(1, int(math.ceil(math.sqrt(i))) + 1):
            if j*j > i:
                break
            else:
                dp[i] = min(dp[i], dp[i-j*j]+1)
        
    # for i in range(n+1):
    #     print(dp[i], end = ' ')
    # print()

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        ans = dp(n)
        print(ans)

if __name__ == '__main__':
    main()