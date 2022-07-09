import sys
input = sys.stdin.readline

N = int(input())
jump_map = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]                      # 목적지에 도착하는 경로는 1 이상, 도착하지 못하는 경로는 0
cnt = 0
def dfs(s, e):

    if dp[s[0]][s[1]]:                                              # 이미 경로 수를 기록해놨던 경로라면 해당 dp 테이블의 값 반환
        return dp[s[0]][s[1]]

    if s == e:                                                      # 목적지에 도착한 경우 1 리턴
        return 1
    elif jump_map[s[0]][s[1]] == 0:                                 # 더 갈 수 있는 방향이 없으면 0 리턴
        return 0 

    dx = [jump_map[s[0]][s[1]], 0]                                  # 아래쪽 방향, 오른쪽 방향
    dy = [0, jump_map[s[0]][s[1]]]
    for i in range(2):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            dp[s[0]][s[1]] += dfs((nx, ny), e)                      # 목적지에 도착한 경우의 경로 수 누적
    
    return dp[s[0]][s[1]]

    
dfs((0, 0), (N-1, N-1))
cnt = dp[0][0]
print(cnt)




