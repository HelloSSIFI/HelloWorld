def solution(lines):
    answer = 0
    start = []
    end = []

    for line in lines:
        time = line.split()
        start.append(start_time(time[1], time[2]))
        end.append(to_millisecond(time[1]))

    for i in range(len(lines)):
        cnt = 0
        current = end[i]

        for j in range(i, len(lines)):
            if current > start[j] - 1000:
                cnt += 1
        answer = cnt if cnt > answer else answer

    return answer

def to_millisecond(time):
    # To second
    h = int(time[:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:8])
    m_s = int(time[-3:])

    # To millisecond
    return (h + m + s) * 1000 + m_s

def start_time(time, time_gap):
    # To millisecond
    gap = int(float(time_gap[:-1]) * 1000)
    return to_millisecond(time) - gap + 1