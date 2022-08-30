import sys
input = sys.stdin.readline


n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

for i in range(k):
    a, b, s, d, z = map(int, input().split())
    arr[a-1][b-1] = (s, d, z)


ans = 0
for j in range(m):

    for i in range(n):
        if arr[i][j]:
            ans += arr[i][j][2]
            arr[i][j] = 0
            break


    new = [[0]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c]:

                tmp, direct, size = arr[r][c]
                nr, nc = r, c
                speed = tmp

                if direct == 1 or direct == 2:
                    rot = 2*(n-1)
                    if direct == 1:
                        tmp += rot-r
                    else:
                        tmp += r

                    tmp %= rot

                    if tmp >= n:
                        nr, nc, direct = rot-tmp, nc, 1
                    else:
                        nr, nc, direct = tmp, nc, 2

                else:
                    rot = 2*(m-1)
                    if direct == 4:
                        tmp += rot-c
                    else:
                        tmp += c

                    tmp %= rot

                    if tmp >= m:
                        nr, nc, direct = r, rot-tmp, 4
                    else:
                        nr, nc, direct = r, tmp, 3



                if new[nr][nc]:
                    new[nr][nc] = max(new[nr][nc], (speed, direct, size), key=lambda x: x[2])
                else:
                    new[nr][nc] = (speed, direct, size)

    arr = new

print(ans)