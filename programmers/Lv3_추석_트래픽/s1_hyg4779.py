from datetime import datetime, timedelta

def solution(lines):
    lines.sort()
    answer = 0
    times = []

    for line in lines:
        day, time, load = line.split()
        start = day + ' ' + time
        # 시간 데이터로 바꾸고, 1초로 범위를 잡기위해 0.5를 더한다(시작, 끝 시간을 0.5초씩 늘려서 1초 범위까지 커버하게)
        end = datetime.fromisoformat(start) + timedelta(seconds=0.5)

        # float로 바꿔서
        load = float(load.strip('s'))
        # 범위가 1초면 안되고 0.999로 잡아야 원래 시간까지 합쳐서 1초가 됨
        start = end - timedelta(seconds=load+0.999)

        times.append((start, end))

    # 각각의 시작, 끝 시간 중에
    for s, e in times:
        cnt = 0
        for os, oe in times:
            # 현재 요청의 시작이 다른 요청의 시작과 끝 사이에 있으면 +1
            if os <= s < oe :
                cnt += 1
        answer = max(answer, cnt)
        print(s, e)

    return answer