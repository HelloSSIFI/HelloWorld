"""
시간초과
"""

def change(time):
    h, m = int(time[0:2]), int(time[3:])
    return h * 60 + m


def solution(n, t, m, timetable):
    answer = ''
    timetable = sorted(list(map(change, timetable)))
    start_time = 9 * 60
    end_time = 9 * 60 + (n-1) * t
    cnt = 1

    print(str(start_time//60)+":"+str(start_time%60), str(end_time//60)+":"+str(end_time%60))

    while cnt <= n:
        cnt += 1
        current = start_time + (cnt-1) * t
        for i in range(m):
            if not timetable:
                break
            if timetable[0] > current:
                break
            else:
                timetable.pop(0)
    return answer


print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))