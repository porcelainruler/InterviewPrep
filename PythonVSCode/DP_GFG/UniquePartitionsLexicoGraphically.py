from sys import stdin

def printResult(sarr, n):
    for i in range(n):
        print(sarr[i], end=' ')
    print()

def dp(n: int):
    dp = [0]*n
    idx = 0
    dp[idx] = n

    while True:
        printResult(dp, idx+1)

        res_val = 0
        while idx >=0 and dp[idx] == 1:
            res_val += dp[idx]
            idx -= 1
    
        # If Out of List i.e. all 1
        if idx < 0:
            print()
            return

        dp[idx] -= 1
        res_val += 1

        # If res_val > dp[idx] : Sorting Order Messed Up
        while res_val > dp[idx]:
            dp[idx+1] = dp[idx]
            res_val = res_val - dp[idx]
            idx += 1

        # Shifting res_val to next idx
        dp[idx+1] = res_val
        idx += 1 

def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        ans = dp(n)

if __name__ == '__main__':
    main()