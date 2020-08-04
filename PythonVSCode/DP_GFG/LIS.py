#code
from sys import stdin

def dp(arr: list, n: int):
    dp = [0]*n
    
    dp[0] = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < 1+dp[j]:
                dp[i] = 1 + dp[j]

    return max(dp)

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        
        ans = dp(arr, n)
        print(ans)

if __name__ == '__main__':
    main()