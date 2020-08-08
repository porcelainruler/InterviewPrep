from sys import stdin

def dp(arr: list, n: int):
    if n <= 2:
        return n

    dp = [[0]*n for i in range(n)]

    for i in range(n):
        dp[i][n-1] = 2
    
    maxEle = 2
    for j in range(n-2, 0, -1):
        i = j-1
        k = j+1

        while i >=0 and k<n:
            if arr[i] + arr[k] < 2*arr[j]:
                k += 1
            elif arr[i] + arr[k] > 2*arr[j]:
                dp[i][j] = 2
                i -= 1
            else:
                dp[i][j] = 1 + dp[j][k]
                maxEle = max(maxEle, dp[i][j])
                i -= 1
                k += 1

        while i >= 0:
            dp[i][j] = 2
            i -= 1

    return maxEle


def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        
        ans = dp(arr, n)
        print(ans)

if __name__ == '__main__':
    main()