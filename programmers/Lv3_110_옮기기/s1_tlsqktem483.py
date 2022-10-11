def solution(s):
    answer = []

    for string in s:
        stack = []
        count_110 = 0
        for str in string:
            if (len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1' and str == '0'):
                count_110 += 1
                stack.pop()
                stack.pop()
            else:
                stack.append(str)

        count_1 = 0
        for s in stack[::-1]:
            if s == '0':
                break
            else:
                count_1 += 1
        answer.append(''.join(stack[:len(stack) - count_1]) + '110' * count_110 + '1' * count_1)
    return answer


print(solution(["1110","100111100","0111111010"]))