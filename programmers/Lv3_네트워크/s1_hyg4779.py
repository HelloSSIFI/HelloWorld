from collections import deque

def solution(n, graph):
    answer = 0
    visit = [0]*n

    for i in range(n):
        if not visit[i]:
            visit[i] = 1
            Q = deque([i])
            while Q:
                now = Q.popleft()
                for idx, now in enumerate(graph[now]):
                    if not visit[idx] and now:
                        visit[idx] = 1
                        Q.append(idx)
            answer += 1

    return answer