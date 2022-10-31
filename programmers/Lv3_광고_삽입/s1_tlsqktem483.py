def solution(play_time, adv_time, logs):
    """
    DP : count viewer
    """

    def time_change(time):
        return int(time[:2]) * 3600 + int(time[3:5]) * 60 + int(time[6:])

    def re_change(time):
        h = time // 3600
        time -= h*3600
        h = str(h) if h >= 10 else '0' + str(h)
        m = time // 60
        time -= m*60
        m = str(m) if m >= 10 else '0' + str(m)
        s = time
        s = str(s) if s >= 10 else '0' + str(s)
        return str(h) + ":" + str(m) + ":" + str(s)

    whole_time = time_change(play_time)
    dp = [0] * (whole_time+1)

    for p in logs:
        start, end = p.split("-")
        s, e = time_change(start), time_change(end)
        dp[s] += 1
        dp[e] -= 1

    for _ in range(2):
        for i in range(1, whole_time+1):
            dp[i] = dp[i] + dp[i-1]

    ad = time_change(adv_time)
    ans = 0
    max_cnt = dp[ad-1]

    for t in range(ad, whole_time):
        if dp[t]-dp[t-ad] > max_cnt:
            max_cnt = dp[t]-dp[t-ad]
            ans = t - ad + 1

    return re_change(ans)


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]))
print(solution("50:00:00", 	"50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]))