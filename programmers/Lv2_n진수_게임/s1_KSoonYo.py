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
        target = change(n, now_num)                     # 현재 수를 n진법으로 변환
        idx = 0                                         # 변환한 수를 가지고 게임 시작
        while idx < len(target):                        # idx가 target의 길이 이내에 있는 동안
            if turn == my_turn and len(answer) < t:     # 나의 차례이고 답의 개수가 t를 넘지 않으면
                answer += target[idx]                   # 현재 n진법으로 변환한 수의 idx번째 수를 답으로 추가
                my_turn += m                            # 사람의 수만큼 +를 하여 다음 차례 대기
                if len(answer) >= t:                    # t의 개수 이상 답을 구했다면 곧바로 반복 중단
                    break
            idx += 1
            turn += 1
        now_num += 1
    
    return answer   

solution(2, 4, 2, 1)