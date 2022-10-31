import heapq


N, M, L = map(int, input().split())
rest = list(map(int, input().split())) + [0, L]                                         # 휴게소에 처음과 끝위치를 넣어주고 오름차순 정렬
rest.sort()
heap = []
for i in range(N + 1):                                                                  # 초기 힙에는 다음 휴게소와의 거리를 2번 넣고 해당 휴게소 인덱스를 넣어줌
    heapq.heappush(heap, [rest[i] - rest[i + 1], rest[i] - rest[i + 1], i])

div = [1] * (N + 1)                                                                     # 휴게소 인덱스와 맞춰 해당 구간에 휴게소를 지어 거리를 등분할 정수
for _ in range(M):
    cur, total, idx = heapq.heappop(heap)                                               # M개의 휴게소를 지으면서 현재 구간이 가장 긴 휴게소를 빼옴
    div[idx] += 1                                                                       # 해당 구간에 휴게소를 하나 더 짓고 등분을 1 올려줌
    cur = total // div[idx]                                                             # 해당 구간 총 거리를 등분에 맞게 나눔(음수이므로 자동올림)
    heapq.heappush(heap, [cur, total, idx])                                             # 새로운 구간값과 총 거리, 인덱스를 다시 힙에 넣어줌

print(-heap[0][0])
