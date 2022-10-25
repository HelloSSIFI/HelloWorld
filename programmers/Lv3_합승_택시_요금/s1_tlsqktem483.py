"""
시간초과
"""
from collections import defaultdict


def solution(n, s, a, b, fares):
    """
    Floyd Warshall
    """
    ans = float('inf')
    n_dict = defaultdict(list)

    def floyd_warshall():
        nonlocal n_dict
        dist = [[float('inf')] * n for _ in range(n)]

        for i, j, edge in fares:
            n_dict[i-1].append(j-1)
            n_dict[j-1].append(i-1)
            dist[i - 1][j - 1] = edge
            dist[j - 1][i - 1] = edge

        for k in range(n):
            dist[k][k] = 0
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist

    distance = floyd_warshall()

    def dfs(cur, route, cnt):
        nonlocal ans

        if cnt >= ans:
            return

        cost = cnt + distance[cur][a-1] + distance[cur][b-1]

        if ans > cost:
            ans = cost

        for n_node in n_dict[cur]:
            if n_node not in route:
                dfs(n_node, route+[n_node], cnt+distance[cur][n_node])

    dfs(s-1, [s-1], 0)

    return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
