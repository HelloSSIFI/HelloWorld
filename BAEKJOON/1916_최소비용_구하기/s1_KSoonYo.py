# heapq를 이용한 다익스트라 알고리즘
# 참고: https://techblog-history-younghunjo1.tistory.com/248?category=1014800
# 참고2: https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801916%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%B5%9C%EC%86%8C%EB%B9%84%EC%9A%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC
# 프림과 다익스트라 알고리즘의 차이: https://coding-insider.tistory.com/entry/Prim-vs-Dijkstra-%ED%94%84%EB%A6%BC-%EB%8B%A4%EC%9D%B5%EC%8A%A4%ED%8A%B8%EB%9D%BC-%EB%B9%84%EA%B5%90
# heapq 자료구조: https://www.daleseo.com/python-heapq/

import heapq
import sys
input = sys.stdin.readline


N = int(input())                                 # 도시의 개수(정점 개수)
M = int(input())                                 # 버스의 개수(간선 개수)

graph = [[] for _ in range(N + 1)]               # 그래프 입력 받기
for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

s, e = map(int, input().split())

q = []
INF = int(1e10)
dist = [INF] * (N + 1)
dist[s] = 0
heapq.heappush(q, (0, s))                         # 첫 시작점 노드 우선순위 큐 push -> heappush(q, (우선 순위, 값)) 우선순위가 가장 높은 값이 root에 위치

while q:
    weight, node = heapq.heappop(q)

    if dist[node] < weight:                       # 시작점에서 현재 노드 까지의 거리가 queue에 기록되어 있던 거리보다 작다면                  
        continue                                  # 최소 거리가 이미 갱신이 된 상태이므로 무시

    for next in graph[node]:                      # (next_node, weight)
        next_node, next_weight = next
        cost = weight + next_weight               # 시작점에서 현재 노드까지의 거리 + 다음 노드로 가기 위한 가중치 비용
        if dist[next_node] > cost:                # 만약 dist 정보에 기록된 값이 실제 cost보다 크다면
            dist[next_node] = cost                # 최소 거리 정보 갱신
            heapq.heappush(q, (cost, next_node))  # 힙에 삽입
            print('q:',  q)

print(dist[e])    


'''
다익스트라 일반 구현 버전(heapq 없이 구현) by 재만님

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]                        # 인접리스트 방식 저장
cost = [100000000] * (N + 1)                            # 비용 초기화
visited = [0] * (N + 1)

for i in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((e, c))                               # 인접리스트에 도착지와 비용을 저장

start, goal = map(int, input().split())
cost[start] = 0                                         # 시작점 비용은 0

for _ in range(N):                                      # 다익스트라 방식
    min_idx = 0
    min_value = 100000000
    for i in range(1, N + 1):                           # 현재 발견된 곳 중 방문하지 않았고 최소비용으로 갈 수 있는 곳을 탐색
        if not visited[i] and min_value > cost[i]:
            min_idx = i
            min_value = cost[i]
    
    visited[min_idx] = 1                                # 찾은 위치를 방문 처리

    for e, c in adj[min_idx]:                           # 해당 위치에서 인접한 노드 탐색
        if not visited[e]:                              # 방문하지 않은곳이면
            cost[e] = min(cost[min_idx] + c, cost[e])   # 현 위치에서 이동할 경우 비용이 더 싸다면 갱신
    
print(cost[goal])



'''

