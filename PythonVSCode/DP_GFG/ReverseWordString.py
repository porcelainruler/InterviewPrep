from sys import stdin

def main():
    t = int(input())

    for i in range(t):
        sarr = list(map(str, stdin.readline().split()))[0]

        sarray = sarr.split('.')

        for i in range(len(sarray)-1):
            print(sarray[len(sarray) - i - 1], end='.')
        print(sarray[0])

if __name__ == '__main__':
    main()