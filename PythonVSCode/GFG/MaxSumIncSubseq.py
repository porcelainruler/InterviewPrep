from sys import stdin;

# Correct for all commented Test cases but problem with time limit of GFG
# 1
# 42
# 468 335 501 170 725 479 359 963 465 706 146 282 828 962 492 996 943 828 437 392 605 903 154 293 383 422 717 719 896 448 727 772 539 870 913 668 300 36 895 704 812 323
# Ans - { 6974 }

def dp (arr, prev, idx, n, mapper):
    if(idx >= n):
        return 0;

    key = str(idx) + "|" + str(prev);

    if(key in mapper.keys()):
        return mapper[key];

    if(arr[idx] > prev):
        s1 = max(dp(arr, prev, idx + 1, n, mapper), ( dp(arr, arr[idx], idx + 1, n, mapper) + arr[idx] ) );
        mapper[key] = s1;
        return s1;
    else :
        s2 = dp(arr, prev, idx + 1, n, mapper);
        mapper[key] = s2;
        return s2;

def main():
    t = int(input());

    for i in range(t):
        n = int(input());
        arr = list(map(int, stdin.readline().split()));

        mapper = dict()

        ans = dp(arr, -1, 0, n, mapper);
        print(ans);



if __name__ == "__main__":
    main();