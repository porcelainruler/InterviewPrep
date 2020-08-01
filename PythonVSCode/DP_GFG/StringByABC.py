# Atmost 1b 2c
# Cases:   (Total Length - n)
# 1. ALL a 0b 0c
# 2. All a 1b
# 3. All a 1c
# 4. All a 1b 1c
# 5. All a 1b 2c
# 6. All a 2c
from sys import stdin

def dp(n: int):
    ans = 0

    # Case-1
    ans += 1

    # Case-2
    ans += n
    
    # Case-3
    ans += n
    
    # Case-4
    if n >= 2:
        ans += n*(n-1)

    # Case-5
    if n >= 3:
        ans += (n*(n-1)*(n-2))//2

    # Case-6
    if n>= 2:
        ans += (n*(n-1))//2

    return ans

def main():
    t = int(input())

    for i in range(t):
        n = int(input())

        ans = dp(n)
        print(ans)

if __name__ == '__main__':
    main()