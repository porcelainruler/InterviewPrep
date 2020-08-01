from sys import stdin
import math

def minJumps(arr: list, idx: int, maper: dict):
    if idx >= len(arr) - 1:
        return 0

    key = str(idx)
    if maper.get(key) != None:
        return maper.get(key)

    val = arr[idx]

    jumps = math.inf
    for i in range(1, val+1):
        if idx + i < len(arr):
            jumps = min(jumps, minJumps(arr, idx+i, maper)) + 1

    maper[key] = jumps
    return jumps


def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))
        maper = dict()

        ans = minJumps(arr, 0, maper)
        print(ans)

if __name__ == '__main__':
    main()