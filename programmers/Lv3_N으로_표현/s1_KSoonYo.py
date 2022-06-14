min_cnt = 9

def search(num, target, cnt = 0, value = 0):
    '''
    num : 이용할 숫자
    target : 목표하는 수
    cnt : 이용할 숫자의 개수
    value : 현재 값
    '''
    global min_cnt

    if value == target:
        min_cnt = min(min_cnt, cnt)
        return

    comp_cnt = cnt                                                  # 현재 cnt의 값을 저장
    for i in range(1, 9):
        comp_cnt += i                                               # 현재 cnt에서 다음 연산을 거칠 N의 개수를 더함
        temp = int(str(num) * i)                                    # 다음 연산을 할 값

        if comp_cnt > 8:                                            # 다음 연산을 하기에 앞서 이미 개수가 8을 넘었다면 
            return                                                  # back
        else:
            search(num, target, comp_cnt, value + temp)             # 더하기 연산
            search(num, target, comp_cnt, value - temp)             # 빼기 연산
            search(num, target, comp_cnt, value * temp)             # 곱셈 연산
            if value:
                search(num, target, comp_cnt, value // temp)        # 나누기 연산
        comp_cnt = cnt                                              # 다음 연산을 거칠 N의 개수를 늘려서 또 더해야 하므로 이전에 더했던 개수를 다시 빼준다.


def solution(N, number):
    answer = 0
    search(N, number)
    if min_cnt > 8:
        answer = -1
    else:
        answer = min_cnt
    
    return answer

print(solution(5, 12))
