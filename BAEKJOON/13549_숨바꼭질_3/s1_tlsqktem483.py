import sys
from collections import deque
input = sys.stdin.readline()

N, K = map(int, input.split())
max_time = 100001

q = deque()
q.append(N)

visited = [-1] * max_time
visited[N] = 0

while q:
    now = q.popleft()

    if now == K:
        print(visited[K])
        break

    for next in [now*2, now-1, now+1]:
        if next == now*2 and 0 < next < max_time and visited[next] == -1:
            visited[next] = visited[now]
            q.append(next)
        if (next == now-1 or next == now+1) and 0 <= next < max_time and visited[next] == -1:
            visited[next] = visited[now] + 1
            q.append(next)