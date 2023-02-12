from collections import deque


def solution(maps):
    answer = []
    N = len(maps)
    M = len(maps[0])
    visited = [[0] * M for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(N):                                          # 모든 지역 탐색
        for j in range(M):
            if maps[i][j] == 'X' or visited[i][j]:              # 바다이거나 이미 탐색한 곳이면 다음반복
                continue

            Q = deque([[i, j]])                                 # 아직 탐색하지 않은 무인도 지형이면
            visited[i][j] = 1                                   # Q와 visited 초기화
            cnt = 0                                             # 식량을 표시할 cnt 초기화
            while Q:                                            # BFS 탐색
                r, c = Q.popleft()
                cnt += int(maps[r][c])                          # cnt에 현재 무인도지형의 식량을 모두 더해줌
                for d in range(4):                              # 4방향 중 무인도가 있다면 visited에 표시 후 Q에 enQ
                    nr = r + dr[d]
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and maps[nr][nc] != 'X':
                        visited[nr][nc] = 1
                        Q.append([nr, nc])
            answer.append(cnt)

    answer.sort()                                               # 무인도 별 식량을 오름차순 정렬
    if not answer:                                              # 만약 무인도가 하나도 없다면 -1
        answer.append(-1)

    return answer
