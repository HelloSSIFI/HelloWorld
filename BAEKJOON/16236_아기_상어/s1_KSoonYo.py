import sys
from collections import deque
input = sys.stdin.readline

def get_fish(N, zone, t, shark, shark_size, candidates):
    # 현재 상어가 잡아먹을 수 있는 물고기 위치 탐색 후 먹기
    # 거리가 최소인 물고기들 중 가장 위쪽, 왼쪽에 있는 물고기를 먹는다.
    # 상어가 자신의 원래 크기만큼의 물고기 n마리를 먹었다면 사이즈 업
    # 현재 상어가 공간 상에서 먹을 수 있는 물고기 후보군 갱신
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    checked = [[False] * N for _ in range(N)]
    r, c, catched = shark
    q = deque([(r, c, 0)])                          # (r, c, 거리)
    checked[r][c] = True
    possible = []
    while q:
        hr, hc, ht = q.popleft()

        for d in dirs:
            nr = hr + d[0]
            nc = hc + d[1]
            if 0 <= nr < N and 0 <= nc < N and not checked[nr][nc] and zone[nr][nc] <= shark_size:
                checked[nr][nc] = True
                if 0 < zone[nr][nc] < shark_size:
                    possible.append((nr, nc, ht + 1))        # (물고기 위치 r, c, 그곳까지 가는 데 걸리는 시간 t) 
                q.append((nr, nc, ht + 1))

    # 가능한 물고기가 없다면 return
    # 현재 자신이 갈 수 있는 경로 주위로 자신보다 크거나 같은 물고기만 있는 경우 
    if not possible:
        return shark, shark_size, 0, t
    
    possible.sort(key=lambda x : (x[2], x[0], x[1]))        # 가능한 물고기들 중 가까운, 가장 위, 왼쪽에 있는 순으로 정렬
    fr, fc, ft = possible[0]                                # 0번째 인덱스 물고기가 target
    zone[r][c] = 0                                          # 상어가 있던 곳은 빈칸으로
    zone[fr][fc] = 9                                        # 이동
    catched += 1
    if catched == shark_size:
        shark_size += 1
        catched = 0

    # 현재 상어 사이즈로 공간 상에서 먹을 수 있는 물고기 탐색
    temp_candidates = 0
    for i in range(N):
        for j in range(N):
            if zone[i][j] != 9 and 0 < zone[i][j] < shark_size:
                temp_candidates += 1 
    
    candidates = temp_candidates
    shark = (fr, fc, catched)
    nt = t + ft
    return  shark, shark_size, candidates, nt

N = int(input())
zone = [list(map(int, input().split())) for _ in range(N)]

shark = tuple()
shark_size = 2
candidates = 0                                                        # 공간 상에서 상어가 먹을 수 있는 물고기 후보군 수   
for i in range(N):
    for j in range(N):
        if zone[i][j] == 9:
            shark = (i, j, 0)                                         # (상어 위치 r, 상어 위치 c, 상어가 먹은 물고기 수)
        elif zone[i][j]:
            if zone[i][j] < shark_size:
                candidates += 1
t = 0
while candidates > 0:
    shark, shark_size, candidates, t = get_fish(N, zone, t, shark, shark_size, candidates)
print(t)