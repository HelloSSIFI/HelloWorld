from collections import  deque

def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visit = [[0]*m for _ in range(n)]
    visit[0][0] = 1

    Q = deque([(0, 0, 1)])
    while Q:
        r, c, cnt = Q.popleft()

        if r == n-1 and c == m-1:
            if answer == -1:
                answer = cnt
            else:
                answer = min(answer, cnt)
            continue

        for d in direct:
            sr, sc = r+d[0], c+d[1]
            if 0 <= sr < n and 0 <= sc < m and not visit[sr][sc] and maps[sr][sc]:
                visit[sr][sc] = 1
                Q.append((sr, sc, cnt+1))

    return answer