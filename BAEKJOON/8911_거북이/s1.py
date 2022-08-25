import sys
input = sys.stdin.readline

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def check():
    global x1, y1, x2, y2
    x1, y1, x2, y2 = min(x1, x), min(y1, y), max(x2, x), max(y2, y)


for tc in range(int(input())):
    coms = input().rstrip()
    x1, y1, x2, y2 = 0, 0, 0, 0
    x, y, idx = 0, 0, 0
    for com in coms:
        if com=='F':
            x, y = x+direct[idx][0], y+direct[idx][1]
            check()

        elif com=='B':
            x, y = x-direct[idx][0], y-direct[idx][1]
            check()

        elif com=='L':
            idx = (idx-1)%4

        elif com=='R':
            idx = (idx+1)%4

    print(abs(x2-x1)*abs(y2-y1))