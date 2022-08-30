import sys
input = sys.stdin.readline


def spread():
    global a

    arr = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if a[i][j] > 0:
                temp = 0
                for d in di:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < R and 0 <= nj < C and a[ni][nj] != -1:
                        amount = a[i][j] // 5
                        arr[ni][nj] += amount
                        temp += amount
                a[i][j] -= temp

    for i in range(R):
        for j in range(C):
            a[i][j] += arr[i][j]


def activate(acs):
    global a

    for (i, j) in acs:
        r, c = i, j + 1
        pre = 0
        d_idx = 0
        while True:
            nr, nc = r + di[d_idx][0], c + di[d_idx][1]
            if (r, c) in acs:
                break

            if 0 <= nr < R and 0 <= nc < C:
                pass
            else:
                # 윗 바람
                if a[i+1][j] == -1:
                    d_idx += 1
                # 아랫 바람
                elif a[i - 1][j] == -1:
                    d_idx = (d_idx - 1) % 4
                nr, nc = r + di[d_idx][0], c + di[d_idx][1]
            a[r][c], pre = pre, a[r][c]
            r, c = nr, nc


R, C, T = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(R)]
ac = []
di = [(0, 1), (1, 0), (0, -1), (-1, 0)]     # 우 상 좌 하
ans = 0


for t in range(T):
    for i in range(R):
        for j in range(C):
            if t == 0 and a[i][j] == -1:
                ac.append((i, j))
    spread()
    activate(ac)

for r in range(R):
    for c in range(C):
        if a[r][c] > 0:
            ans += a[r][c]

print(ans)