from sys import stdin

def dp(arr: list, n: int):
    dp = [0]*(n+1)

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))
        sarr = stdin.readline()

# i = 8
# change = i << 1
# print(change)

if __name__ == '__main__':
    main()