def solution(operations):
    answer = []
    q = []
    for operation in operations:
        command, num = operation.split()
        if command == 'I':
            q.append(int(num))
            q.sort()
        else:
            if q and num == '-1':
                q.pop(0)
            elif q and num == '1':
                q.pop()
    if q:
        answer = [q[-1], q[0]]
    else:
        answer = [0, 0]
    return answer