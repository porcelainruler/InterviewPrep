#code
from sys import stdin

'''
Java Code:
// function to count ways to reach mth stair
    Long countWays(int n){
        
        // your code here
        if(n<=2)
            return (long)n;
    
        long a=1;
        long b=1;
        long c=2;
        for(int i=3 ; i<n+1 ; i++){
            long temp = c;
            c = (b+c)%1000000007;
            a = b;
            b = temp;
        }
    
    return c%1000000007;
        
    }

'''

# Space- O(1)
def dpSpace(n: int):
    if n<=2:
        return n
    
    a=1
    b=1
    c=2
    for i in range(3, n+1):
        temp = c
        c = (b+c)%1000000007
        a = b
        b = temp
    
    return c

def dp(n: int):
    if n <= 2:
        return n

    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def main():
    t = int(input())

    for i in range(t):
        # arr = list(map(int, stdin.readline().split()))
        # sarr = stdin.readline()
        n = int(input())
        # ans = dp(n)
        ans = dpSpace(n)
        print(ans)

if __name__ == '__main__':
    main()
