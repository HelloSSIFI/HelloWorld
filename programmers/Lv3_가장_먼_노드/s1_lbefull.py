from collections import deque


def solution(n, edge):
    v = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)
    visited[1] = 1
    Q = deque()
    Q.append(1)
    for s, e in edge:                   # 양방향 간선 정보 저장
        v[s].append(e)
        v[e].append(s)

    while Q:
        node = Q.popleft()              # BFS 방식으로 탐색

        for e in v[node]:               # 방문하지 않은 노드를 이동횟수를 누적하여 저장
            if not visited[e]:
                Q.append(e)
                visited[e] = visited[node] + 1
    
    answer = visited.count(max(visited))
    return answer


# print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
