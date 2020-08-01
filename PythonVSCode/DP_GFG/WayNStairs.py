# 1 stair or 2 stair at a time
from sys import stdin

'''
very simple explanation for "return m/2 +1"...
# this problem is same as no of non-negative integer solution of (1*x+2*y=m)
since "y" can take value 0,1,2...up-to floor(m/2)==m/2 and hence we got unique "x" for this y 
so total no of solution is => no of values "y" can take.... i.e. 1+m/2

what if we have 3 steps too...
just extend above logic solve for no of non-negative integer solution of (1*x+2*y+3*z=m)
so here z takes values 0,1,2....floor(m/3) so solve for every sub-equation 1*x+2*y=m-3*z.
and we know solution of this i.e. 1+(m-3*z)/2 so just add this for all possible value of z.... 
∑{1+(m-3*i)/2} 0≤i≤floor(m/3)
'''

def sol(m):
    return 1 + m//2

def dp(n: int):
    dp = [0]*(n+1)

    dp[0] = 1

    for i in range(1, n+1):
        dp[i] += dp[i-1]
    
    for i in range(2, n+1):
        dp[i] += dp[i-2]

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        ans = dp(n)
        print(ans)


if __name__ == '__main__':
    main()