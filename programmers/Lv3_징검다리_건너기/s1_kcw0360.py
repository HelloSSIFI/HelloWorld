from collections import deque


def solution(stones, k):
    answer = []
    q = deque()

    for idx, val in enumerate(stones):
        while q and stones[q[-1]] <= val:
            q.pop()

        q.append(idx)

        if q[0] == idx - k:
            q.popleft()

        if idx >= k - 1:
            answer.append(stones[q[0]])

    return min(answer)