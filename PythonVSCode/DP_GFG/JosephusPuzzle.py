from sys import stdin

# josephus(n, k) = (josephus(n - 1, k) + k-1) % n + 1
# josephus(1, k) = 1

def dp(n: int, k: int):
    val = 0

    for i in range(1, n+1):
        val = (val+k)%i

    return val + 1


def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, stdin.readline().split())
        
        ans = dp(n, k)
        print(ans)

if __name__ == '__main__':
    main()