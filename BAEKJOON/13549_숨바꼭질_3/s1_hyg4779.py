from collections import deque


def bfs(now):
    global res

    Q = deque([now])

    while Q:
        now = Q.popleft()
        cnt = graph[now]

        if now == K:
            res = min(res, cnt)
            continue

        go = 2*now
        if go < 100001 and cnt < graph[go]:
            graph[go] = cnt
            Q.append(go)

        for go in (now-1, now+1):
            if 0 <= go < 100001 and cnt < graph[go]:
                graph[go] = cnt+1
                Q.append(go)


N, K = map(int, input().split())
graph = [100001]*100001                     # 현재 이동 시간이 담긴 그래프
graph[N] = 0                                # 출발위치 시간: 0
res = 100001                                # 이동 최소 시간

bfs(N)

print(res)