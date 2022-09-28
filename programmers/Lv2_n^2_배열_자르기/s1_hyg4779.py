def solution(n, left, right):
    answer = []
    '''
    1. left의 위치상 숫자 확인
        left위치의 행의 숫자, +1 , + 2 + ... + n행까지가 left 위치 행의 배열 크기
        다음 행은 left보다 1씩 늘어나고 같은 작업 반복
        right위치 까지 반복
    '''
    for i in range(left, right+1):
        q, mod = divmod(i, n)
        if q < mod:
            q, mod = mod, q
        answer.append(q+1)

    return answer