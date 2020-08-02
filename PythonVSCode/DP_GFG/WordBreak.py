from sys import stdin

def dp(sarr: str, mapper: dict, n: int):
    dp = [[0]*(n) for i in range(n)]

    for l in range(1, n+1):
        for i in range(n):
            j = i + l - 1

            if mapper.get(sarr[i:j+1]) != None:
                dp[i][j] = 1
                continue
            else:
                None
                # Do Something

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(str, stdin.readline().split()))

        mapper = dict()
        for item in arr:
            mapper[item] = 1
        sarr = input()

        ans = dp(sarr, mapper, len(sarr))

if __name__ == '__main__':
    main()