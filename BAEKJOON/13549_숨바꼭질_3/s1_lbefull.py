from collections import deque

N, K = map(int, input().split())
visited = [0] * (100001)
Q = deque()
Q.append(N)
visited[N] = 1

while Q:                                                # BFS
    pos = Q.popleft()
    if pos == K:                                        # 현재 위치가 K가 되면 반복 종료
        break

    teleport = pos * 2                                  # 순간이동 먼저 구해줌
    while 0 < teleport < 100001:                        # 순간이동 위치가 범위 내에 있는동안 반복
        if not visited[teleport]:                       # 방문하지 않은 곳이면
            Q.append(teleport)                          # Q에 enQ 후
            visited[teleport] = visited[pos]            # 순간이동은 시간이 0초이므로 현재 위치와 동일한 시간 표시
        teleport *= 2                                   # *2 후 다시 반복
    
    for p in [pos + 1, pos - 1]:                        # 걷는 위치 반복
        if 0 <= p < 100001 and not visited[p]:          # 범위 내에 있고 방문하지 않은 곳이면
            visited[p] = visited[pos] + 1               # 현재 위치 시간+1 표시
            Q.append(p)                                 # Q에 enQ

print(visited[K] - 1)
