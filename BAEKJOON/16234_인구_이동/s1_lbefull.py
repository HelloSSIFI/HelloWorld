N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

candi = set()                                           # 인구이동 후보 나라 좌표를 저장
for r in range(N):                                      # 처음에는 모든 좌표를 설정
    for c in range(N):
        candi.add((r, c))
answer = -1
while candi:
    new_candi = set()                                   # 새로운 후보군을 저장, 현재 회차에서 이동한 나라들만 다음 회차에서도 이동할 가능성이 있음
    answer += 1
    visited = [[False] * N for _ in range(N)]
    for i, j in candi:
        if visited[i][j]:                               # 현재 회차에서 이미 이동을 했다면 continue
            continue
        
        Q = []
        Q.append([i, j])
        visited[i][j] = True
        sum_pop = A[i][j]

        k = 0
        while k < len(Q):                               # BFS 탐색
            r, c = Q[k]                                 # 이동하지 않은 나라 중 인구차이가 L ~ R 사이에 있는 나라 탐색
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and L <= abs(A[r][c] - A[nr][nc]) <= R:
                    visited[nr][nc] = True
                    Q.append([nr, nc])
                    sum_pop += A[nr][nc]
            k += 1
        
        if len(Q) > 1:                                  # 조건에 해당하는 나라가 2개 이상이라면
            new_pop = sum_pop // len(Q)                 # 새로운 인구로 바꿔주고
            for r, c in Q:                              # 해당 나라의 좌표들을 새로운 후보군에 저장
                A[r][c] = new_pop
                new_candi.add((r, c))
    candi = new_candi                                   # 후보군을 새로운 후보군으로 바꾸고 다시 반복

print(answer)
