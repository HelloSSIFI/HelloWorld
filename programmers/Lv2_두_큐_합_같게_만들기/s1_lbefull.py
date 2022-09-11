from collections import deque


def solution(queue1, queue2):
    answer = 0
    N = len(queue1) + len(queue2)
    sum_q = sum(queue1) + sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    if sum_q % 2:                                   # 두 큐의 합이 짝수가 아니면
        return -1                                   # 합을 같게 만들 수 없음
    sum_q //= 2                                     # 한 큐에 만들어야하는 값을 sum_q로 저장
    sq1 = sum(queue1)                               # 큐1의 합을 sq1으로 저장
    while sq1 != sum_q:                             # sq1이 sum_q가 될 때까지 반복
        if answer > N * 2:                          # 만약 한쪽 큐의 모든값을 다른 큐에 보냈다가 다시 받을때까지
            answer = -1                             # 반복을 해도 sum_q를 만들 수 없다면
            break                                   # sum_q를 만들 수 없음
        if sq1 > sum_q:                             # 큐1의 합이 sum_q보다 크면
            sq1 -= queue1[0]                        # 큐2로 요소를 보내줌
            queue2.append(queue1.popleft())
        else:                                       # 반대의 경우라면 큐2에서 받아옴
            sq1 += queue2[0]
            queue1.append(queue2.popleft())
        answer += 1

    return answer


# print(solution([2], [2]))
