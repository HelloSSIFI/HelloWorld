def solution(n):
    answer = 0
    lp = 1
    rp = 1

    while True:
        temp = 0
        for i in range(lp, rp + 1):
            temp += i

        if temp == n:
            answer += 1
            if lp == n:
                break
            if rp == n:
                lp += 1
                continue
        if temp < n:
            rp += 1
        else:
            lp += 1

    return answer
