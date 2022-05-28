def solution(lines):
    answer = 0
    time_info = []
    for line in lines:
        _, S, T = line.split()
        h, m, s = S.split(':')
        s, ms = s.split('.')
        end_ms = int(h) * 3600000 + int(m) * 60000 + int(s) * 1000 + int(ms)

        ms = int(float(T[:-1]) * 1000)
        time_info.append((end_ms - ms + 1, end_ms))
    
    for time in time_info:
        for ref in time:
            cnt = 0
            for s, e in time_info:
                if ref <= s < ref + 1000 or ref <= e < ref + 1000:
                    cnt += 1
                elif s <= ref <= e:
                    cnt += 1
                if e > ref + 4000:
                    break
            answer = max(answer, cnt)

    return answer


a = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]

print(solution(a))
