import heapq
table = {}
q = []

def solution(fees, records):
    answer = []
    # records = ['3:55 0125 IN', '5:55 0125 OUT']
    
    for record in records:
        time, car_number, car_status = record.split()
        hour, minute = list(map(int, time.split(':')))
        minutes = hour * 60 + minute
        
        if car_status == 'IN':
            if table.get(car_number):
                # 이전에 입차한 기록이 있는 경우
                table[car_number][0] = minutes
                table[car_number][3] = 'IN'
                continue
                
            table[car_number] = [minutes, 0, 0, 'IN'] # 입차 시간, 누적 시간, 요금, 차 상태
        elif car_status == 'OUT':
            table[car_number][1] += (minutes - table[car_number][0])
            table[car_number][0] = 0
            table[car_number][3] = 'OUT'
        
    for key in table.keys():
        if table[key][3] != 'OUT':
            # 입차만 하고 출차는 하지 않았다면 1439분에 출차했다고 가정
            table[key][1] += (1439 - table[key][0])
            table[key][0] = 0
            table[key][3] = 'OUT'
        
        if table[key][1] <= fees[0]:
            table[key][2] += fees[1] # 누적 시간이 기본 시간 이내라면 기본 요금만
        else:
            # 누적 시간이 기본 시간 초과라면
            # 누적 시간 중 기본 시간을 뺀 나머지 시간에서 단위 시간을 나누고
            # 단위 요금을 곱해서 추가 요금을 기본 요금에 더한다.
            extra_per_minutes = (table[key][1] - fees[0]) / fees[2]
            if extra_per_minutes > int(extra_per_minutes):
                extra_per_minutes = int(extra_per_minutes) + 1
            else:
                extra_per_minutes = int(extra_per_minutes)
            
            table[key][2] += (fees[1] +  extra_per_minutes * fees[3] )
        heapq.heappush(q, (int(key), table[key][2]))
        
    while q:
        answer.append(heapq.heappop(q)[1])
        
    return answer
    