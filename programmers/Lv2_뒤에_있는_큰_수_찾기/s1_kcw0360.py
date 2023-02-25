import heapq


def solution(numbers):
    answer = [-1] * len(numbers)

    heap = []

    for i in range(len(numbers)):
        val = numbers[i]

        while heap and heap[0][0] < val:
            _, idx = heapq.heappop(heap)
            answer[idx] = val

        heapq.heappush(heap, [val, i])

    return answer