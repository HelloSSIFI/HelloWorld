from collections import deque
import sys
input = sys.stdin.readline


def dfs(v):
    print(v, end=' ')                   # 방문 노드 출력
    visited[v] = 1                      # 방문표시
    
    for edge in line.get(v, []):        # 현재 노드에 연결된 노드 중 방문하지 않은 노드 방문
        if not visited.get(edge):
            dfs(edge)


def bfs(v):
    Q = deque()
    Q.append(v)                         # 시작 노드를 넣어줌
    visited = dict()                    # 시작 노드 방문표시
    visited[V] = 1

    while Q:
        s = Q.popleft()
        print(s, end=' ')               # Q에서 deQ 후 출력

        for e in line.get(s, []):       # 현재 노드에서 방문하지 않은 갈 수 있는 노드를 모두
            if not visited.get(e):      # Q에 enQ
                visited[e] = 1
                Q.append(e)


N, M, V = map(int, input().split())
line = dict()
for _ in range(M):                      # 간선 정보를 딕셔너리에 저장
    s, e = map(int, input().split())
    line[s] = line.get(s, []) + [e]
    line[e] = line.get(e, []) + [s]

for k in line:
    line[k].sort()                      # 오름차순 정렬

visited = dict()
dfs(V)

print()

bfs(V)
