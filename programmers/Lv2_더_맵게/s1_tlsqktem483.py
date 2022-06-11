import heapq

def solution(s, k):
    heap = sorted(s)
    cnt = 0
    while heap[0] < k:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
            cnt += 1
        except IndexError:
            return -1
    return cnt