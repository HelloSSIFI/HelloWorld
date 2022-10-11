def solution(s):
    answer = []

    for string in s:
        stack = []
        cnt = 0
        # 110 찾기
        for i in string:
            if len(stack) >= 2 and i == '0' and stack[-2] == '1' and stack[-1] == '1':
                stack.pop()
                stack.pop()
                cnt += 1
            else:
                stack.append(i)

        # 뒤에서 부터 체크해서 0이 나오는 지점까지 1의 개수 카운트하기
        check = 0
        for i in reversed(stack):
            if i == '0':
                break
            else:
                check += 1

        # 카운트한 개수 앞에 까지의 stack + 110 개수 만큼 반복 + 나머지 1 모두 추가
        answer.append(''.join(stack[:len(stack)-check]) + '110'*cnt + '1'*check)

    return answer