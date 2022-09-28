def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        # a는 행, b는 열의 값이 된다, 그 위치 들어갈 수는 행과 열 중 큰 수에 +1 값이 들어가게 된다.
        a, b = divmod(i, n)
        answer.append(max(a, b) + 1)

    return answer