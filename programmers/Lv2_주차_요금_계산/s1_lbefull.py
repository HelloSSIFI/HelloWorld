def solution(fees, records):
    in_car_time = dict()                        # key에 차량번호, value에 들어온 시간(분)을 저장
    total_car_min = dict()                      # key에 차량번호, value에 주차한 시간(분)을 저장
    car_fees = dict()                           # key에 차량번호, value에 요금을 저장
    for record in records:
        t, n, io = record.split()
        h, m = t.split(':')
        time = int(h) * 60 + int(m)             # 시간을 분으로 바꿔줌

        if io == "IN":                          # 만약 차가 들어온 기록이면
            in_car_time[n] = time               # 들어온 시간을 저장

        else:                                   # 나간거라면 저장된 시간에 현재 주차시간을 더해줌
            total_car_min[n] = total_car_min.get(n, 0) + (time - in_car_time.pop(n))

    for n, time in in_car_time.items():                                 # 위 반복이 끝났는데 나간기록이 없는 차들이 있다면
        total_car_min[n] = total_car_min.get(n, 0) + (1439 - time)      # 23:59을 분으로 바꾼 1439에서 들어온 시간을 빼서 더해줌

    for n, time in total_car_min.items():
        if time <= fees[0]:                     # 기본시간보다 적게 주차한 차는
            car_fees[n] = fees[1]               # 기본요금만 추가
            continue

        car_fees[n] = fees[1] + ((time - fees[0]) // fees[2]) * fees[3]

        if (time - fees[0]) % fees[2]:          # 기본시간 초과로 주차한 차는
            car_fees[n] += fees[3]              # 요금에 맞게 계산하여 저장

    car_fees = sorted(car_fees.items())         # 차량번호 오름차순 정렬
    answer = []
    for f in car_fees:
        answer.append(f[1])                     # 요금을 answer에 담아줌
    return answer


# print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
