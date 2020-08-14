# dp[i][j] = min(dp[i][j], (sum[i][j] + dp[i][k] + dp[k + 1][j])), for every (i ? k lt; j) 

'''

// Java program for the above approach
import java.util.*;
class GFG{
 
// Function to find the total minimum
// cost of merging two consecutive numbers
static int mergeTwoNumbers(int []numbers)
{
    int len, i, j, k;
 
    // Find the size of numbers[]
    int n = numbers.length;
 
    // If array is empty, return 0
    if (numbers.length == 0)
    {
        return 0;
    }
 
    // To store the prefix Sum of
    // numbers array numbers[]
    int []prefixSum = new int[n + 1];
 
    // Traverse numbers[] to find the
    // prefix sum
    for (i = 1; i <= n; i++) 
    {
        prefixSum[i] = prefixSum[i - 1] +
                         numbers[i - 1];
    }
 
    // dp table to memoised the value
    int [][]dp = new int[n + 1][n + 1];
 
    // Iterate for length >= 1
    for (len = 2; len <= n; len++) 
    {
 
        for (i = 1; i <= n - len + 1; i++)
        {
            j = i + len - 1;
 
            // Find sum in range [i..j]
            int sum = prefixSum[j] - 
                      prefixSum[i - 1];
 
            // Initialise dp[i][j] to Integer.MAX_VALUE
            dp[i][j] = Integer.MAX_VALUE;
 
            // Iterate for all possible
            // K to find the minimum cost
            for (k = i; k < j; k++) 
            {
 
                // Update the minimum sum
                dp[i][j] = Math.min(dp[i][j], 
                                    dp[i][k] +
                                    dp[k + 1][j] + 
                                    sum);
            }
        }
    }
 
    // Return the final minimum cost
    return dp[1][n];
}
 
// Driver Code
public static void main(String[] args)
{
    // Given set of numbers
    int []arr1 = { 6, 4, 4, 6 };
 
    // Function Call
    System.out.print(mergeTwoNumbers(arr1) + "\n");
}
}

'''