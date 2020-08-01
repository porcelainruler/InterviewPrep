from sys import stdin

def sortStack(arr: list):
    if not arr:
        return list()

    ele = arr.pop()

    arr = sortStack(arr)
    arr = addSorted(arr, ele)

    return arr

def addSorted(arr: list, ele: int):
    if not arr:
        arr.append(ele)
        return arr

    if arr[-1] <= ele:
        arr.append(ele)
    else:
        popEle = arr.pop()
        arr = addSorted(arr, ele)
        arr.append(popEle)

    return arr


def insertBottom(arr: list, ele: int):
    if not arr:
        return [ele]

    popEle = arr.pop()
    arr = insertBottom(arr, ele)
    arr.append(popEle)

    return arr

def reverseStack(arr: list):
    if not arr:
        return list()
    
    ele = arr.pop()
    arr = reverseStack(arr)
    arr = insertBottom(arr, ele)

    return arr

def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))

        # ans = sortStack(arr)
        ans = reverseStack(arr)
        print(ans)

if __name__ == '__main__':
    main()

