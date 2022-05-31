def count(period_start, logs):
    # 구간 시작부터 1초까지 처리 개수를 count
    cnt = 0
    period_end = period_start + 1000 - 1

    # log[0]: 처리 시작 시간, log[1] : 처리 완료 시간
    for log in logs:
        if log[1] >= period_start and log[0] <= period_end:
            # 1초 구간 안에 걸쳐 있으면 count +1
            cnt += 1

    return cnt


def solution(lines):
    answer = 0
    max_cnt = 0
    logs = []
    for line in lines:
        time_record = line.split() # ['2016-09-15', '20:59:57.421', '0.351s']
        period = float(time_record[2].replace('s', ''))
        h, m, s = list(map(float, time_record[1].split(':'))) 
        
        # ms 변환
        period *= 1000
        end_time =  (1000 * 60 * 60) * h + (1000 * 60) * m  + 1000 * s

        # 시작 시간 구하기
        start_time = end_time - period + 1

        # 로그 기록 추가
        logs.append((start_time, end_time))

    
    for log in logs:
        max_cnt = max(max_cnt, count(log[0], logs)) 
        max_cnt = max(max_cnt, count(log[1], logs)) 
    
    answer = max_cnt

    return answer


