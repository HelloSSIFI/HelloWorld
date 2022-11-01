import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline

# 현재 노드에서 갈 수 있는 방향대로 출발하여, 최소 비용을 계속 갱신
def boost(r, c, d):

    if r == N:
        return 0

    if dist[r][c][d] != float('inf'):
        return dist[r][c][d]

    if d != 0 and c - 1 >= 0:
        # 이전 방향이 왼쪽이 아니고 다음 c의 범위가 맵에서 벗어나지 않는 경우
        dist[r][c][d] = min(dist[r][c][d], boost(r + 1, c - 1, 0) + MAP[r][c])

    if d != 1:
        # 이전 방향이 중앙이 아닌 경우
        dist[r][c][d] = min(dist[r][c][d], boost(r + 1, c, 1) + MAP[r][c])

    if d != 2 and c + 1 < M:
        # 이전 방향이 오른쪽이 아니고 다음 c의 범위가 맵에서 벗어나지 않는 경우
        dist[r][c][d] = min(dist[r][c][d], boost(r + 1, c + 1, 2) + MAP[r][c])

    return dist[r][c][d]

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

# dist[i][j][d]: (i, j) 칸에서 d 방향으로 출발하였을 때, 목적지까지의 최소 비용 
# 0: 왼, 1: 중, 2: 오, 3: 맨 처음 출발지의 방향 정보
dist = [[[float('inf')] * 4 for _ in range(M)] for _ in range(N)]


minF = 100 * 1000 * 1000
for s in range(M):
    # 지도의 첫 행이 출발지 후보들
    # 첫 출발지에서는 이전 방향에 대한 정보가 없으므로 다음에 갈 수 있는 모든 방향을 고려해야 한다. -> 방향 정보로 -1 입력
    minF = min(minF, boost(0, s, -1))

print(minF)


# 다른 풀이
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j][d] : (i, j) 칸에 d 방향으로 도착했을 때 비용
# d : (0, 1, 2) -> (왼쪽, 중앙, 오른쪽)
dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0:
            for idx in range(3):
                dp[i][j][idx] = graph[i][j]

        else:
            if j == 0:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i][j]           # 왼쪽 대각선 아래로 (i, j)에 올 수 있는 이전 칸에서 현재 칸의 연로를 더하여 필요한 연료값 계산
                dp[i][j][1] = dp[i - 1][j][0] + graph[i][j]                                         # 가장 왼쪽 j이므로 d[i-1][j][2]는 고려할 필요가 x

            elif j == M-1:
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + graph[i][j]
                dp[i][j][1] = dp[i - 1][j][2] + graph[i][j]

            else:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i][j]
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i][j]
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + graph[i][j]

ans = float('inf')

for c in range(M):
    ans = min(ans, min(dp[N-1][c][:]))
print(ans)

