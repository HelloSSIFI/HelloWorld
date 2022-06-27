import math


def get_time(i, o):
    in_time = int(i[:2]) * 60 + int(i[3:])
    out_time = int(o[:2]) * 60 + int(o[3:])
    return out_time - in_time


def charge(t, f):
    base_t, base_f, per_t, per_f = f[0], f[1], f[2], f[3]

    if t <= base_t:
        return base_f
    else:
        remain_time = t - base_t
        return base_f + math.ceil(remain_time / per_t) * per_f


def solution(f, record):
    dict_car = {}
    dict_ans = {}
    ans = []

    for r in record:
        t, car_n, state = r.split()

        if state == 'IN':
            dict_car[car_n] = t
        else:
            if car_n in dict_ans.keys():
                dict_ans[car_n] += get_time(dict_car[car_n], t)
            else:
                dict_ans[car_n] = get_time(dict_car[car_n], t)
            dict_car[car_n] = 0

    for k, v in dict_car.items():
        # 미 출차 차량 계산
        if v:
            if k in dict_ans.keys():
                dict_ans[k] += get_time(dict_car[k], "23:59")
            else:
                dict_ans[k] = get_time(dict_car[k], "23:59")

        # 금액 청구
        dict_ans[k] = charge(dict_ans[k], f)

    for temp in sorted(dict_ans.items()):
        ans.append(temp[1])
    return ans


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))