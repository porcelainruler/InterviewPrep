# Python 3 program to find largest  
# subarray with equal number of  
# 0's and 1's.  
  
# Returns largest subarray with  
# equal number of 0s and 1s  
def maxLen(arr, n):  
  
    # NOTE: Dictonary in python in  
    # implemented as Hash Maps.  
    # Create an empty hash map (dictionary)  
    hash_map = {}   
    curr_sum = 0 
    max_len = 0 
    ending_index = -1 
  
    for i in range (0, n):  
        if(arr[i] == 0):  
            arr[i] = -1 
        else:  
            arr[i] = 1 
  
    # Traverse through the given array  
    for i in range (0, n):  
      
        # Add current element to sum  
        curr_sum = curr_sum + arr[i]  
  
        # To handle sum = 0 at last index  
        if (curr_sum == 0):  
            max_len = i + 1 
            ending_index = i  
  
        # If this sum is seen before,  
        if curr_sum in hash_map: 
              
            # If max_len is smaller than new subarray 
            # Update max_len and ending_index 
            if max_len < i - hash_map[curr_sum]: 
                max_len = i - hash_map[curr_sum] 
                ending_index = i 
        else:  
  
            # else put this sum in dictionary  
            hash_map[curr_sum] = i   
          
    for i in range (0, n):  
        if(arr[i] == -1):  
            arr[i] = 0 
        else:  
            arr[i] = 1 
              
    print (ending_index - max_len + 1, end =" ") 
    print ("to", end = " ") 
    print (ending_index) 
  
    return max_len 
  
# Driver Code  
arr = [1, 0, 0, 1, 0, 1, 1]  
n = len(arr)   
  
maxLen(arr, n)  