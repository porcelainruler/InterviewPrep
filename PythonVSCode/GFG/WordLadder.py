from sys import stdin

sarr = str

def wordLadder(start: str, target: str):
    ans = list()
    

def main():
    t = int(input())

    for i in range(t):
        global sarr
        sarr = list(map(str, stdin.readline().split()))
        start, target = map(str, stdin.radline().split())

        wordLadder(start, target)

if __name__ =='__main__':
    main()