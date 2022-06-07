def solution(n):

    '''
    3진법으로 취급 (0,1,2) (1,2,4)
    '''

    answer = ''         # 계산된 날짜
    quo = n             # 몫

    while quo:          # 몫이 남아있다면 반복
        quo = n//3      # 계산된 몫
        mod = n%3       # 계산된 나머지

        if mod:         # 나머지 1 또는 2가 있으면 추가
            answer += str(mod)
        else:           # 0으로 떨어졌다면 0 == 3이니까 4로 추가
            answer += '4'
            quo -= 1    # -1 해주는 이유
                        # 3일 경우 몫1 나머지0 이므로 한번 더 루프를 돌게됨. 124나라는 0이 없으니까 1을 때를 대비해서 -1해줌
        n = quo         # 몫으로 n을 치환

    return answer[::-1]