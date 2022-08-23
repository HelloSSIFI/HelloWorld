def solution(a, b, g, s, w, t):
    answer = 4 * (10**14)    # 최대 시간
    start = 0    # 시간 값으로 이진 탐색을 하기 위해 최소, 최대 시간을 start, end 값으로 설정
    end = 4 * (10**14)

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            cnt, r = divmod(mid, (t[i]*2))    # mid라는 시간동안 편도 걸리는 시간을 통해 왕복횟수 카운트

            if r:    # 남은 시간(편도) 횟수 +1
                cnt += 1

            if g[i] < cnt * w[i]:
                gold += g[i]
            else:
                gold += cnt * w[i]

            if s[i] < cnt * w[i]:
                silver += s[i]
            else:
                silver += cnt * w[i]

            if g[i] + s[i] < cnt * w[i]:
                total += g[i] + s[i]
            else:
                total += cnt * w[i]

        if gold >= a and silver >= b and total >= a+b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer