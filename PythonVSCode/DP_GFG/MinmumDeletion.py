from sys import stdin

def dp(sarr: str, n: int):
    dp = [[0]*(n) for i in range(n)]

    for k in range(2, n+1):

        for i in range(0, n-k+1):
            j = i + k - 1

            if sarr[i] == sarr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
        
        '''
        for j in range(len(dp)):
            for k in range(len(dp[0])):
                print(dp[j][k], end = ' ')
            print()
        print()
        print()
        '''
        
    return dp[0][n-1]

def dpTD(sarr: str, sidx: int, eidx: int, mapper: dict):
    if sidx >= eidx:
        return 0
    
    key = str(sidx) + '|' + str(eidx)

    if mapper.get(key) != None:
        return mapper.get(key)

    if sarr[sidx] == sarr[eidx]:
        # ans1 = dp(sarr, sidx+1, eidx) + 1
        # ans2 = dp(sarr, sidx, eidx-1) + 1
        ans = dpTD(sarr, sidx+1, eidx-1, mapper)
        # ans = min(min(ans1, ans2), ans3)
    else:
        ans1 = dpTD(sarr, sidx+1, eidx, mapper) + 1
        ans2 = dpTD(sarr, sidx, eidx-1, mapper) + 1
        ans = min(ans1, ans2)

    mapper[key] = ans
    return ans

def main():
    t = int(input())

    for i in range(t):
        sarr = stdin.readline()[:-1]
        # mapper = dict()

        # ans = dpTD(sarr, 0, len(sarr)-1, mapper)
        ans = dp(sarr, len(sarr))
        print(ans)

if __name__ == '__main__':
    main()

# 2
# aebcbda
# geeksforgeeks