def solution(s):
    answer = [0, 0]
    while s != '1':                         # s가 1이 될 때까지 반복
        answer[0] += 1                      # 변환 횟수 + 1
        one = 0                             # 1의 개수를 카운트할 변수
        for i in s:
            if i == '1': one += 1           # 1이라면 카운트
        answer[1] += len(s) - one           # 총 길이에서 1 개수를 뺀 개수를 0개수로 추가
        s = bin(one)[2:]                    # 1의 개수를 2진수로 변환하여 다시 반복
    return answer


# print(solution("110010101001"))
