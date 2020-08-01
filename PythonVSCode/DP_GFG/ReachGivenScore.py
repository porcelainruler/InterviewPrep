# Score Can be 3, 5, 10  - Combination/Selection part is Here
# For Permutation dp[i] = dp[i-3] + dp[i-5] + dp[i-10]

def DP(n: int):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        if i-3 >= 0:
            dp[i] += dp[i-3]
    for i in range(1, n+1):
        if i-5 >= 0:
            dp[i] += dp[i-5] 
    for i in range(1, n+1):
        if i-10 >= 0:
            dp[i] += dp[i-10] 

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        print(DP(n))

if __name__ == '__main__':
    main()

