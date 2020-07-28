from sys import stdin

def maxRect(arr: list):
    max_area = 0
    temp_area = 0

    curr = 0
    stack = []
    while(curr < len(arr)):
        if ((len(stack) == 0) or (arr[stack[-1]] <= arr[curr])):
            stack.append(curr)
            curr += 1
        else:
            ele = stack.pop()

            temp_area = ((curr - stack[-1] - 1) if stack else curr) * arr[ele]
            max_area = max(max_area, temp_area)
    
    while stack:
        ele = stack.pop()

        temp_area = ((curr - stack[-1] - 1) if stack else curr) * arr[ele]
        max_area = max(max_area, temp_area)

    return max_area

def main():
    t = int(input())

    for i in range(t):
        arr = list(map(int, stdin.readline().split()))

        print(maxRect(arr))

    return 0

if __name__ == '__main__':
    main()

# hist = [6, 2, 5, 4, 5, 1, 6] 