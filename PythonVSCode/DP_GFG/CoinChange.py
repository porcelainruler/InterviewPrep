from sys import stdin

def dp(arr: list, n: int, k: int):
    dp = [0]*(k+1)
    dp[0] = 1

    for i in range(n):
        key = arr[i]
        for j in range(key, k+1):
            dp[j] += dp[j-key]

    return dp[k]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        k = int(input())

        ans = dp(arr, n, k)
        print(ans)

if __name__ == '__main__':
    main()