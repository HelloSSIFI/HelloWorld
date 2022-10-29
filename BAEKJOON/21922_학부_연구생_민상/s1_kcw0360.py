from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 9:    # 에어컨 위치
            q.append([i, j])
            visited[i][j] = 1    # 에어컨 자리에도 앉을 수 있다.

dy = [-1, 1, 0, 0]    # 상, 하, 좌, 우
dx = [0, 0, -1, 1]

while q:
    y, x = q.popleft()
    for k in range(4):
        a, b = dy[k], dx[k]
        ny, nx = y + a, x + b
        while 0 <= ny < N and 0 <= nx < M:    # 에어컨 바람이 더 이상 진행 할 수 없을때 까지 반복
            visited[ny][nx] = 1
            if arr[ny][nx] == 9:
                break    # 에어컨 위치에서는 바람이 생겨나기 때문에 더이상 체크x
            if arr[ny][nx] == 3:
                a, b = -b, -a
            elif arr[ny][nx] == 4:
                a, b = b, a
            elif (arr[ny][nx] == 1 and a == 0) or (arr[ny][nx] == 2 and b == 0):
                break    # 지나왔던 곳 반복이끼 때문에 반복문 종료
            ny += a
            nx += b

answer = 0
for i in range(N):
    answer += sum(visited[i])

print(answer)