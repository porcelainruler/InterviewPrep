# Python3 program to count number of  
# substrings with exactly k distinct  
# characters in a given string 
  
# Function to count number of substrings  
# with exactly k unique characters  
def countkDist(str1, k): 
    n = len(str1) 
      
    # Initialize result 
    res = 0
  
    # To store count of characters from  
    # 'a' to 'z'  
    cnt = [0] * 27
  
    # Consider all substrings beginning  
    # with str[i]  
    for i in range(0, n): 
        dist_count = 0
  
        # Initializing array with 0  
        cnt = [0] * 27
  
        # Consider all substrings between str[i..j]  
        for j in range(i, n): 
              
            # If this is a new character for this  
            # substring, increment dist_count.  
            if(cnt[ord(str1[j]) - 97] == 0): 
                dist_count += 1
  
            # Increment count of current character 
            cnt[ord(str1[j]) - 97] += 1
  
            # If distinct character count becomes k,  
            # then increment result. 
            if(dist_count == k): 
                res += 1
            if(dist_count > k): 
                break
  
    return res      
  
# Driver Code 
if __name__ == "__main__": 
    str1 = "abcbaa"
    k = 3
    print("Total substrings with exactly", k,  
           "distinct characters : ", end = "") 
    print(countkDist(str1, k))