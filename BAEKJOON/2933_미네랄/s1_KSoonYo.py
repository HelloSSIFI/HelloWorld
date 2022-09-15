import sys
from collections import deque

input = sys.stdin.readline

def cast_from_left(cave, cast_height, R, C):
    for col in range(C):
        if cave[R - cast_height][col] == 'x':
            cave[R - cast_height][col] = '.'
            return (R - cast_height, col)


def cast_from_right(cave, cast_height, R, C):
    for col in range(C - 1, -1, -1):
        if cave[R - cast_height][col] == 'x':
            cave[R - cast_height][col] = '.'
            return (R - cast_height, col)


def check_cluster(loc, R, C):
    r, c = loc
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]              # 상 하 좌 우
    checked = [[False] * C for _ in range(R)]
    checked[r][c] = True

    moved_clusters = []
    q = deque()

    for d in dirs:
        sr = r + d[0]
        sc = c + d[1]
        if 0 <= sr < R and 0 <= sc < C and cave[sr][sc] == 'x' and not checked[sr][sc]:
            checked[sr][sc] = True
            q.append((sr, sc))

            flag = False
            cluster = [(sr, sc)]
            while q:
                hr, hc = q.popleft()

                for d in dirs:
                    nr = hr + d[0]
                    nc = hc + d[1]

                    if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and not checked[nr][nc]:
                        checked[nr][nc] = True
                        cluster.append((nr, nc))
                        q.append((nr, nc))

                        if nr == (R - 1):
                            flag = True
            if not flag:
                moved_clusters.append(cluster)

    return moved_clusters


def move(cave, cluster, R, C): 
    cluster.sort(key=lambda x : -x[0])                  # 클러스터 내 미네랄 위치 내림차순 정렬(행 기준)

    checked = [False] * C
    min_dist = R + 1
    for mine in cluster:
        mine_r, mine_c = mine
        
        if checked[mine_c]:                             # 클러스터 내에서 같은 열의 밑바닥 미네랄이 체크되었다면 continue
            continue
        
        checked[mine_c] = True                          

        flag = False
        for idx in range(mine_r + 1, R):
            if cave[idx][mine_c] == 'x':                # 현재 열에서 미네랄을 발견했다면 바로 위까지 거리를 측정
                min_dist = min(min_dist, idx - mine_r - 1)
                flag = True
                break
        
        if not flag:                                    # 미네랄이 없다면
            min_dist = min(min_dist, R - mine_r - 1)    # 밑바닥으로 거리 측정


    ### 이동 시작
    for mine in cluster:
        r, c = mine
        cave[r][c], cave[r + min_dist][c] = cave[r + min_dist][c], cave[r][c]


R, C = map(int, input().split())
cave = [list(input().strip()) for _ in range(R)]
N = int(input().strip())
cast_heights = list(map(int, input().split()))



# 1) 막대기 던지기, 0번째부터 짝수번째는 왼 -> 오, 1번째부터 홀수 번째는 오 -> 왼
# 2-1) 파괴된 미네랄과 인접한 클러스터 확인
# 2-2) 해당 클러스터가 바닥에 닿는지 확인, 공중에 뜬 클러스터가 있다면 선별
# 3) 공중에 뜬 클러스터를 아래로
# 4-1) 공중에 뜬 클러스터의 각각의 열에서 동굴 내 다른 미네랄이 있는 경우 -> 그 미네랄 바로 위까지 이동, 없으면 바닥까지 이동
# 4-2) 클러스터 내에서 각 열마다 돌면서 클러스터 맨 아래 바닥 행과 바닥보다 더 아래에 있는 미네랄 거리를 체크, 미네랄이 없으면 바닥까지의 거리 체크
# 5) 가장 가까운 미네랄 거리만큼 클러스터 이동, 이동할 때는 공중에 뜬 클러스터의 모든 열이 이동해야 함


# 막대기 cast
for i in range(len(cast_heights)):
    clusters = []
    if i % 2 == 0:
        mine_loc = cast_from_left(cave, cast_heights[i], R, C)
    else:
        mine_loc = cast_from_right(cave, cast_heights[i], R, C)
    
    if mine_loc:
        clusters = check_cluster(mine_loc, R, C)

    for cluster in clusters:
        move(cave, cluster, R, C)

for row in cave:
    print(''.join(row))
