from sys import stdin, stdout;

def basic_magic_num(n):
    compute = [];

    idx_2 = 0;
    idx_3 = 0;
    idx_5 = 0;

    num = 1;
    for i in range(n+1):
        ans = 1;
        # to do
    return ans;

# C(n+1) = summation( C(i)*C(n) )   N^2 Approach
def cantalan_num_nsq(n):
    dp = [];

    for i in range(n+2):
        dp.append(0);

    dp[0] = 1;
    dp[1] = 1;
    for i in range(2,n):
        dp[i] = 1;
        for j in range(i):
            dp[i] += dp[j]*dp[n-j-1];

    return dp[n-1];

def binomial_coeff(n, k):
    if(k < n-k):
        k = n-k;

    res = 1;

    for i in range(k):
        res *= (n-i);
        res /= (i+1);

    return res;

# C(n) = C(2n, n)/(n+1)     where C(2n, n) is binomial coefficient  Check Correctness
def cantalon_num_n(n):

    temp = binomial_coeff( 2*(n-1), (n-1));
    print(temp)
    return temp/(n-1);


def main() :

    print(cantalan_num_nsq(4));

    print(cantalon_num_n(4));


if __name__ == "__main__" :
    main();