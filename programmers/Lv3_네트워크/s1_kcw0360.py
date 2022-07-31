from collections import deque


def solution(n, computers):
    answer = 0
    visited = [0] * n

    def bfs(s):
        q = deque()
        q.append(s)

        while q:
            now = q.popleft()

            for i in range(n):
                if computers[now][i] == 1 and visited[i] == 0:
                    if i == now:
                        visited[i] = 1
                        continue
                    visited[i] = 1
                    q.append(i)

        return 1


    for i in range(n):
        if visited[i] == 0:
            answer += bfs(i)

    return answer