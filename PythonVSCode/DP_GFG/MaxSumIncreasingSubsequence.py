#code
from sys import stdin

def dp(arr: list, n: int):
    dp = [0]*n
    
    for i in range(n):
        dp[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < arr[i]+dp[j]:
                dp[i] = arr[i] + dp[j]

    return max(dp)

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        
        ans = dp(arr, n)
        print(ans)

if __name__ == '__main__':
    main()

'''

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
 {  
    
    public static int dp(int[] arr, int n) {
        int[] dp = new int[n];
        
        for(int i=0 ; i<n ; i++) {
            dp[i] = arr[i];
            for(int j=0 ; j<i ; j++) {
                if(arr[i] > arr[j] && dp[i] < dp[j] + arr[i])
                    dp[i] = dp[j] + arr[i];
            }
        }
        
        int max = -1;
        for(int i=0 ; i<n ; i++)
            if(max < dp[i])
                max = dp[i];
                
        return max;
    }
    
	public static void main (String[] args)
	 {
	    Scanner sc = new Scanner(System.in);
	    int t = sc.nextInt();
	    for(int i=0 ; i<t ; i++) {
	        int n = sc.nextInt();
	        int[] arr = new int[n];
	        for(int j=0 ; j<n ; j++)
	            arr[j] = sc.nextInt();
	        
	        int ans = dp(arr, n);
	        System.out.println(ans);
	    }
	 }
}

'''