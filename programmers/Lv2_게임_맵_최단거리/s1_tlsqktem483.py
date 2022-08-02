"""
효율성 테스트 Fail
"""
def solution(maps):
    n, m = len(maps), len(maps[0])
    answer = n * m + 1
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def dfs(i, j, route):
        nonlocal answer
        if i == n-1 and j == m-1:
            answer = min(answer, len(route))
            return

        for di in d:
            next_i, next_j = i + di[0], j + di[1]
            n_route = route[::]

            if 0 <= next_i < n and 0 <= next_j < m and maps[next_i][next_j] == 1 and (next_i, next_j) not in route:
                n_route.append((next_i, next_j))
                dfs(next_i, next_j, n_route)

    dfs(0, 0, [(0, 0)])

    if answer > n * m:
        answer = -1

    return answer


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))