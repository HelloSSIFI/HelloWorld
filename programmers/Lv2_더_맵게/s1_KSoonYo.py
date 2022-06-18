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


'''
deque를 이용한 풀이 by 재만님
heapq 실행시간의 절반으로 줄일 수 있다.

from collections import deque


def solution(scoville, K):
    answer = 0
    Q = deque()
    scoville.sort()
    scoville = deque(scoville)
    while (Q and scoville and (Q[0] < K or scoville[0] < K)) or (not Q and scoville and scoville[0] < K) or (Q and not scoville and Q[0] < K):
        A = -1
        B = -1
        answer += 1
        if (not Q and scoville) or (Q and scoville and Q[0] >= scoville[0]):
            A = scoville.popleft()
        
        elif (Q and not scoville) or (Q and scoville and Q[0] < scoville[0]):
            A = Q.popleft()

        if (not Q and scoville) or (Q and scoville and Q[0] >= scoville[0]):
            B = scoville.popleft()
        
        elif (Q and not scoville) or (Q and scoville and Q[0] < scoville[0]):
            B = Q.popleft()
        
        if A > -1 and B > -1:
            Q.append(A + B * 2)
    
    if not Q and not scoville:
        answer = -1

    return answer


'''

