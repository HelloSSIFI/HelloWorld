def solution(X, Y):
    answer = ''
    cnt_X = dict()                                  # X의 각 숫자가 몇번씩 나왔는지 저장
    cnt_Y = dict()                                  # Y의 각 숫자가 몇번씩 나왔는지 저장
    for i in range(9, -1, -1):                      # 딕셔너리 초기화
        cnt_X[str(i)] = 0
        cnt_Y[str(i)] = 0
    for c in X:                                     # 숫자 카운트
        cnt_X[c] += 1
    for c in Y:
        cnt_Y[c] += 1

    for k in cnt_X:                                 # 두 딕셔너리에 공통으로 나온 숫자 중 카운트가 적은것을 큰 숫자 순서로 answer에 추가
        answer += k * min(cnt_X[k], cnt_Y[k])
    
    if not answer:                                  # 만약 하나도 없다면 -1
        answer = '-1'

    if answer.count('0') == len(answer):            # 0으로만 이루어졌다면 0
        answer = '0'

    return answer


# print(solution('100', '2345'))
