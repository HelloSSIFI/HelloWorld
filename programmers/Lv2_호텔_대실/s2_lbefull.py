def solution(book_time):
    def to_minute(time):                            # 문자열 시간을 정수(분)으로 바꿔주는 함수
        time = time.split(':')
        return int(time[0]) * 60 + int(time[1])


    minute = [0] * 1440                             # 0 ~ 1439분의 객실 대여 개수를 저장할 리스트
    for s, e in book_time:
        s = to_minute(s)
        e = min(to_minute(e) + 10, 1440)            # 시작시간(s)과 종료시간(e + 10)을 정수(분)로 구해줌
        for i in range(s, e):                       # s ~ e - 1까지 대여 상황 리스트에 +1로 표시
            minute[i] += 1

    return max(minute)
