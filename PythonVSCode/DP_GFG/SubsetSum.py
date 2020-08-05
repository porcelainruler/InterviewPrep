from sys import stdin

'''

public static boolean dp(int[] arr, int n) {
        int su = 0;
        for(int i=0 ; i<n ; i++)
            su += arr[i];
        
        if(su%2 == 1) {
            return false;
        }
        
        boolean[][] dp = new boolean[n+1][su+1];
        
        for(int i=0 ; i<n+1 ; i++)
            dp[i][0] = true;
            
        for(int i=1 ; i<su+1 ; i++)
            dp[0][i] = false;
        
        for(int i=1 ; i<n+1 ; i++)
            for(int j=1 ; j<su+1 ; j++) {
                if(arr[i-1] <= j) {
                    dp[i][j] = dp[i-1][j-arr[i-1]] | dp[i-1][j];
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        
        
        return dp[n][su/2];
    }

'''

def dp(arr: list, n: int):
    su = 0
    su = sum(arr)

    if su%2 == 1:
        return False

    dp = [[0]*(su+1) for i in range(n+1)]

    for i in range(1, su+1):
        dp[0][i] = False

    for i in range(n+1):
        dp[i][0] = True

    for i in range(1, n+1):
        for j in range(1, su//2 + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] | dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
            # Do Something

    return dp[n][su//2]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        
        ans = dp(arr, n)
        if ans:
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()