from sys import stdin

'''

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {  
    public static int dp(String str1, String str2, int n) {
        int[][] dp = new int[n+1][n+1];
        for(int i=0 ; i<n+1 ; i++) {
            for(int j=0 ; j<n+1 ; j++) {
                if(i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if(str1.charAt(i-1) == str2.charAt(j-1)) {
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
	    sc.nextLine();
	    for(int i=0 ; i<t ; i++) {
	        String str1 = sc.nextLine();
	        
	        StringBuilder st = new StringBuilder(str1);
	        st = st.reverse();
	        String str2 = st.toString();
	        
	        int ans = dp(str1, str2, str1.length());
	        System.out.println(ans);
	    }
	 }
}

'''

def dp(sarr1: str, sarr2: str, n: int):
    dp = [[0]*(n+1) for i in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j] = 0
            elif sarr1[i-1] == sarr2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # for i in range(n+1):
    #     for j in range(n+1):
    #         print(dp[i][j], end = ' ')
    #     print()
    # print()

    return dp[n][n]

def main():
    t = int(input())

    for i in range(t):
        sarr1 = list(map(str, stdin.readline().split()))[0]
        
        ans = dp(sarr1, sarr1[::-1], len(sarr1))
        print(ans)

if __name__ == '__main__':
    main()