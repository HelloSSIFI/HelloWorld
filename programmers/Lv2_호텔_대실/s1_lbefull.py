def solution(book_time):
    def to_minute(time):                            # HH:MM 형태의 문자열 시간을 분단위 정수로 변환하는 함수
        time = time.split(':')
        return int(time[0]) * 60 + int(time[1])


    answer = cnt = 0
    start = []
    end = []
    for s, e in book_time:                          # 시작시간과 종료시간을 각각 start와 end 리스트에 저장
        start.append(to_minute(s))
        end.append(to_minute(e) + 10)

    start.sort()                                    # 두 리스트를 정렬
    end.sort()
    j = 0                                           # end 리스트의 인덱스 j
    for i in range(len(start)):                     # start 리스트 모두 탐색
        while end[j] <= start[i]:                   # 현재 시작시간보다 종료시간이 작은것들은 모두 cnt에서 빼줌
            j += 1
            cnt -= 1

        cnt += 1                                    # 현재 i번 객실 대실(cnt+1)
        if answer < cnt:                            # answer 갱신
            answer = cnt

    return answer


# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
