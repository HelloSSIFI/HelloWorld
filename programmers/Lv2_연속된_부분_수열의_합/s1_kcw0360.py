def solution(sequence, k):
    answer = [1111111, 9999999]
    n = len(sequence)

    interval_sum = 0    # 누적 합
    end = 0    # 마지막 idx

    for i in range(n):
        # 누적 합이 k 이상이 되거나 마지막 idx가 입력된 list의 길이를 넘지 않는 선에서 반복문 실행
        while interval_sum < k and end < n:
            interval_sum += sequence[end]
            end += 1

        if interval_sum == k:    # 누적 합이 k인 경우
            if answer[1] - answer[0] > end - 1 - i:    # 시작, 마지막 idx 차가 작은 경우 갱신
                answer = [i, end-1]
            elif (answer[1] - answer[0] == end - 1 - i) and (answer[0] > i):    # 길이가 같다면 시작 idx가 작은 경우 갱신
                answer = [i, end-1]

        interval_sum -= sequence[i]    # 현재 idx에 해당하는 값을 누적 합에서 제거 후 다음 idx 진행

    return answer