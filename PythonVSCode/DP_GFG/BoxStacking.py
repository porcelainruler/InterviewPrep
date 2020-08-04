# Assumption l>w
from sys import stdin
from operator import attrgetter

class Box:
    def __init__(self, h: int, l: int, w: int):
        super().__init__()
        self.h = h
        self.l = l
        self.w = w
        self.area = w*l
    
    def printer(self):
        print(f'Area: {self.area} - Height: {self.h} - Length: {self.l} - Width: {self.w}')

def dp(boxes: list, n: int):
    dp = [0]*(3*n)
    
    for i in range(3*n):
        dp[i] = boxes[i].h

    for i in range(1, 3*n):
        for j in range(i):
            if boxes[j].l > boxes[i].l and boxes[j].w > boxes[i].w and dp[i] < dp[j] + boxes[i].h:
                dp[i] = dp[j] + boxes[i].h

    return max(dp)

def main():
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = list(map(int, stdin.readline().split()))
        boxes = list()
        for j in range(n):
            h, w, l = arr[j*3 + 0], arr[j*3 + 1], arr[j*3 + 2]

            box1 = Box(h, max(w, l), min(w, l))
            box2 = Box(w, max(h, l), min(h, l))
            box3 = Box(l, max(w, h), min(w, h))

            boxes.append(box1)
            boxes.append(box2)
            boxes.append(box3)
        
        boxes = sorted(boxes, key=attrgetter('area'), reverse=True)
        print(len(boxes))
        ans = dp(boxes, n)
        print(ans)
        # for box in boxes:
        #     box.printer()



if __name__ == '__main__':
    main()


