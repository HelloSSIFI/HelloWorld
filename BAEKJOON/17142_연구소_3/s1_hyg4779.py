from collections import deque
import sys
input = sys.stdin.readline

# 연구소 크기, 선택할 바이러스 수
n, m = map(int, input().split())

# 바이러스 위치, 연구소, 바이러스 선택 조합을 담는 배열
germs, field, array = [], [], []
count = 0
for i in range(n):
    args = list(map(int, input().split()))
    for j in range(n):
        if args[j] == 2:
            germs.append((i, j))
        if args[j] == 0:
            count += 1

    field.append(args)

if count == 0:
    print(0)
    exit()


# 총 균의 수
k = len(germs)
direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
answer = n*n


def comb(now, s):
    global answer

    if len(now) == m:
        array.append(now)
        return

    for j in range(s, k):
        comb(now+[j], j+1)


for i in range(k-m+1):
    comb([i], i+1)


for arr in array:

    visit = [[-1]*n for _ in range(n)]
    Q = deque([])

    # 선택된 바이러스 visit에서 방문 처리 후 Q에 push
    for idx in arr:
        x, y = germs[idx]
        visit[x][y] = 0
        Q.append((x, y))

    # 최대 이동 거리, 감염한 통로 수
    result, cnt = 0, 0
    while Q:
        # 현재 위치
        r, c = Q.popleft()
        # 현재 이동거리가 answer보다 작으면 bfs 중지

        # 4방향 탐색
        for d in direct:
            nr, nc = r+d[0], c+d[1]
            # 격자 안, 통로 또는 바이러스, 방문한 위칙
            if 0 <= nr < n and 0 <= nc < n and visit[nr][nc]==-1:

                visit[nr][nc] = visit[r][c]+1
                if field[nr][nc] == 0:
                    cnt += 1
                    result = max(result, visit[nr][nc])
                    Q.append((nr, nc))

                elif field[nr][nc] == 2:
                    Q.append((nr, nc))
    if cnt == count:
        answer = min(answer, result)

print(-1 if answer == n*n else answer)