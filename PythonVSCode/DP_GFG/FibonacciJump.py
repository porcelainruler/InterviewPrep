# A Dynamic Programming based Python3 program  
# to find minimum number of jumps to reach 
# Destination 
MAX = 1e9
  
# Function that returns the min number  
# of jump to reach the destination 
def minJumps(arr, N): 
      
    # We consider only those Fibonacci 
    # numbers which are less than n, 
    # where we can consider fib[30] 
    # to be the upper bound as this 
    # will cross 10^5 
    fib = [0 for i in range(30)] 
    fib[0] = 0
    fib[1] = 1
    for i in range(2, 30): 
        fib[i] = fib[i - 1] + fib[i - 2] 
  
    # DP[i] will be storing the minimum 
    # number of jumps required for 
    # the position i. So DP[N+1] will 
    # have the result we consider 0 
    # as source and N+1 as the destination 
    DP = [0 for i in range(N + 2)] 
  
    # Base case (Steps to reach source is) 
    DP[0] = 0
  
    # Initialize all table values as Infinite 
    for i in range(1, N + 2): 
        DP[i] = MAX
  
    # Compute minimum jumps required 
    # considering each Fibonacci 
    # numbers one by one. 
  
    # Go through each positions 
    # till destination. 
    for i in range(1, N + 2): 
  
        # Calculate the minimum of that 
        # position if all the Fibonacci 
        # numbers are considered 
        for j in range(1, 30): 
  
            # If the position is safe or the  
            # position is the destination then  
            # only we calculate the minimum 
            # otherwise the cost is MAX as default 
            if ((arr[i - 1] == 1 or i == N + 1) and 
                                    i - fib[j] >= 0): 
                DP[i] = min(DP[i], 1 + DP[i - fib[j]]) 
  
    # -1 denotes if there is 
    # no path possible 
    if (DP[N + 1] != MAX): 
        return DP[N + 1] 
    else: 
        return -1
  
# Driver Code 
arr = [0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0] 
n = len(arr) 
  
print(minJumps(arr, n - 1)) 