# 위상 정렬 이용 
# queue를 이용한 위상 정렬: https://m.blog.naver.com/ndb796/221236874984
# 진입 차수가 0인 정점을 queue에 넣는다.
# queue에서 정점을 pop하고 해당 정점과 연결된 다음 노드의 진입 차수를 -1 해준다.(간선 제거)
# 진입 차수가 0이 된 다음 노드들을 queue에 append하고 q가 빌 때까지 반복
# 조건: 사이클이 없는 방향 그래프여야 한다.
# 처음 시작하는 곳이 없거나, 모든 노드를 방문하기 전에 q가 비면 사이클 존재

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

height_list = [0] * (N + 1)
graph = [deque() for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    height_list[B] += 1
    graph[A].append(B)
    
q = deque()
result  = deque()

for idx in range(1, N + 1):
    if height_list[idx] == 0:
        q.append(idx)

while q:
    temp = q.popleft()
    result.append(temp)

    while graph[temp]:
        next_idx = graph[temp].popleft()
        height_list[next_idx] -= 1
        if height_list[next_idx] == 0:
            q.append(next_idx)

print(*result)
