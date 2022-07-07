def solution(expression):
    answer = float('-INF')

    operator = ['*+-', '*-+', '+*-', '+-*', '-*+', '-+*']
    numbers = list()

    pre = ''
    # 숫자와 연산자 분리해서 담음
    for i in range(len(expression)):
        if expression[i].isdigit():
            pre += expression[i]
        else:
            numbers.append(int(pre))
            numbers.append(expression[i])
            pre = ''
    numbers.append(int(pre))


    # 연산자 우선순위 를 돌면서 최댓값 갱신
    for now in operator:
        tmp = numbers[:]
        for oper in now:
            while oper in tmp:
                idx = tmp.index(oper)

                if oper == '+':
                    tmp = tmp[:idx-1] + [tmp[idx-1] + tmp[idx+1]] + tmp[idx+2:]
                elif oper == '-':
                    tmp = tmp[:idx-1] + [tmp[idx-1] - tmp[idx+1]] + tmp[idx+2:]
                else:
                    tmp = tmp[:idx-1] + [tmp[idx-1] * tmp[idx+1]] + tmp[idx+2:]

        answer = max(answer, abs(tmp[0]))

    return answer

