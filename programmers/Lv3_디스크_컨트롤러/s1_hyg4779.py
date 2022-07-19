import heapq
def solution(jobs):
    # 요청 들어온 시간 to (다음요청이 끝난시간 + 요청이 걸리는 시간)이 큰 값 부터 처리
    N = len(jobs)
    ans, now, i = 0, 0, 0
    start = -1
    heap = []

    while i < N:
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if heap:
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            ans += (now-cur[1])
            i += 1
        else:
            now += 1
    return ans//N