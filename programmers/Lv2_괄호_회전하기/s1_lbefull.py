def solution(s):
    answer = 0
    check = {')': '(', '}': '{', ']': '['}
    for i in range(len(s)):                                         # i칸씩 회전
        stack = []                                                  # 회전 후 올바른 괄호인지 확인할 스택
        for j in range(len(s)):                                     # 회전된 문자열 순회
            idx = (i + j) % len(s)                                  # 회전한 인덱스를 구해줌
            if s[idx] in '({[':                                     # 현재 문자가 여는 괄호일 경우
                stack.append(s[idx])                                # 스택에 넣어줌
            else:                                                   # 닫는 괄호일 경우
                if not stack or check[s[idx]] != stack.pop():       # 짝이 맞지 않으면 break
                    break
        else:                                                       # for문에서 break를 만나지 않았다면
            if not stack:                                           # stack이 비어있을 경우
                answer += 1                                         # answer + 1

    return answer
