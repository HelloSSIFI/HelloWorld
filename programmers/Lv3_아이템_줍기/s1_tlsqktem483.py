from collections import deque


def solution(rectangle, x, y, c, r):
    answer = float('inf')
    graph = [[2]*102 for _ in range(102)]
    visited = [[0]*102 for _ in range(102)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(y1, y2+1):
            for j in range(x1, x2+1):
                if y1 < i < y2 and x1 < j < x2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    def bfs():
        nonlocal answer

        q = deque()
        q.append([y*2, x*2])
        visited[y*2][x*2] = 1

        while q:
            i, j = q.popleft()

            if i == r*2 and j == c*2:
                answer = (visited[i][j]-1) // 2
                break

            for di in d:
                ni, nj = i + di[0], j + di[1]

                if visited[ni][nj] == 0 and graph[ni][nj] == 1:
                    q.append([ni, nj])
                    visited[ni][nj] = visited[i][j]+1

    bfs()

    return answer


print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1,1,5,7]], 1, 1, 4, 7))
print(solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10))
print(solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3))