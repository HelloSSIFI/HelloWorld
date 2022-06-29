import sys
from collections import deque
input = sys.stdin.readline()

N, K = map(int, input.split())
max_time = 100001

q = deque()
q.append(N)

cnt = 0
visited = [-1] * max_time
visited[N] = 0
while q:
    now = q.popleft()
    possible = [now * 2, now + 1, now - 1]
    if now == K:
        cnt += 1
    for next in possible:
        if 0 <= next < max_time:
            if visited[next] == -1 or visited[next] == visited[now] + 1:
                visited[next] = visited[now] + 1
                q.append(next)

print(visited[K])
print(cnt)