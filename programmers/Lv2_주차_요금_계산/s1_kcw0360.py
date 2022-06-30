from collections import defaultdict
import math

def solution(fees, records):
    answer = []
    time = defaultdict(str)
    rec = defaultdict(int)

    for i in records:
        a, b, c = i.split()
        if c == 'IN':
            time[b] = a
        elif c == 'OUT':
            x, y = time[b].split(':')
            dx, dy = a.split(':')
            temp = (int(dx)-int(x)) * 60 + (int(dy)-int(y))
            rec[b] += temp
            del time[b]

    for num, t in time.items():
        x, y = t.split(':')
        temp = (23 - int(x)) * 60 + (59 - int(y))
        rec[num] += temp

    for num, t in sorted(rec.items()):
        if t < fees[0]:
            answer.append(fees[1])
        else:
            temp = fees[1]
            t -= fees[0]
            temp += math.ceil(t/fees[2]) * fees[3]
            answer.append(temp)

    return answer