def solution(n, t, m, timetable):
    int_table = []
    for time in timetable:                              # 시간 정보가 담긴 리스트를
        hh, mm = time.split(':')                        # 문자열에서 정수 분으로 바꿔줌
        int_table.append(int(hh) * 60 + int(mm))
    
    int_table.sort()                                    # 오름차순 정렬
    idx = 0
    for i in range(n):                                  # 셔틀버스를 n회 운영하면서
        cnt = 0                                         # 조건에 맞게 사람을 태워줌
        while cnt < m and idx < len(int_table) and int_table[idx] <= 540 + i * t:
            cnt += 1
            idx += 1
    
    if idx != 0:                                        # 반복이 끝났을 때 한명도 못태운 경우가 아니라면
        idx -= 1                                        # 버스에 마지막으로 탄 사람을 봐야 하므로 인덱스-1
    
    time = (n - 1) * t + 540                            # 마지막 버스 운행 시간을 구해줌
    pos = min(time, int_table[idx] - 1)                 # 마지막 운행시간과 마지막 탑승시간-1 중 작은것을 선택
    if cnt < m:                                         # 만약 마지막 버스에 m명보다 적게 탔다면
        pos = time                                      # 마지막 운행시간을 선택

    hh = str(pos // 60)                                 # 선택한 시간을 다시 문자열로 바꿔서 출력
    mm = str(pos % 60)
    if len(hh) == 1:
        hh = '0' + hh
    if len(mm) == 1:
        mm = '0' + mm

    return hh + ':' + mm

# print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))
