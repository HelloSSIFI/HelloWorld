def solution(n, t, m, timetable):
    # 시간을 분으로 변경 후 정렬
    timetable = [int(time[:2])*60 + int(time[3:5]) for time in timetable]
    timetable.sort()
    last_time = (60 * 9) + (n-1) * t    # 막차 시간 분으로 변경

    for i in range(n):    # 배차 횟수 만큼 반복
        if len(timetable) < m:    # 크루가 대기열에 도착하는 시간의 배열 길이보다 태울 수 있는 인원이 적은 경우
            a, b = divmod(last_time, 60)   # 콘은 막차를 탄다.
            return '{}:{}'.format(str(a).zfill(2), str(b).zfill(2))

        if i == n - 1:    # 마지막 셔틀 버스 일 때
            if timetable[0] <= last_time:    # 마지막 배차 시간에 우선 순위가 가장 높은 크루가 존재 하는 경우
                last_time = timetable[m-1] - 1    # 우선 순위 크루원 보다 1분 빠르게 도착한다.
            return '%02d:%02d' % (last_time // 60, last_time % 60)

        for j in range(m-1, -1, -1):    # del로 인해 idx error를 방지하기 위해 뒤에서 부터 확인
            bus = (60 * 9) + i * t    # 다음 배차 시간
            if timetable[j] <= bus:    # 다음 배차 시간 보다 작거나 같은 사람을 timetable 에서 삭제
                del timetable[j]