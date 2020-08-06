from sys import stdin
import math

def dp(arr: list, m: int, n: int):
    dp = [[0]*n for i in range(m)]

    for i in range(n):
        dp[m-1][i] = arr[m-1][i]
    
    for i in range(m-2, -1, -1):
        for j in range(n):
            a1 = 0
            a2 = 0
            a3 = 0

            if j-1 >= 0 and i+1<m:
                a1 = dp[i+1][j-1]
            
            a2 = dp[i+1][j]

            if j+1 < n and i < m:
                a3 = dp[i+1][j+1]
            
            dp[i][j] = max(a1, max(a2, a3)) + arr[i][j]

    # for i in range(m):
    #     for j in range(n):
    #         print(dp[i][j], end=' ')
    #     print()
    # print()

    maxEle = -math.inf
    for i in range(n):
        if maxEle < dp[0][i]:
            maxEle = dp[0][i] 

    return maxEle 

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        subarr = list(map(int, stdin.readline().split()))
        arr = list()
        for j in range(n):
            arr.append(subarr[j*n: (j+1)*n])
        
        # for i in range(n):
        #     for j in range(n):
        #         print(arr[i][j], end=' ')
        #     print()
        # print()
        
        ans = dp(arr, n, n)
        print(ans)

if __name__ == '__main__':
    main()
# 1
# 11
# 293 794 127 150 156 568 699 817 649 670 819 501 273 816 176 768 60 99 436 766 40 72 511 838 43 664 598 129 540 792 911 185 938 390 334 93 957 384 261 957 405 79 457 678 895 633 797 306 83 585 423 122 8 933 959 50 597 909 530 488 52 440 24 341 829 358 785 786 93 45 94 498 124 551 527 370 535 675 675 617 259 97 738 266 381 49 667 329 957 196 169 360 988 192 701 816 549 485 953 994 530 47 491 5 949 17 374 483 43 48 451 302 496 188 919 876 588 586 557 544 133