from collections import deque


N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# 아기 상어의 현재 크기, y좌표, x좌표
baby, baby_y, baby_x = 2, 0, 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            baby_y, baby_x = i, j   # 아기 상어 위치
            arr[i][j] = 0   # 아기 상어 시작 위치 빈칸 처리


def bfs():
    visited = [[-1] * N for _ in range(N)]
    q = deque()
    q.append([baby_y, baby_x])    # 시작 위치
    visited[baby_y][baby_x] = 0    # 방문 처리
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()
        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]
            if 0 <= y < N and 0 <= x < N:
                if visited[y][x] == -1 and arr[y][x] <= baby:
                    visited[y][x] = visited[a][b] + 1
                    q.append([y, x])

    return visited


def find(visited):
    y, x, res = 0, 0, 10**9

    for i in range(N):
        for j in range(N):
            # 이동 가능한 위치이면서 먹을 수 있는 물고기 일 때
            if visited[i][j] != -1 and 1 <= arr[i][j] < baby:
                if visited[i][j] < res:
                    y, x = i, j
                    res = visited[i][j]

    if res == 10**9:    # 먹을 수 있는 물고기가 없는 경우
        return None
    else:    # 먹을 수 있는 물고기가 있는 경우 위치와 최단거리
        return y, x, res


answer = 0    # 걸린 시간
eat = 0    # 벌크업 가능한지 체크 (먹은 양이 사이즈와 같아지면 벌크업)

while True:
    # 먹을 수 있는 고기 위치 찾기
    temp = find(bfs())

    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if temp == None:
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        baby_y, baby_x = temp[0], temp[1]
        answer += temp[2]

        # 먹은 위치에는 빈 칸 처리
        arr[baby_y][baby_x] = 0
        eat += 1

        # 벌크업이 가능한 경우
        if eat >= baby:
            baby += 1
            eat = 0

print(answer)