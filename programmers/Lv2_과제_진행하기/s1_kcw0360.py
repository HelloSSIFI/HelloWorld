def solution(plans):
    answer = []
    plan = []
    stack = []
    length = len(plans)
    info = dict()
    for name, start, playtime in plans:
        h, m, = map(int, start.split(':'))
        playtime = int(playtime)
        start = h*60 + m    # 분으로 변환
        info[start] = [name, playtime]    # dict에 시간에 따른 정보 저장
        plan.append([name, start, playtime])

    plan.sort(key=lambda x: x[1])    # 과제 시작 시간으로 정렬

    time, cnt = plan[0][1], 0    # 현재 시간, 완료한 과제 수

    while cnt < length:
        if stack:    # 현재 하고 있는 과제가 존재하는경우
            stack[-1][1] -= 1    # 가장 먼저 해야하는 과제 1분 과제 수행
            if stack[-1][1] == 0:    # 가장 먼저 해야하는 과제를 완료했다면 answer에 추가하고 stack에서 제거
                answer.append(stack[-1][0])
                stack.pop()
                cnt += 1    # 완료한 과제 카운트

        if time in info:    # 현재 시간에 시작해야하는 과제가 존재하는 경우
            stack.append(info[time])    # stack에 그 과제 추가

        time += 1    # 1분씩 시간이 흐름

    return answer