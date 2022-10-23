def conversion(s):
    cnt = 0    # 제거되는 0의 개수
    for i in s:
        if i == '0':
            cnt += 1

    temp = bin(len(s)-cnt)[2:]    # 2진수로 변환 (type: str)

    return [cnt, temp]


def solution(s):
    answer = [0, 0]

    while s != '1':
        answer[0] += 1    # 변환 횟수 +1
        del_zero, s = conversion(s)
        answer[1] += del_zero    # 제거된 제로 횟수 추가

    return answer