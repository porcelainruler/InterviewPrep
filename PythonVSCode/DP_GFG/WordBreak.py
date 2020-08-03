from sys import stdin

def dp(sarr: str, mapper: dict, n: int):
    dp = [[0]*(n) for i in range(n)]

    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i + l - 1

            if mapper.get(sarr[i:j+1]) != None:
                dp[i][j] = True
                continue
            else:
                if i == j:
                    dp[i][j] = False
                else:
                    for k in range(i, j):
                        if dp[i][k] and dp[k+1][j]:
                            dp[i][j] = True
                            break
                        else:
                            dp[i][j] = False
                # Do Something
    
    '''
    # For Printing DP Table:
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            print(dp[i][j], end = ' ')
        print()
    print()
    '''
    return dp[0][n-1]

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
        print(ans)

'''
2
12
i like sam sung samsung mobile ice cream icecream man go mango
ilike
12
i like sam sung samsung mobile ice cream icecream man go mango
idontlike
'''

if __name__ == '__main__':
    main()