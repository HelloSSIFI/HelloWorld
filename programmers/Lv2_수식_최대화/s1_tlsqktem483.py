from itertools import permutations


def calculation(n1, n2, op):
    if op == '+':
        return str(int(n1) + int(n2))
    elif op == '-':
        return str(int(n1) - int(n2))
    elif op == '*':
        return str(int(n1) * int(n2))


def solution(expression):
    ans = 0
    exp = []
    operations = []
    temp = ''
    for e in expression:
        if e.isdigit():
            temp += e
        else:
            exp.append(temp)
            exp.append(e)
            if e not in operations:
                operations.append(e)
            temp = ''
    exp.append(temp)

    ops = list(permutations(operations))

    for op in ops:
        stack = exp[::]

        for o in op:
            end_point = len(stack[::])
            idx = 0
            while idx < end_point:
                temp = stack.pop(0)
                if temp == o:
                    stack.append(calculation(stack.pop(), stack.pop(0), o))
                    idx += 2
                else:
                    stack.append(temp)
                    idx += 1
        if abs(int(stack[0])) > ans:
            ans = abs(int(stack[0]))

    return ans


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))