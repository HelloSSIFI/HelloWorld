import heapq
'''
python 시간초과
pypy 통과
'''
N = int(input())        # 도시 수 == 정점 수
M = int(input())        # 버스 수 == 간선 수

graph = [[] for _ in range(N+1)]        # 도시 별 갈 수 있는 도시 리스트

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])             # a에서 b로 가는 비용 c

s, e = map(int, input().split())        # 시작지 도착지
q = []

heapq.heappush(q, (0, s))               # 시작 노드로 가는 경로는 0으로 설정 후 힙q에 삽입

INF = 1e9                               # 갈 수 없는 노드 무한비용
dist = [INF]*(N+1)                      # 거리 초기화
dist[s] = 0                             # 시작노드는 거리 0


'''
힙큐를 사용한 다익스트라 알고리즘
거리가 가장 짧은 노드 우선으로 정렬되어 있음

파이썬 heapq 모듈은 우선순위 큐 알고리즘을 제공


힙 함수 활용
heapq.heappush(heap, item) : item을 heap에 추가
heapq.heappop(heap) : heap에서 가장 작은 원소를 pop & 리턴
heapq.heapify(x) : 리스트 x를 즉각적으로 heap으로 변환함 (in linear time, O(N) )
'''


while q:
    d, now = heapq.heappop(q)       # 가장 거리가 짧은 노드에 대한 정보 꺼내기
    if dist[now] < d:               # 처리된 적 있는 노드 or 이미 거리가 짧은 노드는 무시
        continue

    for i in graph[now]:            # 현재 노드가 갈 수 있는 도시에서
        cost = d + i[1]             # cost = 현재 까지 온 비용 + 해당 도시로 가는 비용
        if cost < dist[i[0]]:       # dist에 저장된 비용보다 작다면 치환
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))     # 힙에 삽입


print(dist[e])