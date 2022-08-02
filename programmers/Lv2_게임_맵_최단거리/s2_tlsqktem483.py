"""
2차원 visited 배열에 cnt 중첩, BFS
"""
from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    route = deque([(0, 0)])
    visited = [[-1] * m for _ in range(n)]
    visited[0][0] = 1

    while route:
        (i, j) = route.popleft()

        for di in d:
            next_i, next_j = i + di[0], j + di[1]
            if 0 <= next_i < n and 0 <= next_j < m and maps[next_i][next_j] == 1:
                if visited[next_i][next_j] == -1:
                    visited[next_i][next_j] = visited[i][j] + 1
                    route.append((next_i, next_j))

    answer = visited[-1][-1]
    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))