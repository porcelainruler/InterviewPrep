# Assumption l>w
from sys import stdin
from operator import attrgetter

class Pair:
    def __init__(self, a: int, b: int):
        super().__init__()
        self.a = a
        self.b = b
    
    # def printer(self):
    #     print(f'a: {self.a} - b: {self.b}')

def dp(pairs: list, n: int):
    dp = [0]*n
    
    for i in range(n):
        dp[i] = 1

    for i in range(1, n):
        for j in range(i):
            if pairs[j].b < pairs[i].a and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1

    return max(dp)

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        pairs = list()
        for j in range(n):
            a, b= arr[j*2 + 0], arr[j*2 + 1]

            pair = Pair(min(a, b), max(a, b))

            pairs.append(pair)
        
        pairs = sorted(pairs, key=attrgetter('a'))

        # for pair in pairs:
        #     pair.printer()

        ans = dp(pairs, n)
        print(ans)


if __name__ == '__main__':
    main()


