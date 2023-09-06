import heapq
from itertools import combinations_with_replacement, permutations


def solution(k, n, reqs):
    answer = float('inf')

    schedule = [[] for _ in range(k)]
    for req in reqs:
        schedule[req[2]-1].append([req[0], req[1]])

    cases = set()
    arr = [i for i in range(1, n - k + 2)]
    for com in combinations_with_replacement(arr, k):
        if com not in cases and sum(com) == n:
            for per in permutations(com, k):
                cases.add(per)

    for case in cases:
        total = 0

        for i in range(k):
            heap = [0] * case[i]

            for st, du in schedule[i]:
                prev = heapq.heappop(heap)
                if st >= prev:
                    heapq.heappush(heap, st + du)
                else:
                    total += prev - st
                    heapq.heappush(heap, prev + du)

        answer = min(answer, total)

    return answer