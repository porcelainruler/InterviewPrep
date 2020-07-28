#code
from sys import stdin;

def knapSackBU(W, wt, val, n): 
    K = [[0 for x in range(W+1)] for x in range(n+1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n+1): 
        for w in range(W+1): 
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
  
    return K[n][W] 

def dp(price, weight, w, idx, n, mapper):
    if(w<=0 or idx >= n):
        return 0;

    key = str(w) + "|" + str(idx);

    if(key in mapper.keys()):
        return mapper[key];

    s1 = 0;
    s2 = 0;

    s1 = dp(price, weight, w, idx + 1, n, mapper);
    if(w >= weight[idx]):
        s2 = dp(price, weight,  w - weight[idx], idx + 1, n, mapper) + price[idx];

    subans = max(s1, s2);
    mapper[key] = subans;
    return subans;

def main():
    t = int(input());

    for i in range(t):
        n = int(input());
        w = int(input());
        price = list(map(int, stdin.readline().split()));
        weight = list(map(int, stdin.readline().split()));

        mapper = dict();

        # ans = dp(price, weight, w, 0, n, mapper);
        ans = knapSackBU(w, weight, price, n)
        print(ans);


if __name__ == "__main__":
    main();