from sys import stdin
import math

def minJumps(arr: list, idx: int):
    if idx >= len(arr) - 1:
        return 0

    val = arr[idx]

    jumps = math.inf
    for i in range(1, val+1):
        if idx + i < len(arr):
            jumps = min(jumps, minJumps(arr, idx+i)) + 1

    return jumps


def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))

        ans = minJumps(arr, 0)
        print(ans)

if __name__ == '__main__':
    main()