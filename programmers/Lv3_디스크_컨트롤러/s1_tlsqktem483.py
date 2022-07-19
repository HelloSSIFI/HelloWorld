import heapq


def solution(jobs):
    answer, current, idx = 0, 0, 0
    s = -1
    heap = []

    while idx < len(jobs):

        for job in jobs:
            if s < job[0] <= current:
                heapq.heappush(heap, [job[1], job[0]])

        if heap:
            job = heapq.heappop(heap)
            s = current
            current += job[0]
            answer += current - job[1]
            idx += 1
        else:
            current += 1

    return answer // len(jobs)


print(solution([[0, 3], [1, 9], [2, 6]]))