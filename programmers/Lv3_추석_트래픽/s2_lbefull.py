def solution(lines):
    answer = 0
    end_time = []                               # 응답 완료 시간을 ms 단위로 넣어줄 리스트
    start_time = []                             # 응답 시작 시간을 ms 단위로 넣어줄 리스트

    for line in lines:                          # 시간 데이터를 ms로 변환
        _, S, T = line.split()
        h, m, s = S.split(':')
        s, ms = s.split('.')
        end_ms = int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms)
        end_time.append(end_ms)                 # 주어진 시간은 응답 완료 시간이므로 end_time에 넣어줌

        ms = int(float(T[:-1]) * 1000)
        start_time.append(end_ms - ms + 1)      # 시작 시간을 구해서 start_time에 넣어줌
    
    start_time.sort()                           # 시작 시간은 정렬이 안되어 있으므로 오름차순 정렬
    end_idx = 0
    start_idx = 0
    cnt = 0
    while (end_idx < len(lines)) and (start_idx < len(lines)):      # 두 배열의 인덱스가 범위를 초과하기 전까지 반복
        if start_time[start_idx] < end_time[end_idx] + 1000:        # 1초간 처리하는 최대값이므로 완료시간에 1초를 더한값과 비교
            cnt += 1                                                # 시작 시간이 작으면 cnt를 늘려주고 다음 시작시간과 비교
            answer = max(cnt, answer)
            start_idx += 1
        else:                                                       # 종료시간이 작으면 cnt를 줄여주고 다음 종료시간과 비교
            cnt -= 1
            end_idx += 1

    return answer


a = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(a))
