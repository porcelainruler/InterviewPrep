# Python 3 implementation of the above approach 
from math import sqrt 
  
# Function to check whether a string 
# is a prime number or not 
def checkPrime(number): 
    if(len(number) == 0): 
        return True
    num = int(number) 
    for i in range(2,int(sqrt(num)) + 1, 1): 
        if ((num % i) == 0): 
            return False
    return True
  
# A function to find the minimum 
# number of segments the given string 
# can be divided such that every 
# segment is a prime 
def splitIntoPrimes(number): 
    numLen = len(number) 
  
    # Declare a splitdp[] array 
    # and initialize to -1 
    splitDP = [-1 for i in range(numLen + 1)] 
  
    # Build the DP table in 
    # a bottom-up manner 
    for i in range(1, numLen + 1, 1): 
  
        # Initially Check if the entire prefix is Prime 
        if (i <= 6 and checkPrime(number[0:i])): 
            splitDP[i] = 1
  
        # If the Given Prefix can be split into Primes 
        # then for the remaining string from i to j 
        # Check if Prime. If yes calculate 
        # the minimum split till j 
        if (splitDP[i] != -1): 
            j = 1
            while(j <= 6 and i + j <= numLen): 
  
                # To check if the substring from i to j 
                # is a prime number or not 
                if (checkPrime(number[i:i+j])): 
  
                    # If it is a prime, then update the dp array 
                    if (splitDP[i + j] == -1): 
                        splitDP[i + j] = 1 + splitDP[i] 
                    else: 
                        splitDP[i + j] = min(splitDP[i + j], 1 + splitDP[i]) 
                j += 1
  
    # Return the minimum number of splits 
    # for the entire string 
    return splitDP[numLen] 
  
# Driver code 
if __name__ == '__main__': 
    print(splitIntoPrimes("13499315")) 
    print(splitIntoPrimes("43")) 