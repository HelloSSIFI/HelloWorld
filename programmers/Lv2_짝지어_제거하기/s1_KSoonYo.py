def solution(s):
    answer = 1

    string = list(s)
    stack = ['' for _ in range(len(string))]
    top = 1
    stack[0] = string[0]

    idx = 1
    while idx < len(string):
        stack[top] = string[idx]
        if top > 0 and stack[top] == stack[top - 1]:
            top -= 1
        else:
            top += 1
        idx += 1

    if top:
        answer = 0

    return answer

print(solution('baabdcccddcd'))