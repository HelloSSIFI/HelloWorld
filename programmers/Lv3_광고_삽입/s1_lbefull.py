def solution(play_time, adv_time, logs):
    def to_sec(time):                               # 문자열 datetime을 정수형(초)으로 바꿔주는 함수
        hh, mm, ss = map(int, time.split(':'))
        return hh * 3600 + mm * 60 + ss


    play_sec = to_sec(play_time)
    adv_sec = to_sec(adv_time)
    sec = [0] * (play_sec + 1)
    for log in logs:                                # log의 시작 시간과 끝 시간을 초로 바꿔서
        s, e = log.split('-')                       # sec 리스트의 구간 시작점에 1 끝점에 -1로 표시
        ss = to_sec(s)
        es = to_sec(e)
        sec[ss] += 1
        sec[es] -= 1

    added = maxl = maxs = 0                         # added는 현재 초에 재생되는 재생 기록 수를 저장
    history = [0] * (play_sec + 1)                  # maxl과 maxs는 최대 누적 재생시간과 그 때의 광고 시작 시간을 저장
    for i in range(adv_sec + 1):                    # history는 i초에 added 했던 기록을 저장
        history[i] = added                          # 0초에 광고를 시작하여 누적 재생시간과 added를 구해줌
        maxl += added
        added += sec[i]

    cur = maxl                                      # 이후 1초씩 늘리면서 광고를 재생
    for i in range(adv_sec + 1, play_sec + 1):      # 광고가 끝나는 지점은 added로 구해서 더해주고
        cur += added                                # 광고가 시작되는 지점은 history에서 빼줌
        cur -= history[i - adv_sec]                 # 그 때마다 maxl을 비교하여 누적 재생시간이 커지면
        if maxl < cur:                              # 시작시간을 maxs에 저장
            maxl = cur
            maxs = i - adv_sec
        history[i] = added
        added += sec[i]

    mh = str(maxs // 3600).zfill(2)
    maxs %= 3600
    mm = str(maxs // 60).zfill(2)
    maxs %= 60
    ms = str(maxs).zfill(2)
    return mh + ':' + mm + ':' + ms


# print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29", "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]))
