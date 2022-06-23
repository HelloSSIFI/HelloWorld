from collections import deque

N = int(input())

house = [list(map(int, input())) for _ in range(N)]

result = []

# 상하좌우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(i, j):
    q = deque()
    q.append([i, j])
    house[i][j] = 0    # 현재 위치 0 => 중복 탐색 하지 않게 하기 위함
    cnt = 1    # 연결된 집 카운트

    while q:
        now = q.popleft()

        for i in range(4):
            y = now[0] + dy[i]
            x = now[1] + dx[i]

            if 0 <= x < N and 0 <= y < N and house[y][x] == 1:
                house[y][x] = 0    # 중복 탐색 방지
                q.append([y, x])    # q에 추가
                cnt += 1    # 집 카운트

    return cnt

# 집 있는 곳 찾기
for i in range(N):
    for j in range(N):
        if house[i][j]:
            result.append(bfs(i, j))    # 집 있다면 bfs 연결된 집 모임 갯수 찾은 후 result에 추가

result.sort()

print(len(result))

for i in result:
    print(i)

