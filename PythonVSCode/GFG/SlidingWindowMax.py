from sys import stdin
from collections import deque 

def kMaxElement(arr: list, k: int):
    dq = deque()

    for i in range(k):
        if len(dq) == 0:
            dq.append(i)
        else:
            while(dq and arr[dq[-1]] <= arr[i]):
                dq.pop()
            
            dq.append(i)

    print(arr[dq[0]], end = ' ')

    for i in range(k, len(arr)):
        while(dq and (i-dq[0]) >= k):
            dq.popleft()

        while(dq and arr[dq[-1]] <= arr[i]):
            dq.pop()
        
        dq.append(i)
        print(arr[dq[0]], end = ' ')

    return 0

def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))
        k = int(input())

        kMaxElement(arr, k)


if __name__ == '__main__':
    main()

# arr = [12, 1, 78, 90, 57, 89, 56]