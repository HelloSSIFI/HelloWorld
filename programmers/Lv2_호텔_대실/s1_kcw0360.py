def solution(book_time):
    check = [0]*1440    # 0 ~ 23:59 까지를 분으로 체크하기 위한 list 생성

    for times in book_time:
        # 입력값을 분으로 변환
        sh, sm = map(int, times[0].split(':'))
        eh, em = map(int, times[1].split(':'))
        start = sh * 60 + sm
        end = eh * 60 + em + 10

        if end > 1440:    # 24시를 넘어가는 경우 24시로 통일
            end = 1440

        for idx in range(start, end):    # 대실하는 시간에 체크
            check[idx] += 1

    return max(check)    # 방의 수가 가장 많이 대실하고 있을 때 값을 출력