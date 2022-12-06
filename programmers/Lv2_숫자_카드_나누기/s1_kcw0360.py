import math


def solution(arrayA, arrayB):
    answer = 0
    # 중복제거
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))

    tmp1 = arrayA[0]
    for i in range(1, len(arrayA)):
        tmp1 = math.gcd(tmp1, arrayA[i])

    for i in arrayB:    # 1번 조건
        if i % tmp1 == 0:
            break
    else:
        answer = max(tmp1, answer)

    tmp2 = arrayB[0]
    for i in range(1, len(arrayB)):
        tmp2 = math.gcd(tmp2, arrayB[i])

    for i in arrayA:    # 2번 조건
        if i % tmp2 == 0:
            break
    else:
        answer = max(tmp2, answer)

    return answer


print(solution([14, 35, 119], [18, 30, 102]))