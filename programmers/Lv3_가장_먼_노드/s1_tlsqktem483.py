from collections import deque

def solution(n, edges):
    """
    :param n:
    :param edges:
    :return:

     BFS 풀이
    """
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    queue = deque([1])

    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)

    visited[1] = 1

    while queue:
        current = queue.popleft()

        for next in graph[current]:
            if not visited[next]:
                visited[next] = visited[current] + 1
                queue.append(next)

    max_count = max(visited)
    ans = visited.count(max_count)
    return ans if ans else 1

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))