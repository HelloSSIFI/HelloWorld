import heapq

def solution(n, t, m, timetable):
    # n: 운행 횟수, t: 셔틀 운행 간격, m: 셔틀 최대 수용 크루 수, timetables: 크루들이 오는 시간
    num = len(timetable)    # 크루 수
    tables = []
    for time in timetable:
        hour, min = time.split()
        tables.append(int(hour)*60+int(min))


    '''
    1. 버스가 옴. 시작 9:00
    2. 탈 수 있는 만큼 탐 (크루 수 빼기)
        1) 크루가 다 탐
            1. 수용인원이 남은 경우
            2. 수용인원이 없는 경우
    
        2) 크루가 남음: 다음 버스 기다림
    '''

    while num:



    return