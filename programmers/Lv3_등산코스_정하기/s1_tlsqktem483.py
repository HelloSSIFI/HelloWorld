"""
DFS : 13 번 이후 시간초과
"""
from collections import defaultdict


def solution(n, paths, gates, summits):
    answer = []
    m_i = float('inf')
    graph = defaultdict(list)

    for s, e, dist in paths:
        graph[s].append([e, dist])
        graph[e].append([s, dist])

    def dfs(start, node, intensity, visited, flag):
        nonlocal m_i
        if node == start and flag:
            if intensity <= m_i:
                m_i = intensity
                answer.append([visited[0], m_i])
            return

        for n_node, di in graph[node]:
            if n_node not in visited:
                if n_node in summits and not flag:
                    temp = max(intensity, di)
                    dfs(start, n_node, temp, [n_node], True)
                elif n_node == start or n_node not in gates:
                    temp = max(intensity, di)
                    dfs(start, n_node, temp, visited+[n_node], flag)

    for gate in gates:
        dfs(gate, gate, 0, [gate], False)
    return sorted(answer, key=lambda x: (x[1], x[0]))[0]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, 	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, 	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, 	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))