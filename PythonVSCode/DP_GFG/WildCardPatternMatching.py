'''

// If current characters match, result is same as 
// result for lengths minus one. Characters match
// in two cases:
// a) If pattern character is '?' then it matches  
//    with any character of text. 
// b) If current characters in both match
if ( pattern[j – 1] == ‘?’) || 
     (pattern[j – 1] == text[i - 1])
    T[i][j] = T[i-1][j-1]   
 
// If we encounter ‘*’, two choices are possible-
// a) We ignore ‘*’ character and move to next 
//    character in the pattern, i.e., ‘*’ 
//    indicates an empty sequence.
// b) '*' character matches with ith character in
//     input 
else if (pattern[j – 1] == ‘*’)
    T[i][j] = T[i][j-1] || T[i-1][j]  

else // if (pattern[j – 1] != text[i - 1])
    T[i][j]  = false 

'''

from sys import stdin

def dp(pattern: str, txt: str, m: int, n: int):
    dp = [[False]*(m+1) for i in range(n+1)]

    dp[0][0] = True

    # Matching '*' with '' from txt
    for i in range(1, m+1):
        if pattern[i-1] == '*':
            dp[0][i] = dp[0][i-1]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if pattern[j-1] == '*':
                # Moving Next Txt(i.e. txt char incl. in * subseq) || Moving Pattern to next (i.e. * equal '')
                dp[i][j] = dp[i-1][j] | dp[i][j-1]
            elif pattern[j-1] == '?' or pattern[j-1] == txt[i-1]:
                # Moving both txt and pattern char
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = False

    # for i in range(n+1):
    #     for j in range(m+1):
    #         print(dp[i][j], end = ' ')
    #     print()
    # print()

    return dp[n][m]

def main():
    t = int(input())

    for i in range(t):
        pattern = list(map(str, stdin.readline().split()))[0]
        txt = list(map(str, stdin.readline().split()))[0]

        ans = dp(pattern, txt, len(pattern), len(txt))
        print(ans)

# 1
# 9 9
# bbabcbcab
# bacbcbabb

if __name__ == '__main__':
    main()

