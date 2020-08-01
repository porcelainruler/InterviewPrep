from sys import stdin

def sortedWithoutReturn(arr):
    # Code here

    if len(arr) != 0:
        ele = arr.pop()

        sortedWithoutReturn(arr)
        
        addSortedWithoutReturn(arr, ele)


def addSortedWithoutReturn(arr: list, ele: int):

    if len(arr) == 0 or arr[-1] >= ele:
        arr.append(ele)
    else:
        popEle = arr.pop()
        addSortedWithoutReturn(arr, ele)
        arr.append(popEle)



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


def calculateStockSpan(a,n):
    #code here
    stack = list()
    ans = list()
    
    for i in range(n):
        if not stack:
            stack.append(i)
            ans.append(i+1)
            continue
        
        while stack and a[stack[-1]] <= a[i]:
            stack.pop()
        
        span = i+1 if len(stack)<=0 else i-stack[-1]
        ans.append(span)
        stack.append(i)
        
    
    return ans

def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))

        ans = sortStack(arr)
        # ans = reverseStack(arr)
        print(ans)

if __name__ == '__main__':
    main()

