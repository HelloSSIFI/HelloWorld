o_bracket = ["(", "["]
c_bracket = [")", "]"]
match = {"(": ")", "[": "]"}
value = {")": 2, "]": 3}

brackets = input() # 괄호 문자열
stack = []         # 검사할 괄호들을 담는 스텍
result = 0         # 결과값


if brackets[0] in c_bracket:    # 첫번째 괄호 닫힌 괄호면 0
    print(0)
    exit()

for b in brackets:              # 입력 문자 순회
    if b in o_bracket:          # 열린 괄호 스텍
        stack.append(b)

    elif b in c_bracket:        # 닫힌 괄호가 나왔다면
        tmp = 0                 # 스텍에서 숫자가 나오면 담을 값

        while stack:            # 스텍 순회
            pre = stack.pop()

            if pre in o_bracket:    # 괄호일 경우
                if match[pre] == b: # 일치한다면
                    if tmp == 0:    # tmp에 없다면
                        stack.append(value[b])
                    else:           # 연속으로 숫자가 나오면 안에 있던 값 * 현재 괄호 값
                        stack.append(value[b] * tmp)
                    break
                else: # 불일치       # 괄호 매치가 안된다면 잘못된 입력값
                    print(0)
                    exit()
            else: # 숫자일 경우       # 숫자가 나온다면 tmp에 저장
                if tmp == 0:
                    tmp = pre
                else:
                    tmp += pre

# for문 끝났는데 스택에 괄호 남아있으면 유효X
for i in stack:
    if i in o_bracket or i in c_bracket:
        print(0)
        exit()
    else:
        result += i

print(result)