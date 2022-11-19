def dfs(str, r, c):
    global answer
    if answer < str: answer = str                                               # 현재까지 부메랑의 강도 합을 갱신
    if r == N: return                                                           # 인덱스를 벗어나면 리턴

    nr = r
    nc = c + 1
    if nc == M:                                                                 # 다음 방향 좌표를 구해줌
        nc = 0
        nr += 1

    if visited[r][c]:                                                           # 현재 좌표가 이미 부메랑에 사용된 곳이면
        dfs(str, nr, nc)                                                        # 다음 좌표 탐색 후 리턴
        return

    booms = ([[r, c - 1], [r, c], [r + 1, c]], [[r, c - 1], [r, c], [r - 1, c]], [[r - 1, c], [r, c], [r, c + 1]], [[r, c + 1], [r, c], [r + 1, c]])
    for boom in booms:                                                          # 4종류의 부메랑 탐색
        for br, bc in boom:                                                     # 각 부메랑의 좌표 탐색
            if br < 0 or N <= br or bc < 0 or M <= bc or visited[br][bc]:       # 인덱스를 벗어나거나 이미 부메랑으로 사용된 곳이면 break
                break
        else:                                                                   # 부메랑으로 사용 가능하면
            added = 0                                                           # 해당 좌표들을 부메랑으로 사용중이라고 표시
            for br, bc in boom:                                                 # 해당 부메랑의 강도를 구해줌
                visited[br][bc] = 1
                added += arr[br][bc]
                if br == r and bc == c: added += arr[br][bc]

            dfs(str + added, nr, nc)                                            # 강도를 더해주고 다음 좌표를 넣어서 재귀

            for br, bc in boom:                                                 # 재귀가 끝난 후 다시 부메랑 표시를 지워줌
                visited[br][bc] = 0

    dfs(str, nr, nc)                                                            # 현재 좌표를 부메랑으로 사용하지 않은 경우로 재귀


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = 0
dfs(0, 0, 0)
print(answer)
