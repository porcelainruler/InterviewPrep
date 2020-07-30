from sys import stdin

arr = list()

# Applying DFS
def numIsland():
    global arr
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                dfs(i, j)
                count += 1

    return count

def dfs(m: int, n: int):
    global arr
    if m >= len(arr) or n >= len(arr[0]):
        return

    if arr[m][n] == 0:
        return
    
    if arr[m][n] == 1:
        arr[m][n] = 0
    
    dfs(m+1, n)
    dfs(m, n+1)


def main():
    t = int(input())

    for i in range(t):
        global arr
        arr = list()

        m, n = map(int, stdin.readline().split())

        for j in range(m):
            arr_sub = list(map(int, stdin.readline().split()))
            arr.append(arr_sub)

        print(numIsland())
    
    exit(0)

if __name__ == '__main__':
    main()