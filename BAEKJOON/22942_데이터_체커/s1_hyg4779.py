from sys import stdin


def main():
    n = int(stdin.readline())

    circles = []
    for _ in range(n):
        x, r = map(int, stdin.readline().split())
        circles.append((x-r, _, True))
        circles.append((x+r, _, False))


    circles.sort()

    stack = []
    crds = set()
    for crd, i, isopen in circles:
        if crd in crds:
            print('NO')
            return
        if isopen:
            stack.append((crd, i))

        elif stack[-1][1] != i:
            print('NO')
            return
        else:
            crds.add(crd)
            stack.pop()

    print('YES')

main()