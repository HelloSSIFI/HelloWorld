from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum = sum(queue1)

    # 두 큐 합의 절반
    target = (q1_sum + sum(queue2)) // 2
    cnt = 0

    while queue1 and queue2:
        # 두 큐 합이 같으면 종료
        if q1_sum == target:
            return cnt

        # queue1의 합이 더 크면 queue1에서 빼기
        elif q1_sum > target:
            q1_sum -= queue1.popleft()

        # queue1의 합이 queue2보다 작을 때
        else:
            queue1.append(queue2.popleft())
            q1_sum += queue1[-1]
        cnt += 1

    return -1  # 두 큐 합이 같아지지 않으면 -1 반환