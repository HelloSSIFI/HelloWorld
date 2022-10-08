from collections import deque
n, m, t = map(int, input().split())

direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

count = n*m
answer = 0
circles = []
for _ in range(n):
    arr = list(map(int, input().split()))
    answer += sum(arr)
    circles.append(arr)


def search(r, c):
    # 현재 숫자
    now = circles[r][c]
    # 지운 숫자가 있는지 체크
    cnt = 0

    # 인접한 것이 있었는지 체크
    Q = deque([(r, c)])
    while Q:
        r, c = Q.popleft()
        cnt += 1

        # 4방향 탐색
        for dir in direct:
            nr = r+dir[0]
            nc = (c+dir[1])%m
            # 인접한 격자 안이고, 방문한 곳이 아닐 때, 현재 숫자와 같은 숫자라면
            if 0 <= nr < n and visit[nr][nc] == 0 and circles[nr][nc] == now:

                # 인접한 숫자 x 및 방문 처리
                circles[nr][nc], visit[nr][nc] = 'x', 1
                Q.append((nr, nc))

    return cnt


for _ in range(t):
    x, d, k = map(int, input().split())

    for num in range(x, n+1, x):
        # 반시계 방향일 때
        line = deque(circles[num-1])
        if d:
            line.rotate(-k)
        # 시계 방향일 때
        else:
            line.rotate(k)
        circles[num-1] = list(line)

    # 인접하고, 같은 숫자 제거
    visit = [[0]*m for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(m):
            if visit[i][j] or circles[i][j] == 'x': continue
            # 방문 처리
            visit[i][j] = 1
            # 인접한 같은 숫자가 있으면
            res = search(i, j)

            if res != 1:
                answer -= res*circles[i][j]
                circles[i][j] = 'x'
                count -= res
                flag = True

    # 숫자를 제거한 적이 있다면
    if not flag:
        if count:
            tmp = answer/count
            new = 0
            for i in range(n):
                for j in range(m):
                    if circles[i][j] == 'x':continue
                    # 평균 보다 작다면
                    if circles[i][j] < tmp: circles[i][j] += 1
                    # 평균 보다 크다면
                    elif circles[i][j] > tmp: circles[i][j] -= 1
                    # 총 합 값 갱신
                    new += circles[i][j]


            answer = new

# for row in circles:
#     print(*row)

print(answer)
