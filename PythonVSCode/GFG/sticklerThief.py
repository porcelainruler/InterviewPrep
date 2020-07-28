from sys import stdin;

# To Think Further
def dp(arr, idx, n, flag, mapper):
    if(idx >= n):
        return 0;

    key = str(idx) + "|" + str(n);

    if(key in mapper.keys()):
        return mapper[key];

    s1 = 0;
    s2 = 0;
    if(flag):
        s1 = dp(arr, idx + 1,  n, False, mapper);
    else:
        s2 = max(dp(arr, idx + 1,  n, True, mapper) + arr[idx], dp(arr, idx + 1,  n, False, mapper));

    subans = max(s1, s2);
    mapper[key] = subans;
    return subans;
'''
def dpBU_Nspace(arr):
    dp = [0] * (len(arr) + 1);
    dp[0] = 0;
    dp[1] = arr[0];

    for i in range(2, len(arr)+1):
        dp[i] = max(dp[i-2] + arr[i-1], dp[i-1]);

    return dp[len(arr)];
'''
def dpBU_Cspace(arr):
    one = 0;
    two = arr[0];
    three = 0;
    for i in range(2, len(arr)+1):
        three = max(one + arr[i-1], two);
        one = two;
        two = three;

    return three;

def main():
    t = int(input());
    
    for i in range(t):
        n = int(input());

        arr = list(map(int, stdin.readline().split()));
        mapper = dict();

        #ans = dp(arr, 0, n, False, mapper);
        #ans = dpBU_Nspace(arr);
        ans = dpBU_Cspace(arr);
        print(ans);

if __name__ == "__main__":
    main();