import sys
input = sys.stdin.readline


def wind(r, c, dr, dc):
    vset = set()
    vset.add((r, c))                                                        # 현재 바람이 이동한 위치를 모두 저장
    nr = r + dr
    nc = c + dc
    while 0 <= nr < N and 0 <= nc < M and (nr, nc) not in vset:             # 한번 바람이 이동한 위치를 다시 방문하거나
        visited[nr][nc] = 1                                                 # 인덱스 범위를 벗어나면 반복 종료
        if arr[nr][nc] == 9: break                                          # 에어컨 위치를 만나면 중복이므로 반복 종료
        if arr[nr][nc]:                                                     # 민상이가 원하는 자리로 표시해주고
            dr, dc = obj[arr[nr][nc] - 1](dr, dc)                           # 물건이 있다면 물건에 따라 바람의 방향을 바꿔주고
        nr = nr + dr                                                        # 새로운 바람이 이동할 좌표를 구해서 반복
        nc = nc + dc


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
obj = [lambda r, c: (r, -c), lambda r, c: (-r, c), lambda r, c: (-c, -r), lambda r, c: (c, r)]

answer = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == 9:                                                  # 에어컨 위치로부터 시작
            visited[r][c] = 1                                               # 에어컨 위치도 바람이 통하므로 1
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:               # 에어컨 위치에서 4방향으로 wind함수 호출
                wind(r, c, dr, dc)

for r in range(N):
    for c in range(M):
        answer += visited[r][c]

print(answer)
