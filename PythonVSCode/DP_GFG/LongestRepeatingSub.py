from sys import stdin

def dp(sarr: str, n: int):
    dp = [[None]*(n+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):

            if i == 0 or j == 0:
                dp[i][j] = 0
            elif sarr[i-1] == sarr[j-1] and i!=j:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])


    return dp[n][n]

def main():
    t = int(input())

    for i in range(t):
        m = list(map(int, stdin.readline().split()))[0]
        sarr = list(map(str, stdin.readline().split()))[0]

        ans = dp(sarr, len(sarr))
        print(ans)

if __name__ == '__main__':
    main()


'''

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {  
    public static int dp(String str, int n) {
        int[][] dp = new int[n+1][n+1];
        for(int i=0 ; i<n+1 ; i++) {
            for(int j=0 ; j<n+1 ; j++) {
                if(i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if(str.charAt(i-1) == str.charAt(j-1) && i!=j) {
                    dp[i][j] = dp[i-1][j-1] + 1;
                } else {
                    dp[i][j] = Integer.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        
        return dp[n][n];
    }
    
	public static void main (String[] args)
	 {
	    Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();
	    for(int i=0 ; i<t ; i++) {
	        int n = sc.nextInt();
	        sc.nextLine();
	        String str = sc.nextLine();
	        int ans = dp(str, n);
	        System.out.println(ans);
	    }
	 }
}

'''