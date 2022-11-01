from collections import defaultdict, deque


def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)

    visited = [-1] * (n+1)
    visited[destination] = 0
    q = deque()
    q.append(destination)

    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

    return [visited[num] for num in sources]
