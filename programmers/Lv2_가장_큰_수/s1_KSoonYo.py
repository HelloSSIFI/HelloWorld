import heapq
from itertools import permutations


def solution(numbers):
    answer = '0'
    nums = list(map(str, numbers))
    perm = list(permutations(nums, len(numbers)))
    q = []

    for num_set in perm:
        num = int(''.join(num_set))
        heapq.heappush(q, (-num, num))
    answer = heapq.heappop(q)[1]
    return str(answer)
solution([0, 0, 0])