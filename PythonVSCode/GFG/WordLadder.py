from sys import stdin

sarr = list()

def condCheck(st: str, tr: str):
    count = 0
    if len(st) != len(tr):
        return False
    for i in range(len(st)):
        if count > 1:
            return False

        if st[i] != tr[i]:
            count += 1
    
    if count == 1:
        return True
    else:
        return False

def wordLadder(start: str, target: str):
    global sarr
    stack = list()
    ans = list()

    stack.append(start)
    ans.append(start)

    chainLen = 0

    while stack:
        st = stack[0]
        stack.remove(stack[0])

        if st == target:
            return chainLen + 1

        i = 0
        while i < len(sarr):
            tr = sarr[i]

            if condCheck(st, tr):
                sarr.remove(tr)
                stack.append(tr)
                chainLen += 1
            i += 1 

    return chainLen
    

def main():
    t = int(input())

    for i in range(t):
        global sarr
        sarr = list(map(str, stdin.readline().split()))
        start, target = map(str, stdin.readline().split())

        ans = wordLadder(start, target)
        print(ans)

if __name__ =='__main__':
    main()

'''
1
poon plee same poie plie poin plea
toon plea                 {st-tr}
'''