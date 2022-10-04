import sys

input = sys.stdin.readline

def get_boundery(s, here, dirs, d = 0, boundery = []):
    r, c = here 

    if d == 3 and s == here:                                # 방향이 우상이면서 현재 노드가 시작점이라면
        bounderies.append(boundery)
        return

    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if 0 < nr <= N and 0 < nc <= N and not visited[nr][nc]:
        visited[nr][nc] = True
        # 방향이 우상일 때는 가는 방향 그대로만 간다.
        # 시작점은 항상 우하 방향으로 출발
        if d == 3:
            get_boundery(s, (nr, nc), dirs, d = d, boundery = boundery[:] + [(nr, nc)])
        else:
            # 그대로 가거나
            get_boundery(s, (nr, nc), dirs, d = d, boundery = boundery[:] + [(nr, nc)])

            # turn
            get_boundery(s, (nr, nc), dirs, d = d + 1, boundery = boundery[:] + [(nr, nc)])
        visited[nr][nc] = False

def get_distance(boundery):
    # 경계선 배열에서 거꾸로 순회하면서 열의 숫자가 다시 커지는 경우 -> d1
    d1 = 0
    
    # 경계선 배열에서 처음부터 순회하면서 열의 숫자가 다시 작아지는 경우 -> d2
    d2 = 0

    for i in range(len(boundery) - 1, -1, -1):
        if boundery[i][1] < boundery[i - 1][1]:
            break
        d1 += 1

    for j in range(len(boundery)):
        if boundery[j][1] < boundery[j - 1][1]:
            break
        d2 += 1

    return d1, d2


def get_population(city, boundery, d1, d2, N):
    global minV

    table = [0, 0, 0, 0, 0, 0]

    x, y = boundery[-1]

    boundery_table = [[] for _ in range(N + 1)]

    for loc in boundery:
        loc_r, loc_c = loc
        boundery_table[loc_r].append(loc_c)


    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if (len(boundery_table[r]) == 1 and c == boundery_table[r][0]) or (len(boundery_table[r]) == 2 and boundery_table[r][1] <= c <= boundery_table[r][0]):
                table[5] += city[r][c]   
                continue

            # 선거구 조건에 따라 합산
            if 1 <= r < x + d1 and 1 <= c <= y:
                table[1] += city[r][c]

            if 1 <= r <= x + d2 and y < c <= N:
                table[2] += city[r][c]

            if x + d1 <= r <= N and 1 <= c < y - d1 + d2:
                table[3] += city[r][c]
            
            if x + d2 < r <= N and y - d1 + d2 <= c <= N:
                table[4] += city[r][c]

    table = table[1:]
    minV = min(minV, max(table) - min(table))


N = int(input())
city = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]


'''
1. 5번 선거구의 경계션을 구한다 -> dfs 이용, 시계방향으로 한 칸씩
2-1. 5번 선거구의 인구 총합을 구한다.
2-2. 5번 선거구를 기준으로 좌상 1번, 우상 2번, 좌하 3번, 우하 4번 선거구의 인구 총합을 구한다.
2-3 선거구별 최대 인구수와 최소 인구수의 차이를 구한다.
3. (x, y) 가 (1, 2) 일 때부터 (N - 2, N - 1) 일 때까지 1번과 2번과정을 반복해서 인구수 차이의 최솟값 도출
'''


minV = 20 * 20 * 100 + 1

# 시작점을 돌면서 boundery가 가능한 경우 모두 수집
for i in range(1, N - 1):
    for j in range(2, N):
        visited = [[False] * (N + 1) for _ in range(N + 1)]
        bounderies = []
        dirs = [[1, 1], [1, -1], [-1, -1], [-1, 1]]             # 시계 방향 대각선 이동(우하, 좌하, 좌상, 우상)
        get_boundery((i, j), (i, j), dirs)
        

        # 바운더리를 돌면서 각각의 선거구 총합을 구하고 인구 차이 계산
        # 이후 최소값과 비교하면서 갱신
        for boundery in bounderies:
            d1, d2 = get_distance(boundery)
            get_population(city, boundery, d1, d2, N)

print(minV)

