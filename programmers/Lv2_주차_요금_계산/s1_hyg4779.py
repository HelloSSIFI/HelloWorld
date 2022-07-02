from collections import defaultdict
from datetime import datetime, timedelta
'''
요금 = 기본 시간 + (누적 주차 시간 - 기본 시간)/단위 시간, 나누어 떨어 지지 않는 다면 올림 처리

차량 번호가 작은 차부터 청구 요금을 return
'''

def solution(fees, records):
    answer = defaultdict(list)              # 차량 번호별 주차시간을 담을 변수

    # 기본 시간, 기본 요금, 단위 시간, 단위 요금
    base_time, base_fee, a, a_fee = fees
    for _ in records:
        t, n, s = _.split()     # 시간, 번호, 입출차
        answer[n].append(t)

    # 차량번호 별 시간 계산
    for now in answer:
        rec = answer[now]
        tmp = 0
        for i in range(1, len(rec), 2):
            OUT = int(rec[i][:2])*60 + int(rec[i][3:])                  # 나간 시간
            IN = int(rec[i-1][:2])*60 + int(rec[i-1][3:])                       # 들어온 시간

            tmp += OUT - IN

        if len(rec)%2:
            tmp += 23*60 + 59 - (int(rec[-1][:2])*60 + int(rec[-1][3:]))    # 입차만 있다면 23:59에서 출차 빼기

        tmp -= base_time                            # 기본시간 빼기

        if tmp <= 0:
            res = base_fee

        else:

            if tmp%a:       # 나머지가 있다면 +1
                res = tmp//a + 1
            else:
                res = tmp//a

            res = res*a_fee + base_fee

        answer[now] = res

    result = [i[1] for i in sorted(list(answer.items()), key= lambda x: x[0])]
    print(result)
    return result


solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])