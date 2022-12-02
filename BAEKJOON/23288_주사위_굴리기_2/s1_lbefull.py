from collections import deque


def sol():
    row = deque([4, 1, 3, 6])                               # 주사위 전개도의 가로줄에 아래면인 6을 추가하여 저장
    col = deque([2, 1, 5, 6])                               # 주사위 전개도의 세로줄을 저장
    r = c = d = answer = 0                                  # 전개도 특성상 윗면과 아래면에 해당하는 1번 3번 인덱스 값은 동일해야 함
    for _ in range(K):
        nr = r + dr[d]
        nc = c + dc[d]                                      # 방향 d로 이동한 결과를 nr, nc에 저장
        if nr < 0 or N <= nr or nc < 0 or M <= nc:          # 지도를 벗어나면 반대방향으로 바꿔서 저장
            d = (d + 2) % 4
            nr = r + dr[d]
            nc = c + dc[d]

        if d in {0, 2}:                                     # 주사위가 좌우로 굴러갈 경우 전면과 후면은 바뀌지 않고, 상하좌우는 1칸씩 쉬프트
            row.rotate(-(d - 1))                            # 따라서 전개도의 가로줄을 해당 방향으로 1칸 쉬프트하고
            col[1], col[3] = row[1], row[3]                 # 세로줄의 1, 3번(상하) 칸을 가로줄에 맞게 바꿔줌
        else:                                               # 방향이 위 아래일 경우는 가로줄, 세로줄만 바꿔서 실행
            col.rotate(-(d - 2))
            row[1], row[3] = col[1], col[3]

        r, c = nr, nc
        answer += bfs(r, c)                                 # 해당 칸의 점수를 더해줌
        A = row[3]                                          # 주사위 아래면은 row 또는 col의 마지막 요소
        B = arr[r][c]                                       # 지도의 현재 칸의 번호
        if A > B:                                           # 조건에 맞게 방향을 바꿔줌
            d = (d + 1) % 4
        elif A < B:
            d = (d - 1) % 4

    return answer


def bfs(sr, sc):
    Q = [[sr, sc]]
    visited = [[0] * M for _ in range(N)]                   # BFS 탐색으로 시작칸(sr, sc)과 이어져있는 칸의 개수를 구해줌
    visited[sr][sc] = 1                                     # 칸의 번호와 개수를 곱해서 리턴
    idx = 0
    while idx < len(Q):
        r, c = Q[idx]
        idx += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[sr][sc] == arr[nr][nc]:
                visited[nr][nc] = 1
                Q.append([nr, nc])

    return arr[sr][sc] * len(Q)


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
print(sol())
