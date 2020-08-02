# Can Select First or Last
'''
F(i, j) represents the maximum value the user
can collect from i'th coin to j'th coin.

F(i, j) = Max(Vi + min(F(i+2, j), F(i+1, j-1) ), 
              Vj + min(F(i+1, j-1), F(i, j-2) ))
As user wants to maximise the number of coins. 

Base Cases
    F(i, j) = Vi           If j == i
    F(i, j) = max(Vi, Vj)  If j == i + 1
'''

# Bottom-Up Approach:

from sys import stdin

def dp(arr: list, n):
    dp = [[0]*(n) for i in range(n)]

    for gap in range(n):
        i = 0
        j = gap
        while(j < n):
            val1 = 0
            val2 = 0
            val3 = 0
            if i+2 <= j:
                val1 = dp[i+2][j] 
            
            if i+1 <= j-1:
                val2 = dp[i+1][j-1]
            
            if i <= j-2:
                val3 = dp[i][j-2]

            start = arr[i] + min(val1, val2)
            end = arr[j] + min(val2, val3)

            dp[i][j] = max(start, end)
            i += 1
            j += 1
        
        gap += 1
    
    return dp[0][n-1]

    
def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        ans = dp(arr, n)

        print(ans)

if __name__ == '__main__':
    main()