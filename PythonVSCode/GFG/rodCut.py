import sys;
from sys import stdin;

def dp(arr, n, mapper):
    if(n <= 0):
        return 0;
    max_val = -sys.maxsize-1;
    
    key = "-" + str(n) + "-";

    if(key in mapper.keys()):
        return mapper[key];

    for i in range(n):
        max_val = max(max_val, dp(arr, n-i-1, mapper) + arr[i]);

    mapper[key] = max_val;
    return max_val;

def main():
    t = int(input());
    
    for i in range(t):
        n = int(input());
        arr = list(map(int, stdin.readline().split()));

        mapper = dict();
        ans = dp(arr, n, mapper);
        print(ans);

if __name__ == "__main__":
    main();