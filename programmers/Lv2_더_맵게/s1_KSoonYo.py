import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    after_swap = lambda x, y : x + (y * 2)

    # heapq의 가장 작은 값이 K 이상이면 끝
    while True:
        if len(scoville) < 2:
            break
        
        x = heapq.heappop(scoville)
        if x >= K:
            break

        y = heapq.heappop(scoville)
        z = after_swap(x, y)
        
        heapq.heappush(scoville, z)
        answer += 1

    if heapq.heappop(scoville) < K:
        answer = -1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))

