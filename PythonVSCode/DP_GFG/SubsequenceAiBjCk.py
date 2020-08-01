# i, j, k >= 1

# Python 3 program to count  
# subsequences of the form 
# a ^ i b ^ j c ^ k 
  
# Returns count of subsequences  
# of the form a ^ i b ^ j c ^ k 
def countSubsequences(s): 
  
    # Initialize counts of different  
    # subsequences caused by different 
    # combination of 'a' 
    aCount = 0
  
    # Initialize counts of different  
    # subsequences caused by different  
    # combination of 'a' and different 
    # combination of 'b' 
    bCount = 0
  
    # Initialize counts of different 
    # subsequences caused by different  
    # combination of 'a', 'b' and 'c'. 
    cCount = 0
  
    # Traverse all characters 
    # of given string 
    for i in range(len(s)): 
      
        # If current character is 'a',  
        # then there are following 
        # possibilities : 
        # a) Current character begins  
        # a new subsequence. 
        # b) Current character is part  
        # of aCount subsequences. 
        # c) Current character is not  
        # part of aCount subsequences.  
        if (s[i] == 'a'): 
            aCount = (1 + 2 * aCount) 
  
        # If current character is 'b', then 
        # there are following possibilities : 
        # a) Current character begins a  
        # new subsequence of b's with  
        # aCount subsequences. 
        # b) Current character is part  
        # of bCount subsequences. 
        # c) Current character is not  
        # part of bCount subsequences.  
        elif (s[i] == 'b'): 
            bCount = (aCount + 2 * bCount) 
  
        # If current character is 'c', then 
        # there are following possibilities : 
        # a) Current character begins a  
        # new subsequence of c's with  
        # bCount subsequences. 
        # b) Current character is part  
        # of cCount subsequences. 
        # c) Current character is not  
        # part of cCount subsequences.  
        elif (s[i] == 'c'): 
            cCount = (bCount + 2 * cCount) 
  
    return cCount 
  
# Driver code 
if __name__ == "__main__": 
    s = "abbc"
    print(countSubsequences(s)) 



'''
#code
from sys import stdin

def dp(sarr: str):
    a = 0
    b = 0
    c = 0
    
    for i in range(len(sarr)):
        if sarr[i] == 'a':
            a = 1 + 2*a
        
        if sarr[i] == 'b':
            b = a + 2*b
            
        if sarr[i] == 'c':
            c = b + 2*c
    
    return c
        

def main():
    t = int(input())
    
    for i in range(t):
        sarr = str(stdin.readline())
        ans = dp(sarr)
        print(ans)

if __name__ == '__main__':
    main()
'''