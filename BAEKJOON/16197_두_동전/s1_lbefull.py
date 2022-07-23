from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
Q = deque()

start = []                                          # 동전이 있는 두 위치를 저장
for r in range(N):
    for c in range(M):
        if arr[r][c] == 'o':
            start.append(r)
            start.append(c)

start.append(0)                                     # 두 위에 추가로 이동횟수를 넣어 Q에 enQ
Q.append(start)

while Q:                                            # BFS 탐색
    r1, c1, r2, c2, cnt = Q.popleft()

    for d in range(4):
        nr1, nc1 = r1 + dr[d], c1 + dc[d]
        nr2, nc2 = r2 + dr[d], c2 + dc[d]

        if (nr1 == -1 or nr1 == N or nc1 == -1 or nc1 == M) and (0 <= nr2 < N and 0 <= nc2 < M):        # 하나의 동전만 떨어질 경우 이동횟수를 출력
            print(cnt + 1)
            exit()
        if (nr2 == -1 or nr2 == N or nc2 == -1 or nc2 == M) and (0 <= nr1 < N and 0 <= nc1 < M):
            print(cnt + 1)
            exit()
        
        if (0 <= nr1 < N and 0 <= nr2 < N and 0 <= nc1 < M and 0 <= nc2 < M):                           # 두 동전 모두 안떨어질 경우
            if cnt + 1 < 10:                                                                            # 이동횟수가 10을 넘지 않도록 새로운 위치를 저장
                if arr[nr1][nc1] == '#' and arr[nr2][nc2] != '#':                                       # 벽이라면 이동 전 위치를,
                    Q.append((r1, c1, nr2, nc2, cnt + 1))                                               # 벽이 아니라면 움직인 위치를 Q에 enQ
                elif arr[nr1][nc1] != '#' and arr[nr2][nc2] == '#':
                    Q.append((nr1, nc1, r2, c2, cnt + 1))
                elif arr[nr1][nc1] != '#' and arr[nr2][nc2] != '#':
                    Q.append((nr1, nc1, nr2, nc2, cnt + 1))
else:                                                                                                   # 10번을 넘거나 움직일 장소가 더 이상 없다면
    print(-1)                                                                                           # -1 출력
