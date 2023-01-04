def solution(n, l, r):
    answer = 0
    for idx in range(l, r+1):

        if idx % 5 == 3:
            continue

        temp = idx
        flag = True
        while True:
            if temp % 5 == 0:
                temp //= 5
            else:
                temp = (temp // 5) + 1

            if temp % 5 == 3:
                flag = False
                break
            elif temp <= 5:
                break

        if flag:
            answer += 1

    return answer