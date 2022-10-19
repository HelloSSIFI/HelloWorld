import sys
input = sys.stdin.readline


def rot(r, c, m):                                                   # r, c 부터 m 칸의 구역을 시계방향으로 회전시키는 함수
    a = [[0] * m for _ in range(m)]                                 # 회전을 저장할 임시 변수
    for i in range(m):
        for j in range(m):
            a[i][j] = A[r + m - 1 - j][c + i]                       # 시계방향 회전한 값을 저장

    for i in range(m):
        for j in range(m):
            A[r + i][c + j] = a[i][j]                               # A 리스트도 갱신


def is_adj3(r, c):                                                  # r, c의 주변에 얼음이 3칸 있는지 확인하는 함수
    cnt = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < n and A[nr][nc]:               # 칸이 인덱스 범위 내에 있고 얼음이 있다면
            cnt += 1                                                # 개수 카운트

    if cnt < 3:                                                     # 3개보다 적다면 False
        return False                                                # 3개 이상이면 True
    else:
        return True


def bfs(i, j):                                                      # 얼음 덩어리 크기를 구하는 함수
    global lump_ice
    que = [(i, j)]                                                  # 시작점을 큐에 넣어주고
    visited[i][j] = 1                                               # 방문 표시
    idx = 0
    while idx < len(que):                                           # BFS 탐색 후
        r, c = que[idx]                                             # 크기가 크면 갱신해줌
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and A[nr][nc]:
                que.append((nr, nc))
                visited[nr][nc] = 1
        idx += 1
    lump_ice = max(lump_ice, len(que))


N, Q = map(int, input().split())
n = 2 ** N
A = [list(map(int, input().split())) for _ in range(n)]
L = list(map(int, input().split()))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

sum_ice = 0                                             # 얼음의 합
lump_ice = 0                                            # 최대 얼음 덩어리
for l in L:
    m = 2 ** l
    for r in range(0, n, m):                            # 격자를 단계 L로 나눈 후
        for c in range(0, n, m):                        # 시계방향으로 회전
            rot(r, c, m)

    target = []
    for r in range(n):
        for c in range(n):                              # 격자 순회
            if not A[r][c] or is_adj3(r, c):            # 현재 칸에 얼음이 없거나 주변 3칸에 얼음이 있으면
                continue                                # 넘어가고
            target.append((r, c))                       # 그렇지 않다면 target에 추가

    for r, c in target:                                 # target의 좌표들은 모두 -1
        A[r][c] -= 1

visited = [[0] * n for _ in range(n)]
for r in range(n):
    sum_ice += sum(A[r])                                # 얼음을 모두 더해줌
    for c in range(n):
        if not visited[r][c] and A[r][c]:               # 얼음 덩어리 크기를 구하기 위해
            bfs(r, c)                                   # BFS

print(sum_ice)
print(lump_ice)
