def solution(queue1, queue2):
    q1 = queue1 + queue2
    q2 = queue2 + queue1
    sum_q1 = sum(queue1)    # 입력값의 queue1의 합
    sum_q2 = sum(queue2)    # 입력값의 queue2의 합
    result = (sum_q1 + sum_q2) // 2    # 각 큐의 합이 되어야 하는 값
    # popleft, append를 각 큐의 가장 앞에 있는 idx로 값을 더하고 뺄 예정
    idx1 = 0    # queue1의 가장 선두에 있는 idx
    idx2 = 0    # queue2의 가장 선두에 있는 idx
    end = len(q1) - 1    # idx의 최대값, 큐에 1개의 원소라도 남아 있어야 한다.

    while idx1 < end and idx2 < end and sum_q1 != sum_q2:
        if sum_q1 < result:    # queue1의 결과값이 목표값 보다 작은 경우
            sum_q1 += q2[idx2]    # queue2의 첫 번째 원소 pop한 후 queue1에 더한다.
            sum_q2 -= q2[idx2]    # pop한 만큼 감소
            idx2 += 1    # queue2에서 pop했기 때문에 idx 한 칸 이동

        if sum_q1 > result:    # queue1의 결과값이 목표값 보다 큰 경우
            sum_q1 -= q1[idx1]    # 첫번째 원소 pop => queue1의 합에서 첫번째 원소 크기 만큼 감소
            sum_q2 += q1[idx1]    # pop한 원소 append => queue2의 합에서 pop한 값만큼 증가
            idx1 += 1    # pop했기 때문에 idx 한 칸 이동

    if sum_q1 == sum_q2:
        return idx1 + idx2
    return -1