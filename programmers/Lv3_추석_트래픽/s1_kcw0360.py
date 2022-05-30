def search(start, change_time):
    cnt = 0    # 카운트 초기화
    end = start + 1000    # 1초간 처리하는 요청을 찾기 위해

    for check in change_time:    # 각 로그의 시간들이 해당 시간안에 포함이 되는지 확인
        if check[0] < end and check[1] >= start:    # 임의시간부터 1초기 때문에 end 시간에 끝나는 값은 포함하지 않는다.
            cnt += 1    # 시간내 포함되는 작업이 있다면 +1

    return cnt

def solution(lines):
    answer = 0
    change_time = []    # 각 로그의 시간을 ms로 변경한 후 [시작 시간, 종료 시간] 형태로 리스트에 추가

    for line in lines:    # 문자열 시간을 ms로 변환
        temp = line.split()
        end_time = (int(temp[1][:2]) * 3600 + int(temp[1][3:5]) * 60 + int(temp[1][6:8])) * 1000 + int(temp[1][9:])
        start_time = end_time - float(temp[2][:-1]) * 1000 + 1    # 시작 시간 포함 해야 하므로 1ms 더한다.
        change_time.append([start_time, end_time])

    for times in change_time:    # 각 로그의 시간 값에서 최대 처리량 찾기
        answer = max(answer, search(times[0], change_time), search(times[1], change_time))
    return answer