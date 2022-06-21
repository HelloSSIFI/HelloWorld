def solution(s):
    answer = 1       # 1로 기본값을 두어 문자열을 모두 제거한다는 결과로 가정
    check = list(s)

    if len(check) % 2:  # 문자열 길이가 홀수이면 어차피 나머지가 남기때문에 검사 전 제거
        answer = 0
        return answer

    stack = [check[0]]

    for i in range(1, len(check)):
        if stack:
            temp = stack.pop()
            if check[i] == temp:
                continue
            else:
                stack.append(temp)
                stack.append(check[i])
        else:
            stack.append(check[i])

    if stack:
        answer = 0
        return answer
    else:
        return answer