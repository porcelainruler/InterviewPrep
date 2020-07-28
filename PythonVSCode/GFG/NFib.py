from sys import stdin;

def main():
    t = int(input());

    for j in range(t):
        n = int(input());

        f = 0;
        s = 1;
        t = f + s;

        for i in range(n):
            t = f + s
            f = s;
            s = t
            print(f, end = " ");
        print()

if __name__ == "__main__":
    main();