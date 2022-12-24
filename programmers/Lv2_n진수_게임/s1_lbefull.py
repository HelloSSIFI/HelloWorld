def solution(n, t, m, p):
    tr = list('0123456789ABCDEF')
    def trans(num, n):                          # 10진수를 n진수로 변환하는 함수
        if num == 0:                            # 0일 경우 '0' 반환
            return '0'

        result = []
        while num > 0:                          # 한자리씩 찾아가며 num이 0이 될 때까지 반복
            result.append(tr[num % n])          # n으로 나눈 나머지를 끝자리에 추가하고
            num //= n                           # num 을 n으로 나누어 줌

        return result[::-1]                     # 숫자가 거꾸로 쌓이므로 뒤집어서 리턴


    answer = []
    total = []
    num = 0
    while len(total) < t * m:                   # m명이 t번씩 말하므로 길이가 t * m이 될 때까지 반복
        total.extend(trans(num, n))             # 숫자를 1씩 올려가며 n진수로 변환한 값을 total에 넣어줌
        num += 1

    for i in range(p - 1, t * m, m):            # p번 차례부터 m씩 올려가면서 말해야 하는 수를 answer에 추가
        answer.append(total[i])

    return ''.join(answer)


# print(solution(2, 4, 2, 1))
