import sys
input = sys.stdin.readline


def check(x, y, d1, d2):
    global ans

    people = [0] * 5
    visited = [[False]*N for _ in range(N)]
    visited[x][y] = True

    whole = 0
    for i in range(N):
        whole += sum(a[i][:])

    # 5번 선거구
    for i in range(1, d1+1):
        visited[x+i][y-i] = True
    for i in range(1, d2+1):
        visited[x+i][y+i] = True
    for i in range(1, d2+1):
        visited[x+d1+i][y-d1+i] = True
    for i in range(1, d1+1):
        visited[x+d2+i][y+d2-i] = True

    # 1번 선거구
    for r in range(x+d1):
        for c in range(y+1):
            if visited[r][c]:
                break
            else:
                people[0] += a[r][c]
    # 2번 선거구
    for r in range(x + d2 + 1):
        for c in range(N-1, y, -1):
            if visited[r][c]:
                break
            else:
                people[1] += a[r][c]
    # 3번 선거구
    for r in range(x + d1, N):
        for c in range(y - d1 + d2):
            if visited[r][c]:
                break
            else:
                people[2] += a[r][c]
    # 4번 선거구
    for r in range(x + d2 + 1, N):
        for c in range(N-1, y - d1 + d2 - 1, -1):
            if visited[r][c]:
                break
            else:
                people[3] += a[r][c]
    # 5번 선거구 인구
    people[4] = whole - sum(people)

    temp = max(people) - min(people)
    ans = temp if temp < ans else ans


N = int(input().rstrip())
a = [list(map(int, input().split())) for _ in range(N)]
ans = float('inf')

for i in range(N-2):
    for j in range(1, N-1):
        d1 = 1
        while i+d1 < N and 0 <= j-d1:
            d2 = 1
            while i+d1+d2 < N and j-d1+d2 < N and i+d2 < N and j+d2 < N:
                check(i, j, d1, d2)
                d2 += 1
            d1 += 1
print(ans)
