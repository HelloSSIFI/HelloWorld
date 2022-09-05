def solution(operations):
    answer = [0, 0]
    q = []
    for op in operations:
        com, num = op.split()
        num = int(num)
        if com == 'I':                      # 삽입 연산일 경우
            q.append(num)                   # q에 추가
        elif q:
            if num == 1:                    # 최대값 삭제일 경우
                q.sort()                    # 오름차순 정렬
            else:                           # 최소값 삭제일 경우
                q.sort(reverse=True)        # 내림차순 정렬
            q.pop()                         # 마지막 요소 삭제
    q.sort()                                # 연산이 끝난 후 오름차순 정렬
    if q:                                   # q가 비어있지 않다면
        answer = [q[-1], q[0]]              # 최대값과 최소값을 answer에 넣어줌
    return answer
