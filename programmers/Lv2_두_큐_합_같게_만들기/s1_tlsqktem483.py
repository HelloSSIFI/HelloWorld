def solution(queue1, queue2):
    answer = -1
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    sum_t = (sum_q1 + sum_q2) // 2

    i, j, l = 0, 0, len(queue1)+len(queue2)

    while i < l and j < l and sum_q1 != sum_q2:
        if sum_q1 < sum_t:
            sum_q1 += queue2[j]
            sum_q2 -= queue2[j]
            queue1.append(queue2[j])
            j += 1
        else:
            sum_q1 -= queue1[i]
            sum_q2 += queue1[i]
            queue2.append(queue1[i])
            i += 1

    if sum_q1 == sum_t and sum_q2 == sum_t:
        answer = i + j

    return answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))