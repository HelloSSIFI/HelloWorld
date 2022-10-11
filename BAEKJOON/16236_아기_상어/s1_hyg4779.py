from collections import deque, defaultdict
def minCostPath(n, graph, x, y):
    # Write your code here
    answer = float('inf')
    visit = [0 for _ in range(n+1)]

    # 현재위치, 현재까지 거리, x방문 여부, y 방문여부
    Q = deque([(1, 0, 1)])
    while Q:
        now, dist, key = Q.popleft()

        # 5번 노드에 방문했을 때
        if now == n:
            # x번, y번 모두 방문했다면
            if key & 1 << x and key & 1 << y:
                answer = min(answer, dist)


        for node, cost in graph[now]:
            nkey = key
            # 현재 상태로 방문한 적이 없는 노드면
            if not nkey & visit[node]:
                nkey |= 1 << node
                visit[node] = nkey
                Q.append((node, dist+cost, nkey))

    return answer



g_nodes, g_edges = map(int, input().rstrip().split())
graph = [[] for _ in range(g_nodes+1)]


for i in range(g_edges):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

x = int(input().strip())

y = int(input().strip())

result = minCostPath(g_nodes, graph, x, y)
print(result)