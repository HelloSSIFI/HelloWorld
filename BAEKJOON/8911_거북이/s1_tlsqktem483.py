import sys
input = sys.stdin.readline

n = int(input())
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for i in range(n):
    i, j, d = 0, 0, 0
    move = list(input())
    post = [(i, j)]

    for m in move:
        if m == 'F':
            i = i + di[d][0]
            j = j + di[d][1]
        elif m == 'B':
            i = i - di[d][0]
            j = j - di[d][1]
        elif m == 'L':
            if d == 3:
                d = 0
            else:
                d += 1
        elif m == 'R':
            if d == 0:
                d = 3
            else:
                d -= 1
        post.append((i, j))

    w = max(post, key=lambda x: x[0])[0] - min(post, key=lambda x: x[0])[0]
    h = max(post, key=lambda x: x[1])[1] - min(post, key=lambda x: x[1])[1]
    print(w * h)