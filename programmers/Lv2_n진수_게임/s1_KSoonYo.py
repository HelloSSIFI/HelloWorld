def change(n, value):
    '''
    n: 진법
    value: 값
    '''
    table = {
        10: 'A', 11 : 'B', 12 : 'C',
        13: 'D', 14: 'E', 15: 'F'
    }

    if value < n:
        return str(value) if value < 10 else str(table[value])
    result = ''
    while value:
        result = (str(value % n) if value % n < 10 else str(table[value % n])) + result
        value //= n
    return result

def solution(n, t, m, p):
    answer = ''

    turn = 1
    my_turn = p
    now_num = 0
    target = ''

    while len(answer) < t:
        target = change(n, now_num)
        idx = 0
        while idx < len(target):
            if turn == my_turn and len(answer) < t:
                answer += target[idx]
                my_turn += m
                if len(answer) >= t:
                    break
            idx += 1
            turn += 1
        now_num += 1
    
    return answer

solution(2, 4, 2, 1)