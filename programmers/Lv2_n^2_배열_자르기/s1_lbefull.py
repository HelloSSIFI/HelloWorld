def solution(n, left, right):
    answer = []                                 # n을 주기로 최소값이 1씩 커지므로
    min_num = left // n + 1                     # 현재 최소값을 n으로 나눠서 구해줌
    num = left % n + 1                          # 시작하는 숫자를 n으로 나눈 나머지를 통해 구해줌
    for _ in range(right - left + 1):           # left~right 까지 반복
        answer.append(max(num, min_num))        # 최소값과 현재값 중 큰 값을 넣어줌
        num += 1                                # 현재값 + 1
        if num == n + 1:                        # 현재값이 n보다 커지면
            num = 1                             # 최소값을 1올리고 현재값을 1로 바꿔줌
            min_num += 1
    return answer


# print(solution(3, 2, 5))
