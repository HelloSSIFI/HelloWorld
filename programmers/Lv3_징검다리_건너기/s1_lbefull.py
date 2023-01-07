from collections import defaultdict
import heapq


def solution(stones, k):
    answer = max(stones[:k])                                # 각각의 좌표 위치에서 k만큼 인접한 위치에 있는 디딤돌 중
    adj = defaultdict(int)                                  # 숫자가 가장 큰 값이 해당 구간을 최대로 넘어갈 수 있는 숫자를 의미함
    heap = []                                               # 이러한 최대값들의 집합 중 가장 작은 값이 전체 징검다리를 건널 수 있는 최대인원이 됨
    for i in range(k):                                      # adj에는 인접한 k위치에 디딤돌 숫자가 몇개씩 있는지를 저장
        adj[stones[i]] += 1                                 # heap에는 인접한 k위치에있는 수들을 최대값 힙으로 저장
        heap.append(-stones[i])                             # 먼저 0 ~ k - 1 까지의 값들을 각각 adj와 heap에 넣어줌
    heapq.heapify(heap)

    for i in range(k, len(stones)):                         # k부터 stones의 끝까지 반복
        adj[stones[i]] += 1                                 # adj에서 현재 위치의 숫자를 1 늘려주고
        adj[stones[i - k]] -= 1                             # 구간에서 없어진 위치(i - k)의 숫자를 1 빼줌
        heapq.heappush(heap, -stones[i])                    # 힙에는 현재 위치의 숫자를 넣어주고
        while not adj[-heap[0]]:                            # 힙의 최대값을 찾기위해 이미 없어진 숫자들을 힙에서 제거
            heapq.heappop(heap)                             # 이렇게 하면 현재 구간 k에서의 최대값은 heap[0]에 저장
        if answer > -heap[0]:                               # 현재 구간에서 최대값이 answer보다 작으면 갱신(모든 구간의 최대값 집합에서 최소값을 선택)
            answer = -heap[0]
    return answer


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
