def solution(operations):
    q = []

    for _ in operations:
        com, num = _.split()

        if com == 'I':    # q에 숫자 넣기
            q.append(int(num))
            q.sort()  # 정렬
        else:
            if q:    # q에 숫자가 있는 경우
                if num == '1':    # 최대값 삭제
                    q.pop()
                else:    # 최소값 삭제
                    q.pop(0)

    if q:
        return [max(q), min(q)]
    else:
        return [0, 0]