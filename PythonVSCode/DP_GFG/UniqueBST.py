from sys import stdin


# C(n+1) = summation( C(i)*C(n) )   N^2 Approach
def cantalan_num_nsq(n):
    dp = []

    dp = [0]*(n+1)

    dp[0] = 1
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = 1
        for j in range(i+1):
            dp[i] += dp[j-1]*dp[i-j]

    return dp[n]

def binomial_coeff(n, k):
    if(k < n-k):
        k = n-k

    res = 1

    for i in range(k):
        res *= (n-i)
        res = res//(i+1)

    return res

# C(n) = C(2n, n)/(n+1)     where C(2n, n) is binomial coefficient  Check Correctness
def cantalon_num_n(n):

    temp = binomial_coeff( 2*n, n)
    return temp//(n+1)


def main() :
    t = int(input())

    for i in range(t):
        n = int(input())

        print(cantalon_num_n(n))


if __name__ == "__main__" :
    main()