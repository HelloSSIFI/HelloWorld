def solution(n, k):
    answer = 0
    res = ''
    m = 12

    while n > 0:
        num = k**m
        if num > n:
            res += str(0)
        else:
            a, b = divmod(n, num)
            res += str(a)
            n = b

        m -= 1

    temp = res.split('0')

    for i in temp:
        if i == '' or int(i) == 1:
            continue

        check = True
        for j in range(2, int(int(i)**0.5) + 1):
            if int(i) % j == 0:
                check = False
                break

        if check:
            answer += 1

    return answer
