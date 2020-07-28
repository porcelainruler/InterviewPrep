from sys import stdin;

def dp(n, step, mapper):
    if(step > n):
        return 0;
    
    if(n == step):
        return 1;

    key = str(n) + "|" + str(step);

    if(key in mapper.keys()):
        return mapper[key];

    a1 = dp(n, step + 1, mapper);
    a2 = dp(n, step + 2, mapper);
    a3 = dp(n, step + 3, mapper);

    mapper[key] = a1 + a2 + a3;

    return a1 + a2 + a3;
    
def bottomUpSol(n):    
    dp[n+1];
    dp[0]=1;dp[1]=1;
    dp[2]=2;

    for i in range(3, n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3];
    return dp[n];

def main():
    t = int(input());

    for i in range(t):
        n = int(input());
        mapper = dict();
        ans = dp(n, 0, mapper);
        print(ans);


if __name__ == "__main__":
    main();