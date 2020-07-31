from sys import stdin
import math

def prefix(arr):
    ans = list()
    ans.append(arr[0])

    for i in range(1, len(arr)):
        ans.append(max(0, ans[-1] + arr[i]))

    return ans

def prefix_sum(prefix, sidx, eidx):
    return prefix[eidx] - prefix[sidx]

def sum(arr, sidx, eidx):
    sum = 0
    for i in range(sidx, eidx+1):
        sum += arr[i]

    return sum

def partition(arr, n, k):
    if k == 1:
        return sum(arr, 0, n-1)
    
    if n == 1:
        return arr[0]
    minPart = math.inf

    for i in range(1, n+1):
        minPart = min(minPart, max(partition(arr, i, k-1), sum(arr, i, n-1)))
    
    return minPart

def main():
    t = int(input())

    for i in range(t):
        k = int(input())
        arr = list(map(int, stdin.readline().split()))

        prefix = prefix(arr)

        partition(arr, 0, k)

if __name__ == '__main__':
    main()