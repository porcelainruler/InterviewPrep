def nSquare(arr):
    arr.sort()
    n = len(arr)
    maxEle = 1000000000
    a = -1
    b = -1
    for i in range(0,n-1):
        for j in range(i+1, n-1):
            if max(arr[i]-arr[0], max(arr[j]-arr[i+1], arr[n-1]-arr[j+1])) < maxEle:
                maxEle = max(arr[i]-arr[0], max(arr[j]-arr[i+1], arr[n-1]-arr[j+1]))
                a = i
                b = j
    
    print(maxEle/2)

def nApproach(arr):
    arr.sort()
    n = len(arr)
    i = -1
    j = n-2
    maxEle = 1000000000
    while i <= j and i<len(arr)-2 and j>0:
        if i <= j and i<len(arr)-2 and j>0 and max(arr[i+1]-arr[0], max(arr[j]-arr[i+2], arr[n-1]-arr[j+1])) < maxEle:
            maxEle = max(arr[i+1]-arr[0], max(arr[j]-arr[i+2], arr[n-1]-arr[j+1]))
            i += 1
            print(maxEle, i, j, 'I')
        elif i <= j and i<len(arr)-2 and j>0 and max(arr[i]-arr[0], max(arr[j-1]-arr[i+1], arr[n-1]-arr[j])) < maxEle:
            maxEle = max(arr[i]-arr[0], max(arr[j-1]-arr[i+1], arr[n-1]-arr[j]))
            j -= 1
            print(maxEle, i, j, 'II')
        else:
            break
    
    print(maxEle/2)

arr = [1,90,95,100]

print(nSquare(arr))
print(nApproach(arr))