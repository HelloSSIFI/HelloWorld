import sys
input = sys.stdin.readline

n = int(input())

wall = []
for _ in range(n):
    wall.append(list(map(int, input().split())))

answer = 0

def dfs(now, direction):
    global answer

    if now == [n-1, n-1]:
        answer += 1
        return

    if direction == 0 or direction == 1:
        if now[1] + 1 < n:
            if wall[now[0]][now[1] + 1] != 1:
                dfs([now[0], now[1] + 1], 0)

    if direction == 1 or direction == 2:
        if now[0] + 1 < n:
            if wall[now[0] + 1][now[1]] != 1:
                dfs([now[0] + 1, now[1]], 2)

    if direction == 0 or direction == 1 or direction == 2:
        if now[0] + 1 < n and now[1] + 1 < n:
            if wall[now[0]][now[1] + 1] != 1 and wall[now[0] + 1][now[1]] != 1 and wall[now[0] + 1][now[1] + 1] != 1:
                dfs([now[0] + 1, now[1] + 1], 1)

start = [0, 1]
dfs(start, 0)

print(answer)
