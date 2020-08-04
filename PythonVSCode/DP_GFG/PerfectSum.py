from sys import stdin


def dp(arr: list, k: int, n: int):
    dp = [[0]*(k+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, k+1):
        dp[0][i] = 0    

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][k]

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        k = int(input())

        ans = dp(arr, k, n)
        print(ans)


if __name__ == '__main__':
    main()


# 1
# 6
# 2 3 5 6 8 10
# 10


'''

# Java Solution -  {Python Giving TLE}

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {
     /*
     
     def dp(arr: list, k: int, n: int):
    dp = [[0]*(k+1) for i in range(n+1)]

    for i in range(n+1):
        dp[i][0] = 1
    
    for i in range(1, k+1):
        dp[0][i] = 0    

    for i in range(1, n+1):
        for j in range(1, k+1):
            if j >= arr[i-1]:
                dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][k]
     
     */
    public static int dp(int[] arr, int sum, int n) {
        int[][] dp = new int[n+1][sum+1];
        
        for(int i=0 ; i<sum+1 ; i++)
            dp[0][i] = 0;
        
        for(int i=0 ; i<n+1 ; i++)
            dp[i][0] = 1;
            
        for(int i=1 ; i<n+1 ; i++)
            for(int j=1 ; j<sum+1 ; j++) {
                if(j >= arr[i-1])
                    dp[i][j] = (dp[i-1][j-arr[i-1]] + dp[i-1][j])%1000000007;
                else
                    dp[i][j] = dp[i-1][j];
            }
        return dp[n][sum];
    }
    
	public static void main (String[] args)
	 {
	    Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();
	    
	    for(int i=0 ; i<t ; i++) {
	        int n = sc.nextInt();
	        int[] arr = new int[n];
	        
	        for(int j=0 ; j<n ; j++) {
	            arr[j] = sc.nextInt();
	        }
	        
	        int sum = sc.nextInt();
	        int ans = dp(arr, sum, n);
	        System.out.println(ans);
	    }
	 }
}

'''