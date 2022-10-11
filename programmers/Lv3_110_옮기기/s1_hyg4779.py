def counting(word):
    # 110을 발견하면 count를 +1 하는 함수

    count, stack = 0, []
    for _s in word:
        if _s == '0' and stack[-2:] == ['1', '1']:
            stack.pop()
            stack.pop()
            count += 1
        else:
            stack.append(_s)

    return (''.join(stack), count)



def solution(s):
    answer = []

    # 110을 제외한 문자를 찾고, 110의 개수 반환
    for string in s:
        word, cnt = counting(string)

        # 뒤에서부터 1의 개수를 셈
        n = 0
        # 0이 나온 곳 뒤에 발견한 110을 개수만큼 붙여주고, 뒤에 다시 1을 n만큼 붙임
        for i in word[::-1]:
            if i == '0':
                break
            else:
                n += 1

        answer.append(word[:len(word)-n]+'110'*cnt+'1'*n)


    return answer


print(solution(["1110","100111100","0111111010"]))
