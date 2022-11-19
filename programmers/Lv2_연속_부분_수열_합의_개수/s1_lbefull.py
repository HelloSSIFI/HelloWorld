def solution(elements):
    total = set()
    N = len(elements)
    sum_e = sum(elements)                           # 수열의 합을 구해놓음
    total.add(sum_e)                                # 수열의 합을 경우의 수에 추가
    elements *= 2                                   # 원형 수열로 표현하기위해 기존 수열의 길이를 2배로 늘림
    for i in range(1, N // 2 + 1):                  # 연속되는 i만큼의 합을 구해서 total에 추가
        for j in range(N):                          # 전체 합에서 위에서 구한 합을 빼주면 (N - i)개로 연속되는 합과 같으므로
            num = sum(elements[j:j + i])            # 1 ~ 전체길이의 반 까지만 반복하여 경우의 수를 구함
            total.add(num)
            total.add(sum_e - num)
    return len(total)


# print(solution([7, 9, 1, 1, 4]))
